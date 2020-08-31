import click
from mixer.file_manager import VFiles
from mixer.video import video_processor


@click.group()
def cli():
    """ Video editor. """
    pass


@cli.command()
@click.argument("files_path")
def conf(files_path):
    """ Creates a conf file. """
    VFiles.create_editor_file(files_path)


@cli.command()
@click.argument("files_path")
def make(files_path):
    """ Makes the video edition. """
    video_processor(files_path)
