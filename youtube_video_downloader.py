from pytube import YouTube
link = input("Put your youtube link here!! URL: ")
def Download(link):
  down = YouTube(link)
  down = down.streams.get_highest_resolution()
  try:
      down.download()
  except:
    print("There has been an error in downloading your youtube video")
  print("This download has completed! ")


Download(link)
