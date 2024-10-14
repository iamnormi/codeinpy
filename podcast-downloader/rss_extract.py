import requests
import xml.etree.ElementTree as ET
import subprocess
import re

# Fetch the RSS feed
url = 'Enter RSS URL Here'
response = requests.get(url)

# Parse the XML
root = ET.fromstring(response.content)

# Extract titles
for item in root.findall('.//item'):
    title = item.find('title').text
    sanitized = re.sub(r'[^\w\s-]', '', title)
    sanitized = sanitized.replace(' ', '_')
    sanitized = sanitized.strip('_')
    sanitized_title = sanitized + ".mp3"

    enclosure = item.find('enclosure')
    enclosure_url = enclosure.get('url')
    aria2c_command = [
        'aria2c',
        '--continue=true',  # Set --continue option explicitly
        '--no-conf',
        '--console-log-level=warn',
        '--summary-interval=0',
        '--download-result=hide',
        '--http-accept-gzip=true',
        '--file-allocation=none',
        '-x16',  # Number of connections per server
        '-j16',  # Number of parallel downloads
        '-s16',  # Number of splits for each file
        '--min-split-size=1M',
        '--header=User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        '--header=Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        '--header=Accept-Language:en-us,en;q=0.5',
        '--check-certificate=true',
        '--remote-time=true',
        '--show-console-readout=true',
        '--auto-file-renaming=false',
        '--out', sanitized_title,  # Output file name
        enclosure_url  # URL of the file to download
    ]
    print(f"Downloading: {sanitized_title} from {enclosure_url}")
    subprocess.run(aria2c_command)




