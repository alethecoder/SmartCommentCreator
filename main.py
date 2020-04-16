import sys
import json
import jsonschema
import os.path
import numpy as np
import clipboard

from jsonschema import validate
import comment_creator.config as cfg

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication

sys.path.append(r"./comment_creator/qt_ui")

from mainGUI import Ui_Dialog

# DEBUG
#import logging
#logging.basicConfig(level=logging.DEBUG)



class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.initUi()
        # read/create the settings (json file)
        self.load_settings()
        #
        self.show()  

    def initUi(self):
        self.setWindowTitle("Smart comment creator")
        self.setWindowFlags(self.windowFlags() |
                QtCore.Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.size())
        self.cfg = cfg.new_cfg()
        self.txt_is_comment = False
        # hook signals to slots - link gui objects to functions
        # checkboxes
        self.ui.cbUpper.clicked.connect(self._cb_ui)
        self.ui.cbMulti.clicked.connect(self._cb_ui)
        self.ui.cbFrame.clicked.connect(self._cb_ui)
        self.ui.cbCentered.clicked.connect(self._cb_ui)
        self.ui.cbCopy.clicked.connect(self._cb_ui)
        self.ui.cbAlways.clicked.connect(self._w_on_top)
        # radiobuttons
        self.ui.rbPython.clicked.connect(self._cb_ui)
        self.ui.rbC.clicked.connect(self._cb_ui)
        self.ui.rbMatlab.clicked.connect(self._cb_ui)
        # buttons
        self.ui.btnMakeComment.clicked.connect(self._ctrl_manager)
        self.ui.btnCopy.clicked.connect(self._copy_to_clipboard)
                
                
    def _w_on_top(self):
        diag = QDialog(self)
        if self.ui.cbAlways.isChecked():
            self.cfg['lastSession']['alwaysOnTop'] = 'yes'
            diag.setWindowFlags(self.windowFlags() |
                    QtCore.Qt.WindowStaysOnTopHint)
                    
        else:
            self.cfg['lastSession']['alwaysOnTop'] = 'no'
            diag.setWindowFlags(self.windowFlags() &
                    ~QtCore.Qt.WindowStaysOnTopHint)
                
                
    def _cb_ui(self):
        """
        callback for ui objects
        """
        if self.ui.cbUpper.isChecked():
            self.cfg['lastSession']['upperCase'] = 'yes'
        else:
            self.cfg['lastSession']['upperCase'] = 'no'
        if self.ui.cbMulti.isChecked():
            self.cfg['lastSession']['multiLines'] = 'yes'
        else:
            self.cfg['lastSession']['multiLines'] = 'no'
        if self.ui.cbFrame.isChecked():
            self.cfg['lastSession']['frame'] = 'yes'
        else:
            self.cfg['lastSession']['frame'] = 'no'
        if self.ui.cbCentered.isChecked():
            self.cfg['lastSession']['centered'] = 'yes'
        else:
            self.cfg['lastSession']['centered'] = 'no'
        if self.ui.cbCopy.isChecked():
            self.cfg['lastSession']['copyClipboard'] = 'yes'
        else:
            self.cfg['lastSession']['copyClipboard'] = 'no'
        if self.ui.cbAlways.isChecked():
            self.cfg['lastSession']['alwaysOnTop'] = 'yes'
        else:
            self.cfg['lastSession']['alwaysOnTop'] = 'no'

        if self.ui.rbPython.isChecked():
            self.cfg['lastSession']['dialect'] = 'Python'
        elif self.ui.rbC.isChecked():
            self.cfg['lastSession']['dialect'] = 'C'
        elif self.ui.rbMatlab.isChecked():
            self.cfg['lastSession']['dialect'] = 'Matlab'

        if self.txt_is_comment is True:
            self._ctrl_manager()



    def load_settings(self):
        if os.path.exists(cfg.CONFIG_FILE_NAME):
            with open(cfg.CONFIG_FILE_NAME) as f:
                _cfg = json.load(f)
                if self.validateJson(_cfg):
                    self.cfg = _cfg
                else:
                    self.cfg = cfg.new_cfg()
                    self._update_settings()
        else:
            self.cfg = cfg.new_cfg()
            self._update_settings()
        self._ui_init()


    def msgOut(self, msg, comment=True, italic=False):
        if italic:
            self.ui.txtOut.setFontItalic(True)
            self.ui.txtOut.append(msg + '\n')
            self.ui.txtOut.setFontItalic(False)
        else:
            self.ui.txtOut.setText(msg + '\n')
        
        # txtOut contains a comment (not an error message)
        self.txt_is_comment = comment
        

    def validateJson(self, json_data):
        try:
            validate(instance = json_data, schema = cfg.configSchema)
        except jsonschema.exceptions.ValidationError as err:
            self.msgOut("Can't validate configuration file!\n Error: "\
                    + str(err), False, True)
            return False
        return True 
        

    def _ui_init(self):
        """
        init all the ui objects with the last session values
        """
        if self.cfg['lastSession']['upperCase'] == 'yes':
            self.ui.cbUpper.setChecked(True)
        if self.cfg['lastSession']['multiLines'] == 'yes':
            self.ui.cbMulti.setChecked(True)
        if self.cfg['lastSession']['frame'] == 'yes':
            self.ui.cbFrame.setChecked(True)
        if self.cfg['lastSession']['centered'] == 'yes':
            self.ui.cbCentered.setChecked(True)
        if self.cfg['lastSession']['copyClipboard'] == 'yes':
            self.ui.cbCopy.setChecked(True)
        if self.cfg['lastSession']['alwaysOnTop'] == 'yes':
            self.ui.cbAlways.setChecked(True)
        self._gui_init_language()


    def _gui_init_language(self):
        """
        select the language for the comment settings
        """
        l = self.cfg['lastSession']['dialect']
        if l == 'Python':
            self.ui.rbPython.setChecked(True)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(False)
        
        elif l == 'C':
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(True)
            self.ui.rbMatlab.setChecked(False)

        elif l == 'Matlab':
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(True)

        else:
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(False)


    def _ctrl_manager(self):
        """
        reads the language settings and accordingly makes the comment
        """
        c = self._make_comment()
        # out to txtbox
        self.msgOut(c)
        # copy to clipboard?
        if self.cfg['lastSession']['copyClipboard'] == 'yes':
            clipboard.copy(c)

       
    def _make_comment(self):
        l = self._get_language()
        # load lang settings
        _ll = self.cfg['language'][l]['lineLength']
        _ds = self.cfg['language'][l]['singleLineSettings']\
                ['delimiterSymbol']
        _is = self.cfg['language'][l]['singleLineSettings']\
                ['interruptionSymbol']
        # all uppercase
        _au = self.cfg['lastSession']['upperCase']
        # multilines
        _ml = self.cfg['lastSession']['multiLines']
        #frame
        _fr = self.cfg['lastSession']['frame']
        # centered
        _ce = self.cfg['lastSession']['centered']
        #
        # get the string comment
        txt = self.ui.txtIn.toPlainText()
        txt_len = len(txt)
        # first try the single line
        spaces = _ll - txt_len - len(_ds) - 3*cfg.SPACE_LEN
        # one line comment? - at least 1 space between text and delimiter
        if spaces > 1:
            # disable frame and centered
            self.ui.cbFrame.setEnabled(False)
            self.ui.cbCentered.setEnabled(False)
            self.ui.cbFrame.setChecked(True)
            self.ui.cbCentered.setChecked(True)
            # available space can be splitted (pre and post text)
            if np.mod(spaces, 2):
                pre_spaces = np.int(np.floor(spaces/2))
                post_spaces = spaces - pre_spaces
            else:
                pre_spaces = np.int(spaces/2)
                post_spaces = spaces - pre_spaces
            c = _ds + " " + pre_spaces*_is + " " + txt + " " + post_spaces*_is
        # multiline comment
        else:
            cc = 1
            # multiline comment

        if _au == 'yes':
            c = c.upper()

        if _ml == 'yes':
            c = self._build_multi_lines(_au, _fr, _ce)
            

        return c


    def _get_language(self):
        """
        return the selected dialect
        """
        return self.cfg['lastSession']['dialect'] 


    def _build_multi_lines(self, _au, _fr, _ce):
        # enable options
        self.ui.cbFrame.setEnabled(True)
        self.ui.cbCentered.setEnabled(True)
        self.ui.cbFrame.setChecked(self._conv(_fr))
        self.ui.cbCentered.setChecked(self._conv(_ce))

        return "a"




    def _conv(self, state):
        if state == 'yes':
            return True
        elif state == 'no':
            return False
        else: self.msg("Key in the configuration file is not valid!",\
                False, True)


    def _copy_to_clipboard(self):
        """
        execute the manual copy of comment text to the system clipboard
        """
        clipboard.copy(self.ui.txtOut.toPlainText())


    def closeEvent(self, e):
        """
        method run when the dialog is closed
        """
        self._update_settings()


    def _update_settings(self):
        with open(cfg.CONFIG_FILE_NAME, 'w') as json_file:
            json.dump(self.cfg, json_file, indent = 4)
            self.msgOut('Configuration file updated!', False, True)
            self.txt_is_comment = False
            
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show
    sys.exit(app.exec_())


