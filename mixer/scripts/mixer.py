import click
from mixer.file_manager import VFiles
from mixer.video import Processor


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
    video_processor = Processor(files_path)
    video_processor.make()
