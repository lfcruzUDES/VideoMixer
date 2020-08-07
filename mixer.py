#!/home/sit/Documentos/python/VideoMixer/env/bin/python

import settings
import os
from sys import argv

class Mixer(object):

    def __init__(self, video_path, ext):
        self.video_path = video_path
        self.ext = ext

    def join(self):
        file_names = sorted(os.listdir(self.video_path))
        videos_list = os.path.join(self.video_path, ".videos.txt")
        result = os.path.join(self.video_path, f"video_joined.{self.ext}")
        
        with open(videos_list, "w") as v:
            v.write("")
        with open(videos_list, "a") as v:
            # v.write(f"file '{settings.intro}'\n")
            for name in file_names:
                if not ".txt" in name and f".{self.ext}" in name:
                    v.write(f"file './{name}'\n")
            # v.write(f"file '{settings.close}'\n")
        os.system(
            f"ffmpeg -f concat -safe 0 -i {videos_list} -c copy {result}"
        )
        os.remove(videos_list)
        

if __name__ == "__main__":
    try:
        m = Mixer(argv[1], argv[2])
        m.join()
    except IndexError:
        print("Enter a video path and file extention.")
