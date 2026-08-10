@echo off
title Khalifa Labs - Media Extractor
cd /d "%userprofile%\Documents"

echo ===================================================
echo             KHALIFA LABS MEDIA EXTRACTOR
echo ===================================================
echo.
echo Select an option:
echo [1] Best Quality MP3 Audio Only
echo [2] Best Quality MP4 Video
echo [3] Default Fast Video Download
echo.

set /p choice="Select an option (1-3): "
set /p url="Paste Video URL here: "

if "%choice%"=="1" (
    yt-dlp -x --audio-format mp3 --audio-quality 0 "%url%"
) else if "%choice%"=="2" (
    yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" "%url%"
) else if "%choice%"=="3" (
    yt-dlp "%url%"
) else (
    echo Invalid choice!
)

pause
