import ffmpeg
import os
from mixer.file_manager import VFiles, GeneralConf


def video_processor(conf_file):
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
            video = stream.video
            audio = stream.audio
            if len(data["slices"]) > 0:
                for seconds in data["slices"]:

                    video_trimed = video.filter(
                            'trim',
                            start=seconds["start"],
                            end=seconds["end"]
                            ).overlay(logo)
                    audio_trimed = audio.filter(
                            'atrim',
                            start=seconds["start"],
                            end=seconds["end"]
                            )
                    streams += [video_trimed, audio_trimed]
            else:
                streams += [video.overlay(logo), audio]
    joined = ffmpeg.concat(*streams, v=1, a=1).node
    out = ffmpeg.output(joined[0], joined[1], 'joined.mp4')
    out.run()
