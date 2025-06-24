import os
import zipfile
import shutil
from utils import ensure_dir
from payload_dumper_gustyx import extract_payload  

def extract_payload_from_zip(zip_path, extract_to):
    print(f"📦 Finding zip: {zip_path}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        members = zip_ref.namelist()
        payload_files = [m for m in members if 'payload.bin' in m]
        if not payload_files:
            print("🚫 payload.bin Not Found in ROM zip.")
            return None
        payload_name = payload_files[0]
        zip_ref.extract(payload_name, extract_to)
        return os.path.join(extract_to, payload_name)

def handle_unpack(input_file, output_dir):
    print(f"[+] Preparing For Unpack: {input_file}")

    if input_file.endswith(".zip"):
        print("📦 Detection ZIP File, Extracting payload.bin...")
        temp_dir = "temp_payload"
        os.makedirs(temp_dir, exist_ok=True)
        payload_path = extract_payload_from_zip(input_file, temp_dir)
        if not payload_path:
            print("❌ Fail Extract payload.bin in ROM ZIP.")
            return
    elif input_file.endswith(".bin"):
        payload_path = input_file
    else:
        print("❌ Unrecognized File. Must be ZIP or payload.bin")
        return

    print(f"🔧 Unpacking payload: {payload_path}")
    ensure_dir(output_dir)
    try:
        extract_payload(payload_path, output_dir) 
        print(f"✅ Done Unpacking to: {output_dir}")
    except Exception as e:
        print(f"❌ Fail Extract payload: {e}")

    if input_file.endswith(".zip"):
        shutil.rmtree(temp_dir, ignore_errors=True)