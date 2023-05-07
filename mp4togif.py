import pytube
from moviepy.editor import VideoFileClip
import os
import pathlib

class Youtube_mp4_to_gif:
    
    global file_path
    file_path = pathlib.Path(__file__).parent.resolve()
    
    def mp4_download_yt(self,url,is_downloaded = False,is_ready=False):
        if is_ready:
            my_video = pytube.YouTube(url,use_oauth=True, allow_oauth_cache=True)
            my_video.streams.get_highest_resolution().download()
            is_downloaded = True
            is_ready = False
        else:
            return print("Use delete_mp4 function before using this function or check that you have a variable for 'is_ready'")
        return is_downloaded,is_ready

    def mp4_to_gif(self,name):
        
        # get mp4 path
        file_list = []
        for file in os.listdir(file_path):
                # check only mp4 files
                if file.endswith('.mp4'):
                    file_list.append(file)
        # transform mp4 to gif
        videoClip = VideoFileClip(file_list[0])
        videoClip.write_gif(f"{name}.gif")
        
        is_converted = True
        
        return is_converted
    
    def delete_mp4(self,is_converted,is_ready = False):
        
        # if conversion done, get mp4 path
        if is_converted:
            delete_list = []
            # Iterate directory
            for file in os.listdir(file_path):
                # check only mp4 files
                if file.endswith('.mp4'):
                    delete_list.append(file)
        
        else:
            return is_ready
        
        # then delete mp4
        for file in delete_list:
            os.remove(file)
        
        is_ready = True
        
        return is_ready