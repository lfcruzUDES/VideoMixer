from os import path

# Base paths
# ------------------------------------------------------------
BASE_PATH = path.dirname(path.abspath(__file__))
TEMPLATE_DOC_CONF_NAME = "conf.yml"
TEMPLATE_DOC_CONF_PATH = path.join(
    BASE_PATH, "conf_template.yml"
)
VIDEO_EXTENSIONS = path.join(
    BASE_PATH, "utils/video_extensions.yml"
)

# Video paths
# ------------------------------------------------------------
RESOURCES_BASE_PATH = "/home/sit/Vídeos/Recursos/MP4"
INTRO = path.join(RESOURCES_BASE_PATH, "general.mp4")
CUT = path.join(RESOURCES_BASE_PATH, "corte.mp4")
CLOSE = path.join(RESOURCES_BASE_PATH, "cierre.mp4")
