import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

# Enable native ANSI color support in Windows Command Prompt
os.system('')

# Modern 24-bit RGB Palette (Vercel / OpenAI inspired)
ACCENT    = '\033[38;2;56;189;248m'   # Soft Slate Cyan (#38BDF8)
WHITE     = '\033[38;2;243;244;246m'   # Crisp Off-White (#F3F4F6)
MUTED     = '\033[38;2;107;114;128m'   # Subtle Slate Gray (#6B7280)
SUCCESS   = '\033[38;2;74;222;128m'   # Soft Emerald Green (#4ADE80)
ERROR     = '\033[38;2;248;113;113m'   # Soft Rose Red (#F87171)
BOLD      = '\033[1m'
RESET     = '\033[0m'

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
  {ACCENT}{BOLD}KHALIFA LABS{RESET} {MUTED}│ Media Extractor v1.0{RESET}
  {MUTED}─────────────────────────────────────────────────────────────{RESET}"""
    print(banner)

def get_save_directory():
    print(f"\n  {MUTED}Save Destination:{RESET}")
    print(f"   {ACCENT}1{RESET} {MUTED}•{RESET} {WHITE}Downloads Folder{RESET}")
    print(f"   {ACCENT}2{RESET} {MUTED}•{RESET} {WHITE}Desktop{RESET}")
    print(f"   {ACCENT}3{RESET} {MUTED}•{RESET} {WHITE}Browse Custom Directory...{RESET}")
    print(f"   {ACCENT}B{RESET} {MUTED}•{RESET} {MUTED}Back to main menu{RESET}")
    
    loc_choice = input(f"\n  {ACCENT}›{RESET} {WHITE}Select location [1]: {RESET}").strip().lower()

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
        print(f"  {MUTED}No folder selected. Defaulting to Downloads.{RESET}")
        return os.path.join(home, "Downloads")
    else:
        return os.path.join(home, "Downloads")

def main():
    while True:
        show_banner()
        print(f"\n  {WHITE}{BOLD}Select Action:{RESET}")
        print(f"   {ACCENT}1{RESET} {MUTED}•{RESET} {WHITE}MP3 Audio Only{RESET} {MUTED}(High Bitrate){RESET}")
        print(f"   {ACCENT}2{RESET} {MUTED}•{RESET} {WHITE}MP4 Video{RESET} {MUTED}(Custom Quality / Resolution){RESET}")
        print(f"   {ACCENT}3{RESET} {MUTED}•{RESET} {WHITE}Fast Default Video Download{RESET}")
        print(f"   {ACCENT}4{RESET} {MUTED}•{RESET} {MUTED}Exit{RESET}")
        print(f"  {MUTED}─────────────────────────────────────────────────────────────{RESET}")

        choice = input(f"\n  {ACCENT}›{RESET} {WHITE}Choice (1-4): {RESET}").strip()

        if choice == '4':
            print(f"\n  {MUTED}Exiting Khalifa Labs Engine. Goodbye!{RESET}\n")
            sys.exit()

        if choice not in ['1', '2', '3']:
            print(f"\n  {ERROR}Invalid selection.{RESET}")
            input(f"  {MUTED}Press Enter to continue...{RESET}")
            continue

        url = input(f"\n  {ACCENT}›{RESET} {WHITE}Paste URL (or 'b' to go back): {RESET}").strip()
        if url.lower() == 'b':
            continue
        if not url:
            print(f"\n  {ERROR}URL cannot be empty.{RESET}")
            input(f"  {MUTED}Press Enter to continue...{RESET}")
            continue

        save_dir = get_save_directory()
        if save_dir == "BACK":
            continue

        cmd_args = []

        if choice == '1':
            cmd_args = ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
        elif choice == '2':
            print(f"\n  {WHITE}{BOLD}Select Video Quality:{RESET}")
            print(f"   {ACCENT}1{RESET} {MUTED}•{RESET} {WHITE}Best Available{RESET} {MUTED}(4K / 2K / 1080p){RESET}")
            print(f"   {ACCENT}2{RESET} {MUTED}•{RESET} {WHITE}1080p Max{RESET}")
            print(f"   {ACCENT}3{RESET} {MUTED}•{RESET} {WHITE}720p Max{RESET}")
            print(f"   {ACCENT}4{RESET} {MUTED}•{RESET} {WHITE}480p Max{RESET}")
            q_choice = input(f"\n  {ACCENT}›{RESET} {WHITE}Select quality [1]: {RESET}").strip().lower()

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

        print(f"\n  {MUTED}─────────────────────────────────────────────────────────────{RESET}")
        print(f"  {ACCENT}⚙{RESET}  {WHITE}Output Directory:{RESET} {MUTED}{save_dir}{RESET}")
        print(f"  {ACCENT}⚙{RESET}  {WHITE}Initializing Khalifa Labs Engine...{RESET}")
        print(f"  {MUTED}─────────────────────────────────────────────────────────────{RESET}\n")

        # --- KHALIFA LABS ANTI-BOT ENGINE ---
        full_cmd = [
            "yt-dlp", 
            "--extractor-args", "youtube:player_client=ios,mweb,tv",
            "-P", save_dir
        ] + cmd_args + [url]

        try:
            subprocess.run(full_cmd, check=True)
            print(f"\n  {SUCCESS}✔ Download complete!{RESET}")
            print(f"  {MUTED}Saved to: {save_dir}{RESET}")
        except FileNotFoundError:
            print(f"\n  {ERROR}✖ Error: 'yt-dlp' is not installed or not in PATH.{RESET}")
        except Exception as e:
            print(f"\n  {ERROR}✖ An error occurred: {e}{RESET}")

        input(f"\n  {MUTED}Press Enter to return to main menu...{RESET}")

if __name__ == "__main__":
    main()
