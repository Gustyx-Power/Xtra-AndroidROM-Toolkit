from repacker import handle_repack
from unpacker import handle_unpack

def print_colored(msg, color="cyan"):
    colors = {
        "cyan": "\033[96m",
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "end": "\033[0m"
    }
    print(f"{colors.get(color, '')}{msg}{colors['end']}")

def main():
    print("╔══════════════════════════════════╗")
    print("║   📱 XTRA ANDROID ROM TOOLKIT    ║")
    print("║          By Gustyx-Power         ║")
    print("╚══════════════════════════════════╝")
    print("This tool can only Unpack and Repack payload.bin in Custom ROM or OEM ROM")
    print("1. 📦 Unpack payload.bin in ROM")
    print("2. 🛠️  Repack Image")
    mode = input(">> Choose Mode (1/2): ")

    if mode == "1":
        print("Format Text :")
        print("Enter the path to the ZIP file or payload.bin:Unpack-Rom/Pixel-OS.zip or Unpack-Rom/payload.bin")
        print("Enter the unpack output folder path:Unpack-Output")
        input_file = input("Enter the path to the ZIP file or payload.bin: ").strip()
        output_dir = input("Enter the unpack output folder path: ").strip()
        handle_unpack(input_file, output_dir)

    elif mode == "2":
        print("Format Text :")
        print("Enter the path of the folder containing .img:Repack-Input")
        print("Enter the output name payload.bin:Repack-Output/payload.bin")
        input_dir = input("Enter the path of the folder containing .img: ").strip()
        output_file = input("Enter the output name payload.bin: ").strip()
        handle_repack(input_dir, output_file)

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()