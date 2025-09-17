import os
import requests
import xml.etree.ElementTree as ET
import subprocess
import re

# Prompt user for RSS URL and output folder
url = input("Enter RSS URL: ").strip()
output_dir = input("Enter output directory (default: './downloads'): ").strip() or "downloads"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Fetch and parse RSS
response = requests.get(url)
root = ET.fromstring(response.content)

# Extract titles and process the first item
for item in root.findall('.//item'):
    title = item.find('title').text
    sanitized = re.sub(r'[^\w\s-]', '', title)
    sanitized = sanitized.replace(' ', '_').strip('_')
    base_filename = sanitized
    mp3_filename = base_filename + ".mp3"
    opus_filename = base_filename + ".opus"
    mp3_path = os.path.join(output_dir, mp3_filename)
    opus_path = os.path.join(output_dir, opus_filename)

    enclosure = item.find('enclosure')
    enclosure_url = enclosure.get('url')

    # aria2c download command
    aria2c_command = [
        'aria2c',
        '--continue=true',
        '--no-conf',
        '--console-log-level=warn',
        '--summary-interval=0',
        '--download-result=hide',
        '--http-accept-gzip=true',
        '--file-allocation=none',
        '-x16',
        '-j16',
        '-s16',
        '--min-split-size=1M',
        '--header=User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        '--header=Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        '--header=Accept-Language:en-us,en;q=0.5',
        '--check-certificate=true',
        '--remote-time=true',
        '--show-console-readout=true',
        '--auto-file-renaming=false',
        '--out', mp3_path,
        enclosure_url
    ]

    print(f"Downloading: {mp3_filename} from {enclosure_url}")
    subprocess.run(aria2c_command)

    # Convert to Opus
    ffmpeg_command = [
        'ffmpeg',
        '-i', mp3_path,
        '-c:a', 'libopus',
        '-b:a', '32k',
        '-ac', '1',
        opus_path
    ]
    print(f"Converting to Opus: {opus_filename}")
    subprocess.run(ffmpeg_command)

    # Optional: Delete original mp3
    os.remove(mp3_path)
    print(f"Deleted original MP3: {mp3_filename}")

    print(f"Conversion complete. Output saved to: {opus_path}")
    break  # Stop after one download

