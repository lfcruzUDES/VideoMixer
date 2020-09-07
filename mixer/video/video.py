import datetime
import os
import subprocess

from uuid import uuid4

import ffmpeg

from mixer import settings
from mixer.file_manager import GeneralConf, VFiles


class Processor(object):
    """ Class that process de instructions in the conf.yml """

    files_in_temp_dir = []

    def __init__(self, work_directory):
        self.work_directory = work_directory
        self.local_conf = VFiles.get_conf(work_directory)
        self.general_conf = GeneralConf.retrive_file()
        self.logo = ffmpeg.input(self.general_conf["logo"])

    def delete_temporary_files(self):
        """ Delete temporary files. """
        for f in self.files_in_temp_dir:
            os.remove(f)

    def get_video_scale(self, video):
        """ Get the video scale. """
        command = ["ffprobe", "-v", "error",
                   "-select_streams", "v:0",
                   "-show_entries", "stream=width,height",
                   "-of", "csv=s=x:p=0", video]
        scale = (subprocess
                 .run(command, stdout=subprocess.PIPE)
                 .stdout.decode('utf-8'))

        if scale == settings.VIDEO_SCALE_SIZE:
            return False
        return True

    def time_to_seconds(self, start, end):
        """ Transform 00:00:00 notation to seconds, where end is the difference
        between start and end seconds. """
        start_hours, start_minutes, start_seconds = [
            int(s) for s in start.split(":")]
        end_hours, end_minutes, end_seconds = [int(e) for e in end.split(":")]
        start_seconds = datetime.timedelta(
            hours=start_hours, minutes=start_minutes, seconds=start_seconds
        ).total_seconds()
        end_seconds = datetime.timedelta(
            hours=end_hours, minutes=end_minutes, seconds=end_seconds
        ).total_seconds()
        return {"ss": start_seconds, "t": end_seconds - start_seconds}

    def scale(self, video):
        """ Scales the video to hd1080. """
        new_video = os.path.join(
            settings.TMP, f"{uuid4().hex}.mp4"
        )
        self.files_in_temp_dir.append(new_video)
        command = (f"ffmpeg -y -i {video} -s {settings.VIDEO_SCALE} {new_video}")
        os.system(command)
        return ffmpeg.input(new_video)

    def trim(self, video, start, end):
        """ Trim the video. """
        time = self.time_to_seconds(start, end)
        name, ext = os.path.splitext(video)
        new_video = os.path.join(
            settings.TMP, f"{uuid4().hex}.mp4"
        )
        self.files_in_temp_dir.append(new_video)
        command = (f"ffmpeg -y -i {video} -ss {time['ss']} -t {time['t']} "
                   f"-s {settings.VIDEO_SCALE} "
                   f"{new_video}")
        os.system(command)
        return ffmpeg.input(new_video)


    def make(self):
        """ Process videos, following the instructions in conf file. """
        streams = []

        for data in self.local_conf["videos"]:
            if data["video"].startswith("_"):
                general_key = data["video"][1:]
                video_path = self.general_conf[general_key]
                stream = ffmpeg.input(video_path)
                if not self.get_video_scale(data["video"]):
                    stream = self.scale(data["video"])
                streams += [stream.video, stream.audio]
            else:
                stream = ffmpeg.input(data["video"])

                if len(data["slices"]) > 0:
                    for seconds in data["slices"]:
                        stream_trimmed = self.trim(
                            data["video"],
                            seconds["start"],
                            seconds["end"],
                        )
                        streams += [stream_trimmed.video.overlay(self.logo), stream_trimmed.audio]
                else:
                    if not self.get_video_scale(data["video"]):
                        stream = self.scale(data["video"])
                    streams += [stream.video.overlay(self.logo), stream.audio]
        joined = ffmpeg.concat(*streams, v=1, a=1, unsafe=True).node
        out = ffmpeg.output(joined[0], joined[1], 'joined.mp4')
        out.run()
        self.delete_temporary_files()
