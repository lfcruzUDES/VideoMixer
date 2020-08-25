""" General configuration class """

import os
from pathlib import Path
from mixer.utils import YAML, MFiles


class GeneralConf(object):

    base_path = os.path.join(
        Path.home(),
        ".config/videomixer"
    )
    file_name = "mixer_conf.yml"
    file_structure = {
        "intro": None,
        "cut": None,
        "end": None,
        "logo": None,
    }

    @classmethod
    def interactive_creator(self, intro, cut, end, logo):
        self.file_structure["intro"] = (
            intro if intro
            else input("Enter a INTRO stream path: ")
        )
        self.file_structure["cut"] = (
            cut if cut else
            input("Enter a CUT stream path: ")
        )
        self.file_structure["end"] = (
            end if end
            else input("Enter a END stream path: ")
        )
        self.file_structure["logo"] = (
            log if logo else
            input("Enter a LOGO stream path: ")
        )
        self.create_file()

    @classmethod
    def create_file(self):
        """ Creates a file. """
        if not MFiles.exists(self.base_path, self.file_name):
            os.makedirs(self.base_path)
        YAML.dump(os.path.join(self.base_path, self.file_name),
                  self.file_structure)
        return True

    @classmethod
    def retrive_file(self):
        """ Retrives a file. """
        if MFiles.exists(self.base_path, self.file_name):
            return YAML.load()
        else:
            return False

    @classmethod
    def save_file(self, data):
        """ Updates a file. """
        data_mix = {
            **self.file_structure,
            **data
        }
        YAML.dump(os.path.join(self.base_path, self.file_name),
                  self.file_structure)
        return True

    @classmethod
    def delete_file(self):
        """ Deletes a file. """
        os.remove(os.path.join(self.base_path, self.file_name))
        return True
