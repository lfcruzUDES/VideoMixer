import os


class FFmpeg(object):

    @classmethod
    def slice_video(self, video, start, end):
        """Slices a video.

        Args:
            video_path (str): path to video with the vide name. 
            start (string): Time in format 00:00:00.
            end (string): Time in format 00:00:00.
        """        
        
        name, ext = os.path.splitext(video)
        slices_video_name = f"/tmp/sl_{name}.mp4"
        
        result = os.system(f"ffmpeg -y -i {video} -ss {start} -t {end} {slices_video_name}.mp4")
        if not result:
            return slices_video_name
        return False