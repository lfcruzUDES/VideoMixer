import click
from mixer.file_manager import VFiles


@click.group()
def cli():
    """ Video editor. """
    pass


@cli.command()
@click.argument("files_path")
def conf(files_path):
   """ Creates a conf file. """
   VFiles.create_editor_file(files_path)
