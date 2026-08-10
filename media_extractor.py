import os
import subprocess
import sys

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
===============================================================
               K H A L I F A   L A B S
            Fast CLI Media Extractor v1.0
===============================================================
    """
    print(banner)

def main():
    show_banner()
    print(" Select Download Option:")
    print(" [1] Best Quality MP3 Audio Only")
    print(" [2] Best Quality MP4 Video (High Res)")
    print(" [3] Fast Default Video Download")
    print(" [4] Exit")
    print("---------------------------------------------------------------")

    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == '4':
        print("\nExiting. Thanks for using Khalifa Labs tools!")
        sys.exit()

    if choice not in ['1', '2', '3']:
        print("\n[!] Invalid selection. Please restart.")
        return

    url = input("\nPaste Video / Media URL here: ").strip()
    if not url:
        print("\n[!] URL cannot be empty.")
        return

    print("\n---------------------------------------------------------------")
    print("[*] Processing download via Khalifa Labs Engine...")
    print("---------------------------------------------------------------\n")

    if choice == '1':
        cmd = ["yt-dlp", "-x", "--audio-format", "mp3", "--audio-quality", "0", url]
    elif choice == '2':
        cmd = ["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", url]
    elif choice == '3':
        cmd = ["yt-dlp", url]

    try:
        subprocess.run(cmd, check=True)
        print("\n[✔] Download completed successfully!")
    except FileNotFoundError:
        print("\n[!] Error: 'yt-dlp' is not installed or not in your PATH.")
        print("    Run: 'winget install yt-dlp' in Command Prompt first.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
