import yaml


class YAML(object):
    """ Functions for yaml """

    @classmethod
    def load(self, yaml_doc):
        """ READ YAML """
        data = None
        with open(yaml_doc, "r") as f:
            data = f.read()
        return yaml.load(data, Loader=yaml.FullLoader)

    @classmethod
    def dump(self, yaml_doc, data):
        """ WRITE YAML """
        with open(yaml_doc, "w") as f:
            yaml.dump(data, f, Dumper=yaml.Dumper, allow_unicode=True)
