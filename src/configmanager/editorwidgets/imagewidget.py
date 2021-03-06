from PyQt4.QtGui import QFileDialog

from configmanager.editorwidgets.core import ConfigWidget
from configmanager.editorwidgets.uifiles.photowidget_config import Ui_Form


class ImageWidgetConfig(Ui_Form, ConfigWidget):
    description = 'Allow the user to select an image'

    def __init__(self, parent=None):
        super(ImageWidgetConfig, self).__init__(parent)
        self.setupUi(self)
        self.defaultLocationText.textChanged.connect(self.widgetchanged)
        self.locatioButton.pressed.connect(self.openfilepicker)

    def openfilepicker(self):
        startpath = self.defaultLocationText.text() or '/home'
        path = QFileDialog.getExistingDirectory(self.parent(), "Select default photo location", startpath)
        self.defaultLocationText.setText(path)

    def getconfig(self):
        location = self.defaultLocationText.text()
        return {"defaultlocation": location}

    def setconfig(self, config):
        self.defaultLocationText.setText(config.get('defaultlocation', ''))

