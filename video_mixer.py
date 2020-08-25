#!/home/quattroc/Documentos/python/VideoMixer/env/bin/python
""" VideoMixer Menú """
import datetime
from sys import argv

from mixer import Mixer
from utils.intro import logo


class Menu(object):
    mixer = Mixer()

    def __init__(self, *args):
        try:
            if args[1] == "-conf":
                self.conf(args)
            elif args[1] == "-std":
                self.std(args)
            else:
                self.intro()
        except IndexError:
            self.intro()

    def intro(self):
        logo()
        print((
            "\nOptions:\n"
            "\t-conf\tCreates doc conf.\n\t\t-f force to recreate file.\n"
            "\t-std\tStandardizes videos (HD1080).\n"
        ))

    def conf(self, args):
        """ Creates a conf file. """
        try:
            print(args)
            force = False
            target_path = args[2]
            if args[2] == "-f":
                force = True
                target_path = args[3]
            self.mixer.create_doc_conf(target_path, force)
        except IndexError:
            self.mixer.create_doc_conf()

    def std(self, args):
        """ Standardizes videos. """
        conf = None
        try:
            conf = self.mixer.read_doc_conf(args[2])
        except IndexError:
            conf = self.mixer.read_doc_conf(args[2])
        finally:
            print(conf)

if __name__ == "__main__":
    Menu(*argv)
