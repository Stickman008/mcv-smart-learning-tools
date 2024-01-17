import gdown

def download_file_from_drive(url, destination_path):
    try:
        gdown.download(url, destination_path, quiet=False)
        print(f"File downloaded to {destination_path}")
    except gdown.DownloadError as e:
        if "Permission denied" in str(e):
            print("Permission denied. You may need to change the file permissions or use the Google Drive API for restricted files.")
        else:
            print(f"Error downloading file: {e}")