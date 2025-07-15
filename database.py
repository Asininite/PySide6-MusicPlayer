# FILE: database.py
import sqlite3
import os

# Get the directory of the current script to ensure the database is created there.
APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, 'music_player.db')

def create_database():
    """Creates the database and the liked_songs table if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # The 'UNIQUE' constraint prevents duplicate paths from being added.
    c.execute('''
        CREATE TABLE IF NOT EXISTS liked_songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_liked_song(path):
    """Adds a song path to the liked_songs table."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO liked_songs (path) VALUES (?)", (path,))
        conn.commit()
    except sqlite3.IntegrityError:
        # This error occurs if the song path is already in the database,
        # which is fine. We can safely ignore it.
        print(f"Song already liked: {path}")
    finally:
        conn.close()

def remove_liked_song(path):
    """Removes a song path from the liked_songs table."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM liked_songs WHERE path=?", (path,))
    conn.commit()
    conn.close()

def get_all_liked_songs():
    """Retrieves all liked song paths from the database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT path FROM liked_songs ORDER BY id")
    # fetchall() returns a list of tuples, e.g., [('path1',), ('path2',)]
    # The list comprehension extracts the first item from each tuple.
    songs = [item[0] for item in c.fetchall()]
    conn.close()
    return songs

def is_song_liked(path):
    """Checks if a song is in the liked_songs table."""
    if not path:
        return False
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # We select 1, which is slightly more efficient than selecting the whole path.
    c.execute("SELECT 1 FROM liked_songs WHERE path=?", (path,))
    result = c.fetchone()
    conn.close()
    return result is not None