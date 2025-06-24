import os
import shutil
import zipfile
from utils import ensure_dir
from img2payload_gustyx import create_payload_image


def print_colored(msg, color="cyan"):
    colors = {
        "cyan": "\033[96m",
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "end": "\033[0m"
    }
    print(f"{colors.get(color, '')}{msg}{colors['end']}")
    

def handle_repack(input_dir, output_file):
    print(f"[+] Repacking: {input_dir} -> {output_file}")
    create_payload_image(input_dir, output_file)
    print("[+] Done repacking.")

REPACK_INPUT_DIR = 'Repack-Input'
REPACK_OUTPUT_DIR = 'Repack-Output'

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)
    print(f"✅ Repacked: {output_path}")

def main():
    ensure_dir(REPACK_OUTPUT_DIR)

    folders = [d for d in os.listdir(REPACK_INPUT_DIR) if os.path.isdir(os.path.join(REPACK_INPUT_DIR, d))]
    if not folders:
        print("❗ No Detection Folder in Repack-Input/")
        return

    for folder in folders:
        folder_path = os.path.join(REPACK_INPUT_DIR, folder)
        output_zip = os.path.join(REPACK_OUTPUT_DIR, f"{folder}.zip")
        zip_folder(folder_path, output_zip)

if __name__ == "__main__":
    main()