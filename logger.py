from kivy.utils import platform

from pathlib import Path
from Logger import Logger


_FILENAME = "log.md"
if platform == "android":
    _DIR = Path("/sdcard/emulated/0/Download")
else:
    _DIR = Path("logs")


logger = Logger()
logger.createLog(_DIR, _FILENAME)
