import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

# Enable native ANSI color support in Windows Command Prompt
os.system('')

# Terminal Color Codes
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{CYAN}{BOLD}
==================================================================

 _  _ _  _ ____ _    _ ____ ____   _    ____ ___  ____ 
 |_/  |__| |__| |    | |___ |__|   |    |__| |__] [__  
 | \_ |  | |  | |___ | |    |  |   |___ |  | |__] ___] 

                  --- KHALIFA LABS ---
              Fast CLI Media Extractor v1.0

=================================================================={RESET}
    """
    print(banner)

def get_save_directory():
    print(f"\n{CYAN}--- Select Save Location ---{RESET}")
    print(" [1] Downloads Folder")
    print(" [2] Desktop")
    print(" [3] Browse Folder")
    print(" [B] Back to Main Menu")
    
    loc_choice = input(f"\n{YELLOW}Select location (1-3, or B) [Default = 1]: {RESET}").strip().lower()

    if loc_choice == 'b':
        return "BACK"

    home = os.path.expanduser("~")
    if loc_choice == '2':
        return os.path.join(home, "Desktop")
    elif loc_choice == '3':
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        selected_path = filedialog.askdirectory(title="Select Save Location")
        root.destroy()
        
        if selected_path:
            return selected_path
        print(f"{YELLOW}[!] No folder selected. Defaulting to Downloads folder.{RESET}")
        return os.path.join(home, "Downloads")
    else:
        return os.path.join(home, "Downloads")

def main():
    while True:
        show_banner()
        print(f"{BOLD} Select Download Option:{RESET}")
        print(" [1] MP3 Audio Only")
        print(" [2] MP4 Video (Choose Resolution/Quality)")
        print(" [3] Fast Default Video Download")
        print(" [4] Exit")
        print("---------------------------------------------------------------")

        choice = input(f"\n{YELLOW}Enter choice (1-4): {RESET}").strip()

        if choice == '4':
            print(f"\n{CYAN}Exiting. Thanks for using Khalifa Labs tools!{RESET}")
            sys.exit()

        if choice not in ['1', '2', '3']:
            print(f"\n{RED}[!] Invalid selection.{RESET}")
            input("Press Enter to continue...")
            continue

        url = input(f"\n{YELLOW}Paste Video / Media URL here (or type 'b' to go back): {RESET}").strip()
        if url.lower() == 'b':
            continue
        if not url:
            print(f"\n{RED}[!] URL cannot be empty.{RESET}")
            input("Press Enter to continue...")
            continue

        save_dir = get_save_directory()
        if save_dir == "BACK":
            continue

        cmd_args = []

        if choice == '1':
            cmd_args = ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
        elif choice == '2':
            print(f"\n{CYAN}--- Select Video Quality ---{RESET}")
            print(" [1] Best Available (4K / 2K / 1080p)")
            print(" [2] 1080p Max")
            print(" [3] 720p Max")
            print(" [4] 480p Max")
            print(" [B] Back to Main Menu")
            q_choice = input(f"\n{YELLOW}Select quality (1-4, or B) [Default = 1]: {RESET}").strip().lower()

            if q_choice == 'b':
                continue

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
        print(f"{CYAN}[*] Destination: {save_dir}{RESET}")
        print(f"{CYAN}[*] Processing download via Khalifa Labs Engine...{RESET}")
        print("---------------------------------------------------------------\n")

        full_cmd = ["yt-dlp", "-P", save_dir] + cmd_args + [url]

        try:
            subprocess.run(full_cmd, check=True)
            print(f"\n{GREEN}[✔] Download completed successfully!{RESET}")
            print(f"{GREEN}[✔] File saved to: {save_dir}{RESET}")
        except FileNotFoundError:
            print(f"\n{RED}[!] Error: 'yt-dlp' is not installed or not in your PATH.{RESET}")
            print("    Run: 'winget install yt-dlp' in Command Prompt first.")
        except Exception as e:
            print(f"\n{RED}[!] An error occurred: {e}{RESET}")

        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
