# Made by Enomiis on Github
# note that you have to use the get_auth.py file before you can use the library, I don't know why but now YouTube requires an authentification before any download.

from mp4togif import Youtube_mp4_to_gif
# state of current conversion variables
state_download = False
state_conversion = False
state_ready = True
# creation of an object of Youtube_mp4_to_gif class
youtube = Youtube_mp4_to_gif()
# downloading youtube video by link, mp4_download_yt(url,is_downloaded,is_ready)
state_download,state_ready = youtube.mp4_download_yt("https://www.youtube.com/watch?v=IdK6_SAycS4",state_download,state_ready)
# converting it to GIF, mp4_to_gif(name)
state_conversion = youtube.mp4_to_gif("Non mario")
# deleting mp4 video to avoid taking space delete_mp4(is_converted)
# !!! This function will delete every .mp4 file in the folder so be careful where you are using it !
state_ready = youtube.delete_mp4(state_conversion)