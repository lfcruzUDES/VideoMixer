import os

import settings

from mixer.files_worker import FilesWorker
from mixer.video_worker import VideoWorker


class Mixer(FilesWorker, VideoWorker):
    pass

if __name__ == "__main__":
    v = Mixer(
        base_path="/home/quattroc/Vídeos/TestVideoMixer",
        ext_target="mp4"
    )
    v.create_doc_conf()
