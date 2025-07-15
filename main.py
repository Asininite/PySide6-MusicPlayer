# FILE: main.py
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTime
from PySide6.QtGui import QIcon, QAction

# Import the new database module
import database
from MusicWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.muted = True
        # This will store the file path of the currently loaded song
        self.current_song_path = None
        self.current_playlist = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Music Player Application')

        # --- Database Initialization ---
        # Create the database and 'liked_songs' table on startup
        database.create_database()

        self.ui.toolButtonPlay.setEnabled(False)
        self.ui.toolButtonNext.setEnabled(False)
        self.ui.toolButtonPrevious.setEnabled(False)

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        self.audioVolumeLevel = 70
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(self.audioVolumeLevel / 100.0)

        # --- Add a "Like" button to the UI ---
        # NOTE: This assumes you have added a QToolButton named 'toolButtonLike' in Qt Designer
        # or you are adding it programmatically. For this example, we assume it exists.
        # If it doesn't, you'll get an AttributeError. See the next section for how to add it.
        try:
            self.ui.toolButtonLike.clicked.connect(self.toggle_like_song)
            self.ui.toolButtonLike.setEnabled(False) # Disable until a song is loaded
        except AttributeError:
            print("WARNING: 'toolButtonLike' not found in your UI file. Please add it.")


        # --- Original Connections ---
        self.ui.actionOpen_Music.triggered.connect(self.open_music)
        self.ui.toolButtonPlay.clicked.connect(self.play_pause_music)
        self.ui.horizontalSliderVolume.sliderMoved.connect(self.volume_slider_changed)
        self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
        self.ui.horizontalSliderPlay.sliderMoved.connect(self.play_slider_changed)
        self.ui.toolButtonStop.clicked.connect(self.player.stop)
        self.ui.toolButtonVolume.clicked.connect(self.volume_mute)

        # --- New "Liked Songs" Menu ---
        self.liked_songs_menu = QMenu("Liked Songs", self)
        self.ui.menuFile.addMenu(self.liked_songs_menu)
        # The 'aboutToShow' signal dynamically populates the menu right before it is shown
        self.liked_songs_menu.aboutToShow.connect(self.populate_liked_songs_menu)

        # --- Player Signal Connections ---
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        # Update the play/pause button icon when the player state changes
        self.player.playbackStateChanged.connect(self.update_play_pause_icon)
        self.player.mediaStatusChanged.connect(self.handle_media_status_changed)

        # --- Playlist Connections ---
        self.ui.toolButtonNext.clicked.connect(self.play_next_song)
        self.ui.toolButtonPrevious.clicked.connect(self.play_previous_song)


    def open_music(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Music", "", "Audio Files (*.mp3 *.wav *.flac)")
        if fileName:
            self.current_song_path = fileName
            self.player.setSource(QUrl.fromLocalFile(fileName))
            self.ui.toolButtonPlay.setEnabled(True)
            self.ui.toolButtonLike.setEnabled(True)
            self.ui.toolButtonNext.setEnabled(True)
            self.ui.toolButtonPrevious.setEnabled(True)
            self.update_like_button_status()
            self.player.play()

    def play_pause_music(self):
        # This function now correctly toggles between play and pause.
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def update_play_pause_icon(self, state):
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.ui.toolButtonPlay.setIcon(QIcon(":/icons/pause.png"))
        else:
            self.ui.toolButtonPlay.setIcon(QIcon(":/icons/play.png"))

    def position_changed(self, position):
        if self.ui.horizontalSliderPlay.maximum() != self.player.duration():
            self.ui.horizontalSliderPlay.setMaximum(self.player.duration())
        self.ui.horizontalSliderPlay.setValue(position)

        # Corrected time calculation
        seconds = (position / 1000) % 60
        minutes = (position / 60000) % 60
        hours = (position / 3600000) % 24
        time = QTime(int(hours), int(minutes), int(seconds))
        self.ui.labelTimer.setText(time.toString('hh:mm:ss'))

    def duration_changed(self, duration):
        self.ui.horizontalSliderPlay.setRange(0, duration)

    def volume_slider_changed(self, position):
        self.audioVolumeLevel = position
        self.audio.setVolume(position / 100.0)

    def play_slider_changed(self, position):
        self.player.setPosition(position)

    def volume_mute(self):
        if self.muted:
            self.audio.setMuted(True)
            self.ui.horizontalSliderVolume.setValue(0)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/mute.png"))
            self.muted = False
        else:
            self.audio.setMuted(False)
            self.ui.horizontalSliderVolume.setValue(self.audioVolumeLevel)
            self.ui.toolButtonVolume.setIcon(QIcon(":/icons/volume.png"))
            self.muted = True

    # --- Liked Songs Functions ---

    def toggle_like_song(self):
        """Adds or removes the current song from the liked songs database."""
        if not self.current_song_path:
            return
        if database.is_song_liked(self.current_song_path):
            database.remove_liked_song(self.current_song_path)
        else:
            database.add_liked_song(self.current_song_path)
        self.update_like_button_status()

    def update_like_button_status(self):
        """Updates the like button icon based on whether the current song is liked."""
        if database.is_song_liked(self.current_song_path):
            # NOTE: You will need to add these icons to your resources.qrc file
            self.ui.toolButtonLike.setIcon(QIcon(":/icons/heart-filled.png"))
            self.ui.toolButtonLike.setChecked(True)
        else:
            self.ui.toolButtonLike.setIcon(QIcon(":/icons/heart-outline.png"))
            self.ui.toolButtonLike.setChecked(False)

    def populate_liked_songs_menu(self):
        """Clears and refills the 'Liked Songs' menu with songs from the database."""
        self.liked_songs_menu.clear()
        liked_songs = database.get_all_liked_songs()
        if not liked_songs:
            self.liked_songs_menu.addAction("No liked songs yet").setEnabled(False)
            return

        for song_path in liked_songs:
            # Get just the filename to display in the menu
            file_name = os.path.basename(song_path)
            # Use a lambda with a default argument to correctly capture the song_path
            action = QAction(file_name, self)
            action.triggered.connect(lambda checked=False, path=song_path: self.play_liked_song(path))
            self.liked_songs_menu.addAction(action)

    def play_liked_song(self, path):
        """Plays a song selected from the 'Liked Songs' menu."""
        self.current_song_path = path
        self.player.setSource(QUrl.fromLocalFile(path))
        self.ui.toolButtonLike.setEnabled(True)
        self.ui.toolButtonNext.setEnabled(True)
        self.ui.toolButtonPrevious.setEnabled(True)
        self.update_like_button_status()
        self.player.play()

    # --- Playlist Functions ---

    def handle_media_status_changed(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.play_next_song()

    def play_next_song(self):
        if not self.current_playlist:
            self.current_playlist = database.get_all_liked_songs()
        
        if not self.current_playlist:
            return

        try:
            current_index = self.current_playlist.index(self.current_song_path)
            next_index = (current_index + 1) % len(self.current_playlist)
            self.play_liked_song(self.current_playlist[next_index])
        except ValueError:
            # If the current song is not in the playlist, play the first song
            self.play_liked_song(self.current_playlist[0])

    def play_previous_song(self):
        if not self.current_playlist:
            self.current_playlist = database.get_all_liked_songs()

        if not self.current_playlist:
            return

        try:
            current_index = self.current_playlist.index(self.current_song_path)
            prev_index = (current_index - 1) % len(self.current_playlist)
            self.play_liked_song(self.current_playlist[prev_index])
        except ValueError:
            # If the current song is not in the playlist, play the last song
            self.play_liked_song(self.current_playlist[-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())