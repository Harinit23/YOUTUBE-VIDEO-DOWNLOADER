from pytube import YouTube

def download_video(url, output_path='downloads'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        print("Downloading:", video.title)
        video.download(output_path)
        print("Download complete!")
    except Exception as e:
        print("Error:", str(e))

def download_audio(url, output_path='downloads'):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        print("Downloading audio:", audio.title)
        audio.download(output_path)
        print("Audio download complete!")
    except Exception as e:
        print("Error:", str(e))

def main():
    print("YouTube Downloader")

    while True:
        print("\nChoose an option:")
        print("1. Download Video")
        print("2. Download Audio")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            url = input("Enter YouTube video URL: ")
            download_video(url)
        elif choice == '2':
            url = input("Enter YouTube video URL: ")
            download_audio(url)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()