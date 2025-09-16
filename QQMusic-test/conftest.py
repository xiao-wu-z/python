
import pytest
from pywinauto import Application

from Utils.logUtils import Logger


class QQmusicApp :

    def __init__(self):
        self.appPath = "D:\资料\gui-auto-test-master\工具\qqmusic\qqmusic\QQMusic.exe"
        self.app = None
        self.win = None
        self.logger = Logger.getLog()

    # 启动程序
    def launch(self):
        try:
            # self.app = Application(backend="uia").start(self.appPath)
            self.app = Application(backend="uia").connect(process=130060)
            self.win = self.app.window(title = "QQMusic")
            self.win.wait("visible")
            # self.win.print_control_identifiers()
            self.logger.info("应用程序启动成功!")
        except Exception as e:
            self.logger.error(f"应用程序启动失败:{e}")

    def close(self):
        self.win.close()


@pytest.fixture(scope="session")
def QQMusic_app():
    QQmusic = QQmusicApp()

    QQmusic.launch()
    yield QQmusic
    # QQmusic.close()
