# from ChatGPT prompt: extract enclosure url
import requests
import xml.etree.ElementTree as ET

# Fetch the RSS feed
url = 'Enter RSS URL Here'
response = requests.get(url)

# Parse the XML
root = ET.fromstring(response.content)

# Extract titles and enclosure URLs
for item in root.findall('.//item'):
    # Extract the title
    title = item.find('title').text
    print(f"Title: {title}")
    
    # Extract the enclosure URL (if it exists)
    enclosure = item.find('enclosure')
    if enclosure is not None:
        enclosure_url = enclosure.get('url')
        print(f"Enclosure URL: {enclosure_url}")
    else:
        print("No enclosure URL found")

    print()  # Blank line between items
