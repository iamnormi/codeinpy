# from ChatGPT prompt: run tile and url with aria2c
import requests
import xml.etree.ElementTree as ET
import subprocess
import re

# Function to sanitize filenames
def sanitize_title(title):
    # Remove non-alphanumeric characters except spaces and hyphens
    sanitized = re.sub(r'[^\w\s-]', '', title)
    sanitized = sanitized.replace(' ', '_')  # Replace spaces with underscores
    return sanitized.lower()  # Return the sanitized and lowercase title

# Fetch the RSS feed
url = 'Enter RSS URL Here'
response = requests.get(url)

# Parse the XML
root = ET.fromstring(response.content)

# Extract titles and enclosure URLs and run aria2c for each
for item in root.findall('.//item'):
    title = item.find('title').text
    enclosure = item.find('enclosure')
    
    if enclosure is not None:
        enclosure_url = enclosure.get('url')
        sanitized_title = sanitize_title(title) + ".mp3"  # Assuming mp3 files, adjust as necessary
        
        # Run aria2c to download the file
        aria2c_command = ['aria2c', '-o', sanitized_title, enclosure_url]
        
        print(f"Downloading: {sanitized_title} from {enclosure_url}")
        subprocess.run(aria2c_command)
    else:
        print("No enclosure URL found for this item.")
