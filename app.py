import streamlit as st
import yt_dlp
import os

def download_video(url):
    output_path = "%(title)s.%(ext)s"
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': output_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    
    return filename  # Full path to downloaded file

# Streamlit UI
st.set_page_config(page_title="YouTube Downloader", page_icon="📥")
st.title("🎬 YouTube Video Downloader")

video_url = st.text_input("Enter YouTube video URL")

if st.button("Download"):
    if video_url.strip():
        try:
            filepath = download_video(video_url)
            with open(filepath, "rb") as f:
                st.success("✅ Download ready!")
                st.download_button(
                    label="📥 Click here to save video",
                    data=f,
                    file_name=os.path.basename(filepath),
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL.")