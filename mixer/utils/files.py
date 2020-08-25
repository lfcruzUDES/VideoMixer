""" Class that have a functions for files """

import os


class MFiles(object):

    @classmethod
    def exists(self, *args):
        """ Return True if file exist. """
        return os.path.exists(os.path.join(
            *args
        ))
