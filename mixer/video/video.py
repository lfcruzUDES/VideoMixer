import os
import subprocess

from mixer.file_manager import GeneralConf, VFiles


class Processor(object):
    """ Class for process de video streams. """

    default_scale = "1920x1080"
    video_cache = []

    def get_scale(self, video):
        command = ["ffprobe", "-v", "error",
                   "-select_streams", "v:0",
                   "-show_entries", "stream=width,height",
                   "-of", "csv=s=x:p=0", video]
        scale = (subprocess
                .run(command, capture_output=subprocess.PIPE)
                .stdout.decode('utf-8'))

        if scale == self.default_scale:
            return False
        return True
    
    def cut(self, video, start, end):
        command = ["ffmpeg", "-i", video, 
                   "-ss", start, "-t", end, 
                   "-async", "1" ]
    
def video_processor(conf_file):
    """ Process videos. """
    general_conf = GeneralConf.retrive_file()
    datas = VFiles.get_conf(conf_file)
    streams = []

    for data in datas:
        if data["video"].startswith("_"):
            general_key = data["video"][1:]
            print(general_key)
        else:
            command = ["ffprobe", "-v", "error", "-select_streams", "v:0",
                       "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0", data['video']]
            scale = (subprocess
                     .run(command, capture_output=subprocess.PIPE)
                     .stdout.decode('utf-8'))

            print(scale)
