import os
import shutil

import yaml

import settings


class FilesWorker(object):
    conf = None

    def file_path(self, path, file_name):
        return os.path.join(
            path if path else ".",
            file_name
        )

    def get_videos_by_default(self, video_files_path):
        v_files = []
        ext = self.yaml_load(settings.VIDEO_EXTENSIONS)
        for f in os.listdir(video_files_path):
            name, file_ext = os.path.splitext(f)
            if file_ext.lower() in ext["v_ext"]:
                v_files.append(
                    os.path.join(
                        video_files_path,
                        f
                    )
                )
        return v_files

    def create_doc_conf(self, video_files_path=None):
        """ Creates a configuration document (YAML). """
        doc_conf = self.file_path(
            video_files_path,
            settings.TEMPLATE_DOC_CONF_NAME
        )
        data = None
        if not os.path.exists(doc_conf):
            data = self.yaml_load(settings.TEMPLATE_DOC_CONF_PATH)
            data["files"] = self.get_videos_by_default(video_files_path)
            self.yaml_dump(doc_conf, data)
        else:
            data = self.read_doc_conf(doc_conf_path=video_files_path)
        print(data)

    def read_doc_conf(self, doc_conf_path=None):
        conf_doc = self.file_path(
            doc_conf_path,
            settings.TEMPLATE_DOC_CONF_NAME
        )
        return self.yaml_load(conf_doc)

    def yaml_load(self, yaml_doc):
        data = None
        with open(yaml_doc, "r") as f:
            data = f.read()
        return yaml.load(data, Loader=yaml.FullLoader)

    def yaml_dump(self, yaml_doc, data):
        with open(yaml_doc, "w") as f:
            yaml.dump(data, f, Dumper=yaml.Dumper, allow_unicode=True)
