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


@cli.command()
def show():
    """ Show data stored in general conf. """
    GeneralConf.show_data_file()


@cli.command()
@click.option("--key", type=click.types.STRING,
              help="Key for configuration dictionary")
@click.option("--value", type=click.types.STRING,
              help="Value for key")
def update(key, value):
    """ Updates one key from general conf. """
    datas = GeneralConf.retrive_file()
    if value:
        datas[key] = value
        print(datas)
        GeneralConf.save_file(datas)
    GeneralConf.show_data_file()
