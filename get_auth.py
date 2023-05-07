# Here we will just use a quick file to register our YouTube account used to download the video from the site
# I needed this step to use the whole library, it might not be the case for you

import pytube
print("Please follow the instructions that will be written in the console tab.")

# The important part that is missing in some of the other code snippets on the Internet is the use_oauth and allow_oauth_cache
my_video = pytube.YouTube("https://www.youtube.com/watch?v=C0DPdy98e4c",use_oauth=True, allow_oauth_cache=True)
my_video.streams.get_highest_resolution().download()
print("You can now use the library on your computer !")