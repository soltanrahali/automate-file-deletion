import os
import datetime

def delete_old_jpeg_files(directory, months_threshold=6):
    now = datetime.datetime.now()
    six_months_ago = now - datetime.timedelta(days=months_threshold * 30)

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if filename.lower().endswith('.jpeg') and modification_time < six_months_ago:
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    downloads_directory = os.path.expanduser("~/Downloads")
    delete_old_jpeg_files(downloads_directory)
