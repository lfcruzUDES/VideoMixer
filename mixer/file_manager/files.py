""" Manage files used in video process. """

import os
from mixer.utils import v_ext, YAML


class VFiles(object):
    editor_file_name = "conf.yml"

    @classmethod
    def get_video_files(cls, video_path):
        """ Obtains video files. """
        files = os.listdir(video_path)
        videos = []
        for _file in files:
            name, ext = os.path.splitext(_file)
            if ext.lower() in v_ext:
                videos.append({
                    "video": os.path.join(video_path, _file),
                    "slices": [],
                })
        return videos

    @classmethod
    def create_editor_file(cls, video_path):
        """ Create file to edit videos. """
        _file = os.path.join(video_path, cls.editor_file_name)
        data = cls.get_video_files(video_path)
        YAML.dump(os.path.join(video_path, cls.editor_file_name),
                  data)

    @classmethod
    def get_conf(cls, video_path):
        if not video_path:
            video_path = "."
        return YAML.load(os.path.join(
            video_path, cls.editor_file_name
            ))
