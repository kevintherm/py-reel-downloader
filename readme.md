# Instagram Reel Downloader

Simple Instagram reel downloader using python and selenium.

## Usage

To use this project is quite simple and straight forward.

\*Make sure to select which driver you're using, I've setup 2 driver (chrome and firefox) Other than that you can setup your own driver and it's mobile emulation.

1. Clone this project `git clone [url]`
2. Go to project directory `cd [dir]`
3. Run the script `py main.py`
4. Paste the url, and enter the output filename (default=video.mp4)

### Error Messages

1. `Failed to Obtain Video URL`: Instagram changes url serving on their end, or failed to use mobile emulation on selenium resulting instagram delivering the url as a blob
2. `Failed to fetch video. Check internet connection`: Failed to fetch video file, returned status is not 200
