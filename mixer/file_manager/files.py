""" Manage files used in video process. """

import os

from mixer import settings
from mixer.utils import YAML


class VFiles(object):
    editor_file_name = settings.LOCAL_CONF_NAME

    @classmethod
    def get_video_files(cls, video_path):
        """Get video files.

        Args:
            video_path (str): Path to the videos

        Returns:
            list: List of dicts={video: path, slices: [{"start":"00:00:00", "end": 00:00:00}]}
        """
        files = os.listdir(video_path)
        videos = []
        for _file in files:
            name, ext = os.path.splitext(_file)
            if ext.lower() in settings.VIDEO_EXT:
                videos.append({
                    "video": os.path.join(video_path, _file),
                    "slices": [],
                })
        return videos

    @classmethod
    def create_editor_file(cls, video_path):
        """Creates a new file conf.

        Args:
            video_path (str): Path to the videos.
        """
        _file = os.path.join(video_path, cls.editor_file_name)
        data = {
            "videos": cls.get_video_files(video_path),
            "images": [],
        }

        YAML.dump(os.path.join(video_path, cls.editor_file_name),
                  data)

    @classmethod
    def get_conf(cls, video_path):
        """Get data from conf file.

        Args:
            video_path (str): Path to the videos, default name
            of configuration file is conf.yml

        Returns:
            list: data of configuration file.
        """
        if not video_path:
            video_path = "."
        return YAML.load(os.path.join(
            video_path, cls.editor_file_name
            ))
