import requests
import os

def download_file(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded: {filename}")

def split_file(filename, parts):
    filesize = os.path.getsize(filename)
    part_size = filesize // parts
    with open(filename, 'rb') as f:
        for i in range(parts):
            with open(f"{filename}.part{i+1}", 'wb') as part_file:
                if i == parts - 1:  # last part takes the remainder
                    part_file.write(f.read())
                else:
                    part_file.write(f.read(part_size))
    print(f"Split into {parts} parts.")

if __name__ == "__main__":
    url = "https://windsurf-stable.codeium.com/api/update/win32-x64-user/stable/latest"  # <- Replace this
    filename = "downloaded_file.zip"
    download_file(url, filename)
    split_file(filename, 10)
