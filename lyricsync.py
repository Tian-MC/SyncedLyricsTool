"""
Lyrics Synchronizer

This script automatically searches for synchronized lyrics (LRC format) for audio files (MP3 and FLAC) in the current directory and embeds them into the files' metadata. 
It uses the `syncedlyrics` library to fetch the lyrics and `mutagen` to handle audio metadata.

Steps:
1. Scans the current directory for audio files.
2. Extracts artist and title metadata from the files.
3. Searches for synchronized lyrics (LRC) using the artist and title.
4. Embeds the lyrics into the audio file's metadata (ID3 tags for MP3, Vorbis comments for FLAC).

Supported formats: MP3, FLAC
Dependencies: mutagen, syncedlyrics
"""

import os
from syncedlyrics import search
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, USLT
from mutagen.easyid3 import EasyID3

def get_synced_lyrics(artist, title):
    # Search for synchronized lyrics (LRC)
    try:
        lrc_text = search(f"{artist} {title}")  # Remove allow_plain_format
        return lrc_text
    except Exception as e:
        print(f"Error while searching for lyrics: {e}")
        return None

def add_lyrics_to_audio(file_path, lyrics):
    # Get file extension
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.mp3':
        # Handle metadata for MP3 files
        audio = MP3(file_path, ID3=ID3)
        if not audio.tags:
            audio.add_tags()
        audio.tags.add(USLT(encoding=3, lang='eng', desc='Lyrics', text=lyrics))
        audio.save()
    elif ext == '.flac':
        # Handle metadata for FLAC files
        audio = FLAC(file_path)
        audio['lyrics'] = lyrics
        audio.save()
    else:
        print(f"Unsupported format: {ext}")

def get_metadata(file_path):
    # Get file extension
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.mp3':
        # Read metadata for MP3 files
        audio = MP3(file_path, ID3=EasyID3)
        artist = audio.get('artist', ['Unknown Artist'])[0]
        title = audio.get('title', ['Unknown Title'])[0]
    elif ext == '.flac':
        # Read metadata for FLAC files
        audio = FLAC(file_path)
        artist = audio.get('artist', ['Unknown Artist'])[0]
        title = audio.get('title', ['Unknown Title'])[0]
    else:
        print(f"Unsupported format: {ext}")
        return None, None

    return artist, title

def main():
    # Get the current directory path (where the script is located)
    folder_path = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                # Get artist and title from metadata
                artist, title = get_metadata(file_path)
                if artist is None or title is None:
                    print(f"Unable to read metadata for {filename}")
                    continue

                print(f"Processing: {artist} - {title}")

                # Download synchronized lyrics
                lrc_text = get_synced_lyrics(artist, title)
                if lrc_text:
                    # Add lyrics to the audio file
                    add_lyrics_to_audio(file_path, lrc_text)
                    print(f"Synced lyrics added to {filename}")
                else:
                    print(f"No synced lyrics found for {artist} - {title}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()