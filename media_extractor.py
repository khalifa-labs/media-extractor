import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
==================================================================

 _  _ _  _ ____ _    _ ____ ____   _    ____ ___  ____ 
 |_/  |__| |__| |    | |___ |__|   |    |__| |__] [__  
 | \_ |  | |  | |___ | |    |  |   |___ |  | |__] ___] 

                  --- KHALIFA LABS ---
              Fast CLI Media Extractor v1.0

==================================================================
    """
    print(banner)

def get_save_directory():
    print("\n--- Select Save Location ---")
    print(" [1] Downloads Folder")
    print(" [2] Desktop")
    print(" [3] Browse Folder (Opens Windows Explorer Popup)")
    
    loc_choice = input("Select location (1-3) [Default = 1]: ").strip()

    home = os.path.expanduser("~")
    if loc_choice == '2':
        return os.path.join(home, "Desktop")
    elif loc_choice == '3':
        print("\n[*] Opening Windows folder picker window...")
        root = tk.Tk()
        root.withdraw()  # Hide main blank Tkinter window
        root.attributes('-topmost', True)  # Bring popup window to front
        selected_path = filedialog.askdirectory(title="Select Save Location")
        root.destroy()
        
        if selected_path:
            return selected_path
        print("[!] No folder selected. Defaulting to Downloads folder.")
        return os.path.join(home, "Downloads")
    else:
        return os.path.join(home, "Downloads")

def main():
    show_banner()
    print(" Select Download Option:")
    print(" [1] MP3 Audio Only")
    print(" [2] MP4 Video (Choose Resolution/Quality)")
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

    save_dir = get_save_directory()
    cmd_args = []

    if choice == '1':
        cmd_args = ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
    elif choice == '2':
        print("\n--- Select Video Quality ---")
        print(" [1] Best Available (4K / 2K / 1080p)")
        print(" [2] 1080p Max")
        print(" [3] 720p Max")
        print(" [4] 480p Max")
        q_choice = input("Select quality (1-4) [Default = 1]: ").strip()

        if q_choice == '2':
            fmt = "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]"
        elif q_choice == '3':
            fmt = "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]"
        elif q_choice == '4':
            fmt = "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480]"
        else:
            fmt = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

        cmd_args = ["-f", fmt]
    elif choice == '3':
        cmd_args = []

    print("\n---------------------------------------------------------------")
    print(f"[*] Destination: {save_dir}")
    print("[*] Processing download via Khalifa Labs Engine...")
    print("---------------------------------------------------------------\n")

    full_cmd = ["yt-dlp", "-P", save_dir] + cmd_args + [url]

    try:
        subprocess.run(full_cmd, check=True)
        print("\n[✔] Download completed successfully!")
        print(f"[✔] File saved to: {save_dir}")
    except FileNotFoundError:
        print("\n[!] Error: 'yt-dlp' is not installed or not in your PATH.")
        print("    Run: 'winget install yt-dlp' in Command Prompt first.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
