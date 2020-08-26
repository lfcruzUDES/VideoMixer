""" Manage files used in video process. """

import os
from mixer.utils import v_ext, YAML

class VFiles(object):
    editor_file_name = "conf.yml"

    @classmethod
    def get_video_files(self, video_path):
        files = os.listdir(video_path)
        videos = []
        for _file in files:
            name, ext = os.path.splitext(_file)
            if ext in v_ext:
                videos.append({
                    "video": os.path.join(video_path, _file),
                    "slices": [],
                })
        return videos

    @classmethod
    def create_editor_file(self, video_path):
        _file = os.path.join(video_path, self.editor_file_name)
        data = self.get_video_files(video_path)
        YAML.dump(os.path.join(video_path, self.editor_file_name),
                  data)
