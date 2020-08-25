import click
from mixer.file_manager import GeneralConf

@click.group()
def cli():
    pass


@cli.command()
@click.option("--intro", type=click.types.STRING, 
              help="Path to the intro stream.")
@click.option("--cut", type=click.types.STRING, 
              help="Path to the cut stream.")
@click.option("--end", type=click.types.STRING, 
              help="Path to the end stream.")
@click.option("--logo", type=click.types.STRING, 
              help="Path to then logo img(PNG).")
def create(intro, cut, end, logo):
    """ Creates a new config file at ~/.config/videomixer """
    GeneralConf.interactive_creator(intro, cut, end, logo)
