
from os import walk
from os.path import join, relpath
import zipfile
from datetime import date
import os

source_dir = r"C:\Users\User\Desktop\BEREN"
backup_dir = r"C:\Users\User\Desktop\YEDEK"

def backup_files():
    os.makedirs(backup_dir, exist_ok=True)

    today = date.today()
    zip_path = join(backup_dir, f"backup_{today}.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in walk(source_dir):
            for file in files:
                file_path = join(root, file)
                arcname = relpath(file_path, source_dir)
                zipf.write(file_path, arcname)

    print("Yedekleme tamamlandı:", zip_path)

backup_files()
