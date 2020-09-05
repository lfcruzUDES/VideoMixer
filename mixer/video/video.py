import os
import subprocess
import datetime

import ffmpeg
from mixer.file_manager import GeneralConf, VFiles


class Processor(object):
    to_delete = []

    def get_video_scale(self, video):
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

    def time_to_seconds(self, start, end):
        start_hours, start_minutes, start_seconds = [int(s) for s in start.split(":")]
        end_hours, end_minutes, end_seconds = [int(e) for e in end.split(":")]
        start_seconds = datetime.timedelta(
            hours=start_hours, minutes=start_minutes, seconds=start_seconds
        ).total_seconds()
        end_seconds = datetime.timedelta(
            hours=end_hours, minutes=end_minutes, seconds=end_seconds
        ).total_seconds()
        return {"ss": start_seconds, "t": end_seconds - start_seconds}

    def trim(self, video, start, end, scale):
        stream = ffmpeg.input(video, **time_to_seconds(start, end))
        if scale:
            name, ext = os.path.splitext(video)
            new_video = os.path.join("/tmp", f"{name}_trimmed.mp4")
            self.to_delete.append(new_video)
            stream = ffmpeg.filter(stream, "scale", "hd1080")
            stream = ffmpeg.output(new_video)
            ffmpeg.run(stream)
            stream = ffmpeg.input(new_video)

        stream = ffmpeg.overlay()
        return [video_trimed, audio_trimed]


    def video_processor(self, conf_file):
        """ Process videos. """
        general_conf = GeneralConf.retrive_file()
        logo = ffmpeg.input(general_conf["logo"])
        datas = VFiles.get_conf(conf_file)
        streams = []

        for data in datas:
            if data["video"].startswith("_"):
                general_key = data["video"][1:]
                video_path = general_conf[general_key]
                stream = ffmpeg.input(video_path)
                streams += [stream.video, stream.audio]
            else:
                stream = ffmpeg.input(data["video"])
                scale_ok = True
                if not self.get_video_scale(data["video"]):
                    scale_ok = False
                video = stream.video
                audio = stream.audio

                if len(data["slices"]) > 0:
                    for seconds in data["slices"]:
                        streams += self.trim(video, audio,
                                             seconds["start"], seconds["end"],
                                             scale=True)
                else:
                    streams += [video.overlay(logo), audio]
        joined = ffmpeg.concat(*streams, v=1, a=1).node
        out = ffmpeg.output(joined[0], joined[1], 'joined.mp4')
        out.run()


import datetime
datetime.timedelta().total_seconds()
