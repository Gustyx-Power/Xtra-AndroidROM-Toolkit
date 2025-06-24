
# ⚙️ Xtra Android ROM Toolkit

> 📦 Cross-Platform Payload.bin Unpacker & Repacker  
> ✨ Supports **Android Termux**, **Linux**, and **Windows**

![Python](https://img.shields.io/badge/Python-3.10+%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-informational)
![License](https://img.shields.io/github/license/Gustyx-Power/Xtra-AndroidROM-Toolkit)
![Stars](https://img.shields.io/github/stars/Gustyx-Power/Xtra-AndroidROM-Toolkit?style=social)

---

## 🧰 Supported Platforms

| Platform | Logo | Notes |
|---------|------|-------|
| **Termux** | <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Termux.svg" width="64"/> | CLI-based Android environment |
| **Android** | <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Android_logo_2023_%28stacked%29.svg" width="128"/> | Accessed via Termux |
| **Linux** | <img src="https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png" width="64"/> | Full bash-based support |
| **Windows** | <img src="https://upload.wikimedia.org/wikipedia/commons/e/e6/Windows_11_logo.svg" width="128"/> | Requires Python and PATH setup |

---

## 📥 Installation

### 📌 Step 1: Clone

```bash
git clone https://github.com/yourusername/rom-toolkit-python.git
cd Xtra-AndroidROM-Toolkit
```

### ⚙️ Step 2: Install Dependencies

#### 🧰 Termux

```bash
sh install_deps_termux.sh
```

#### 🐧 Linux

```bash
sh install_deps_linux.sh
```

#### 🪟 Windows

> 💡 Requirements:
> - Python 3.10+
> - Python must be in your system `PATH`

```bat
install_deps_windows.bat
```

Or manually:

```bat
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 rom_toolkit.py
```

🎮 Interactive Menu:
```
╔══════════════════════════════════╗
║     📱  XTRA ANDROID ROM TOOLKIT       ║
╚══════════════════════════════════╝
1. 📦 Unpack ROM
2. 🛠️  Repack Image
>> Choose mode (1/2):
```

---

## 🗂 Folder Structure

```
rom-toolkit-python/
├── rom_toolkit.py               # CLI launcher
├── unpacker.py                  # Unpack logic
├── repacker.py                  # Repack logic
├── payload_dumper_gustyx.py     # Custom wrapper
├── img2payload_gustyx.py        # Repack to payload.bin
├── payload_dumper/              # Payload extractor (forked)
├── install_deps_termux.sh       # Termux installer
├── install_deps_linux.sh        # Linux installer
├── install_deps_windows.bat     # Windows installer
├── requirements.txt             # Python dependencies
```

---

## 🧪 Requirements

Inside `requirements.txt`:

```txt
protobuf>=5.27.3
six>=1.16.0
bsdiff4>=1.1.5
brotli>=1.1.0
zstandard>=0.23.0
fsspec>=2023.0.0
requests>=2.28.0
aiohttp>=3.8.0
```

---

## 🙌 Credits

- 🔧 **payload_dumper** by [Vasya Lyashenko (vasi) Russian🇷🇺](https://github.com/vm03/payload_dumper.git)
- 🛠️ Modded by **Gusti Aditya Muzaky (Gustyx-Power) Indonesia🇮🇩**

---

## 📜 License

This project is licensed under the **MIT License**.  
See [`LICENSE`](./LICENSE) for details.

---

## ❤️ Final Note

> Made with 💡 & 💻 to help Android tinkerers like **Gustyx-Power**.
