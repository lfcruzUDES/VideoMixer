import ffmpeg
import os
from mixer.utils import YAML


def video_processor(conf_file):
    data = YAML.load(conf_file)
