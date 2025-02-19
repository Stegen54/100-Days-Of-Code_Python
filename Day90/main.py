import requests
import os
import re

def sanitize_filename(filename):
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Convert to ASCII-compatible string
    filename = filename.encode('ascii', 'ignore').decode('ascii')
    return filename if filename else "unknown"

# Fetch 10 users from the API
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)

if response.status_code != 200:
    print("Error: Couldn't get API data")
else:
    users = response.json()["results"]
    
    # Ensure directory exists
    os.makedirs("user_images", exist_ok=True)

    for person in users:
        first_name = person["name"]["first"]
        last_name = person["name"]["last"]
        image_url = person["picture"]["medium"]
        
        # Create sanitized filename
        safe_name = sanitize_filename(f"{first_name} {last_name}")
        filename = f"user_images/{safe_name}.jpg"
        
        # Download and save the image
        img_data = requests.get(image_url).content
        with open(filename, "wb") as img_file:
            img_file.write(img_data)
        
        try:
            print(f"Saved: {filename}")
        except UnicodeEncodeError:
            print("Saved file (name contains special characters)")
