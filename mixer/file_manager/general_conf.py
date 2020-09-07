""" General configuration class """

import os
from pathlib import Path

from mixer import settings
from mixer.utils import YAML, MFiles


class GeneralConf(object):

    base_path = os.path.join(
        Path.home(),
        settings.GENERAL_CONF_DIR
    )
    file_name = settings.GENERAL_CONF_NAME
    file_structure = {
        "intro": None,
        "cut": None,
        "end": None,
        "logo": None,
    }

    @classmethod
    def interactive_creator(cls, intro, cut, end, logo):
        cls.file_structure["intro"] = (
            intro if intro
            else input("Enter a INTRO stream path: ")
        )
        cls.file_structure["cut"] = (
            cut if cut else
            input("Enter a CUT stream path: ")
        )
        cls.file_structure["end"] = (
            end if end
            else input("Enter a END stream path: ")
        )
        cls.file_structure["logo"] = (
            log if logo else
            input("Enter a LOGO stream path: ")
        )
        cls.create_file()

    @classmethod
    def create_file(cls):
        """ Creates a file. """
        if not MFiles.exists(cls.base_path, cls.file_name):
            os.makedirs(cls.base_path)
        YAML.dump(os.path.join(cls.base_path, cls.file_name),
                  cls.file_structure)
        return True

    @classmethod
    def retrive_file(cls):
        """ Retrives a file. """
        _file = os.path.join(cls.base_path, cls.file_name)
        if MFiles.exists(cls.base_path, cls.file_name):
            return YAML.load(_file)
        else:
            return False

    @classmethod
    def show_data_file(cls):
        """ Show data from conf file. """
        if MFiles.exists(cls.base_path, cls.file_name):
            data = cls.retrive_file()
            for k, v in data.items():
                print(f"{k}\t{v}")
        else:
            print("No data.")

    @classmethod
    def save_file(cls, data):
        """ Updates a file. """
        data_mix = {
            **cls.file_structure,
            **data
        }
        YAML.dump(os.path.join(cls.base_path, cls.file_name),
                  data_mix)
        return True

    @classmethod
    def update(cls, param):
        datas = cls.retrive_file()
        print(datas)

    @classmethod
    def delete_file(cls):
        """ Deletes a file. """
        os.remove(os.path.join(cls.base_path, cls.file_name))
        return True
