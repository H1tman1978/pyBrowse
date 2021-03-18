import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Forward Button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Refresh Button
        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_button)

        # Home Button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # Address Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setApplicationName('PyBrowse v-0.0.1')
    window = MainWindow()
    app.exec_()
