# img2payload_gustyx.py
# Created by GustyxPower | XMS

import os
import struct
from update_metadata_pb2 import DeltaArchiveManifest, InstallOperation, PartitionUpdate

def create_payload_image(img_dir, output_path):
    manifest = DeltaArchiveManifest()

    for img_file in os.listdir(img_dir):
        if not img_file.endswith(".img"):
            continue

        part = manifest.partitions.add()
        part.partition_name = img_file.replace(".img", "")
        part.new_partition_info.size = os.path.getsize(os.path.join(img_dir, img_file))

        op = InstallOperation()
        op.type = InstallOperation.REPLACE
        with open(os.path.join(img_dir, img_file), "rb") as f:
            chunk = f.read()
            op.data_offset = 0  # temporary, will be rewritten
            op.data_length = len(chunk)
            part.operations.extend([op])

    manifest_bytes = manifest.SerializeToString()

    with open(output_path, "wb") as out:
        out.write(b"CrAU")
        out.write(struct.pack("<Q", len(manifest_bytes)))     # manifest_len
        out.write(struct.pack("<Q", 0))                        # metadata_signature_len
        out.write(manifest_bytes)

        for part in manifest.partitions:
            img_path = os.path.join(img_dir, f"{part.partition_name}.img")
            with open(img_path, "rb") as f:
                out.write(f.read())

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 img2payload_gustyx.py <img_dir> <output_payload.bin>")
        exit(1)

    create_fake_payload(sys.argv[1], sys.argv[2])