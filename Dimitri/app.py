import sys
import os
import yt_dlp

def download_dj_fast(file_path):
    if not os.path.exists(file_path):
        print("Error: List file not found...")
        return

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio',

        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),

        'ignoreerrors': True,

        'addmetadata': True,

        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            },
            {
                'key': 'FFmpegMetadata',
            },
        ],
    }

    print(f"{len(urls)} items (Destination: {output_dir}/)...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        print("\n🔥 Download Complete 🔥")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        download_dj_fast(sys.argv[1])
    else:
        print("Usage: python dj_download.py list.txt")

