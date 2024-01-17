from pytube import Playlist, YouTube


def download_playlist(playlist_url, download_path):
  """
  Downloads all videos from a YouTube playlist to a specific folder, replacing invalid characters in filenames with underscores.

  Args:
    playlist_url: The URL of the YouTube playlist.
    download_path: The path to the folder where the videos will be downloaded.
  """
  # Create a Playlist object from the URL.
  playlist = Playlist(playlist_url)

  # Get the number of videos in the playlist.
  num_videos = len(playlist.video_urls)

  # Print a message to the user.
  print(f"Downloading {num_videos} videos from the playlist: {playlist.title}")

  # Loop through each video in the playlist and download it.
  for i, video_url in enumerate(playlist.video_urls):
    video = YouTube(video_url)

    # Get the highest resolution available.
    video_stream = video.streams.get_highest_resolution()

    # Replace invalid characters in the video title with underscores.
    safe_filename = "".join([c if c.isalnum() or c in ("_", "-") else "_" for c in video.title])

    # Download the video and save it to the specified folder with the sanitized filename.
    video_stream.download(output_path=download_path, filename=f"{i+1:02} - {safe_filename}.mp4")

    # Print a progress message to the user.
    print(f"Downloaded video {i+1}/{num_videos}: {video.title}")

# Get the playlist URL and the download path from the user.
playlist_url = input("Enter the YouTube playlist URL: ")
download_path = input("Enter the download path: ")

# Download the playlist.
download_playlist(playlist_url, download_path)

print("Done!")
