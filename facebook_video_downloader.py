import requests


video_url = input("Enter YOur FaceBook Video Link : ")

# Make a request to the video URL
response = requests.get(video_url)

# Check if the request was successful
if response.status_code == 200:
    # Get the content of the response (the video file)
    video_content = response.content
    # Open a file in binary write mode
    with open("video.mp4", "wb") as f:
        # Write the video content to the file
        f.write(video_content)
        print("Video downloaded successfully!")
else:
    print("Failed to download video. HTTP Status Code:", response.status_code)
