import os

import settings

from .files_worker import FilesWorker


class Mixer(FilesWorker):
    video_ext = [""]
    videos = []

    def standardize(self):
        for video in self.videos:
            if not video.startswith("0X0_"):
                input_v = os.path.join(self.base_path, video)
                name, ext = os.path.splitext(video)
                output = os.path.join(self.base_path, f"0X0_{name}")
                v = os.system(f"ffmpeg -y -i {input_v} -s hd1080 {output}.mp4")
                if v:
                    print(f"Error: There are a problem in video {video}")
                    print(output)
                    break

    def encode(self):
        pass


if __name__ == "__main__":
    v = Mixer(
        base_path="/home/quattroc/Vídeos/TestVideoMixer",
        ext_target="mp4"
    )
    v.create_doc_conf()
