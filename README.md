![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

# PySide6 Music Player

A simple music player application built with Python, PySide6, and SQLite.

## Features

- Play, pause, and stop music playback.
- Adjust the volume.
- Seek through the music track.
- Open and play individual audio files.
- "Like" songs to save them to a playlist.
- View and play songs from your "Liked Songs" playlist.
- Basic playlist functionality (next/previous song).
- Mute and unmute the volume.

## Requirements

- Python 3
- PySide6
- SQLite3 (usually included with Python)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/PySide6-MusicPlayer.git
    cd PySide6-MusicPlayer
    ```

2.  **Install dependencies:**
    ```bash
    pip install PySide6
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

## How to Use

1.  **Open a Music File:**
    - Click on "File" -> "Open Music" to select an audio file (`.mp3`, `.wav`, `.flac`).
    - The music will start playing automatically.

2.  **Playback Controls:**
    - **Play/Pause:** Toggle between playing and pausing the current track.
    - **Stop:** Stop the music playback.
    - **Seek Bar:** Drag the slider to seek to a specific part of the track.
    - **Volume:** Adjust the volume using the volume slider.
    - **Mute/Unmute:** Click the volume icon to mute or unmute the audio.

3.  **Liked Songs:**
    - **Like a Song:** While a song is playing, click the heart icon to "like" it. This will add the song to your "Liked Songs" playlist.
    - **View Liked Songs:** Click on "File" -> "Liked Songs" to see a list of all your liked songs.
    - **Play a Liked Song:** Click on any song in the "Liked Songs" menu to play it.

4.  **Playlist:**
    - **Next/Previous:** Use the next and previous buttons to navigate through your "Liked Songs" playlist.

## Database

The application uses an SQLite database (`music_player.db`) to store the file paths of your liked songs. This file is created automatically in the application's directory.

## Code Structure

-   **`main.py`**: The main entry point of the application. It contains the main window logic, event handling, and media player controls.
-   **`MusicWindow.py`**: The UI class generated from the `.ui` file. It defines the graphical user interface elements.
-   **`database.py`**: Handles all database operations, including creating the database, and adding, removing, and retrieving liked songs.
-   **`resources.qrc`**: The Qt resource file that bundles icons and other assets into the application.
-   **`resource.py`**: The Python file generated from the `.qrc` file.
-   **`icons/`**: Directory containing the icons used in the application.


