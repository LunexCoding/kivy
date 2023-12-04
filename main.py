from app import MyApp
from logger import logger


_log = logger.getLogger(__name__)


if __name__ == '__main__':
    try:
        MyApp().run()
    except Exception as e:
        _log.error(e)
