import sys
import yt_dlp

def download_youtube_video(url):
    # ダウンロードの設定
    ydl_opts = {
        'format': 'best',  # 画質・音質が最良のものを選択
        'outtmpl': '%(title)s.%(ext)s',  # ファイル名を「動画タイトル.拡張子」にする
        # 'outtmpl': '/OUTPUT_PATH/%(title)s.%(ext)s',  # 出力場所の指定
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"ダウンロードを開始します: {url}")
            ydl.download([url])
            print("ダウンロードが完了しました！")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 引数がある場合はそれをURLとして使用
        video_url = sys.argv[1]
        download_youtube_video(video_url)
    else:
        # 引数がない場合は入力を求める
        print("使い方の例: python download_video.py \"https://www.youtube.com/watch?v=...\"")
        video_url = input("URLを入力してください: ")
        if video_url:
            download_youtube_video(video_url)
