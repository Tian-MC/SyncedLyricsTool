

# LyricsSync

**Automatically embed synchronized lyrics (LRC) into your audio files (MP3 and FLAC).**

LyricsSync is a Python script that searches for synchronized lyrics (in LRC format) based on the artist and title of your audio files and embeds them directly into the file's metadata. It supports MP3 and FLAC formats.

----------

## Features

-   **Automatic Lyrics Search**: Fetches synchronized lyrics (LRC) using the `syncedlyrics` library.
-   **Metadata Handling**: Reads artist and title metadata from audio files.
-   **Lyrics Embedding**: Embeds lyrics into the audio file's metadata:
    -   MP3: Uses ID3 tags.
    -   FLAC: Uses Vorbis comments.
-   **Easy to Use**: Just run the script, and it processes all supported audio files in the directory.
----------

## Ignoring the 401 Error

If you encounter a `401 Unauthorized` error while running the script, it means the lyrics provider has restricted access. This is a known issue with some external APIs. You can safely ignore this error, as the script will work.

----------

## Installation

### 1. Clone the repository

    git clone https://github.com/Tian-MC/SyncedLyricsTool.git
    cd SyncedLyricsTool

### 2. Install dependencies

Make sure you have Python 3.7 or higher installed. Then, install the required libraries:

```pip install mutagen syncedlyrics```

----------

## Usage

1.  Place your audio files (MP3 or FLAC) in the same directory as the script.
2.  Run the script:

python lyricsync.py

The script will:

-   Extract the artist and title from each file's metadata.
-   Search for synchronized lyrics (LRC) online.
-   Embed the lyrics into the audio file if found.

----------

## Example

    LyricsSync/  
    ├── song1.mp3  
    ├── song2.flac  
    └── lyricsync.py

Running the script:

    python lyricsync.py

Output:

    Processing: Artist Name - Song Title  
    Synced lyrics added to song1.mp3  
    No synced lyrics found for Artist Name - Song Title

----------

## Supported Formats

-   **MP3**: Lyrics are embedded in ID3 tags.
-   **FLAC**: Lyrics are embedded in Vorbis comments.

----------

## Dependencies

-   `mutagen`: For handling audio metadata.
-   `syncedlyrics`: For fetching synchronized lyrics.

----------

## Code Overview

### Key Functions

-   **get_synced_lyrics(artist, title)**
    
    -   Searches for synchronized lyrics (LRC) using the artist and title.
    -   Returns the lyrics as a string or None if not found.
-   **add_lyrics_to_audio(file_path, lyrics)**
    
    -   Embeds the lyrics into the audio file's metadata.
    -   Supports MP3 (ID3 tags) and FLAC (Vorbis comments).
-   **get_metadata(file_path)**
    
    -   Extracts the artist and title from the audio file's metadata.
    -   Returns None for unsupported formats.
-   **main()**
    
    -   Scans the current directory for audio files.
    -   Processes each file by fetching and embedding lyrics.

----------

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

