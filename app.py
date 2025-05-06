import streamlit as st
import yt_dlp
import os

def download_video(url):
    # Get the user's Downloads folder path
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # yt-dlp download options
    ydl_opts = {
        'outtmpl': f'{downloads_dir}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            },
            {
                'key': 'FFmpegMetadata'
            }
        ],
        'postprocessor_args': [
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-strict', 'experimental'
        ]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return downloads_dir

# Streamlit UI
st.set_page_config(page_title="YouTube Downloader", page_icon="🎥")
st.title("🎥 YouTube Video Downloader")

video_url = st.text_input("Enter YouTube video URL")

if st.button("Download"):
    if video_url.strip():
        try:
            path = download_video(video_url)
            st.success(f"✅ Download complete! Saved to: `{path}`")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")