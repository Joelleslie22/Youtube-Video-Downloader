from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

def download_video(url, save_path):
    try:
        print("🔄 Creating YouTube object with pytubefix...")
        yt = YouTube(url)
        print("✅ Title:", yt.title)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        if not stream:
            print("❌ No downloadable stream found.")
            return

        print(f"⬇️ Downloading: {yt.title}")
        stream.download(output_path=save_path)
        print("✅ Download finished!")
        messagebox.showinfo("Success", f"Downloaded to:\n{save_path}")
    except Exception as e:
        print(f"❌ Error during download: {e}")
        messagebox.showerror("Download Failed", f"Error:\n{e}")

def start_download():
    url = url_input.get().strip()
    if not url:
        messagebox.showwarning("Missing URL", "Please enter a YouTube URL.")
        return

    folder = filedialog.askdirectory(title="Select Download Folder")
    if folder:
        print("📁 Folder:", folder)
        threading.Thread(target=download_video, args=(url, folder), daemon=True).start()
    else:
        print("❌ Folder selection canceled.")

app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("450x150")

tk.Label(app, text="YouTube URL:", font=("Arial", 12)).pack(pady=10)
url_input = tk.Entry(app, width=50)
url_input.pack()

tk.Button(app, text="Download", command=start_download, bg="#4CAF50", fg="white").pack(pady=20)
app.mainloop()
