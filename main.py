import sys
import json
import jsonschema
import os.path
import numpy as np
import clipboard

from jsonschema import validate
import comment_creator.config as cfg

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

sys.path.append(r"./comment_creator/qt_ui")

from mainGUI import Ui_Dialog

# DEBUG
#import logging
#logging.basicConfig(level=logging.DEBUG)


class Language():
    dialect = ''
    line_len = ''
    delim_sym = ''
    delim_sym_begin = ''
    delim_sym_end = ''
    s_inter_sym = ''
    inter_sym = ''
    upper_case = ''
    multi_lines = ''
    frame = ''
    frame_on_delim = ''
    frame_ofst = ''
    centered = ''
    need_delim = ''


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
        """
        font = self.ui.txtOut.font()
        fontMetrics = QtGui.QFontMetricsF(font)
        spaceWidth = fontMetrics.width(' ')
        self.ui.txtOut.setTabStopWidth(spaceWidth*4)
        """
        # flag to enable/disable internal callback - true to disable
        self.int_clbk = False
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
        self.ui.btnMakeComment.clicked.connect(self.create_comment)
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
        if (self.ui.cbMulti.isChecked() == True and self.int_clbk == False):
            self.cfg['lastSession']['multiLines'] = 'yes'
        else:
            self.cfg['lastSession']['multiLines'] = 'no'
        if (self.ui.cbFrame.isChecked() == True\
                and self.ui.cbFrame.isEnabled() == True\
                and self.int_clbk == False):
            self.cfg['lastSession']['frame'] = 'yes'
        else:
            self.cfg['lastSession']['frame'] = 'no'
        if (self.ui.cbCentered.isChecked() == True\
                and self.ui.cbCentered.isEnabled() == True
                and self.int_clbk == False):
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
        # update the settings related to the selected dialect
        self._store_lang_cfg()
        # run the comment creator only if there is user text
        if self.ui.txtIn.toPlainText():
            self.create_comment()


    def load_settings(self):
        if os.path.exists(cfg.CONFIG_FILE_NAME):
            with open(cfg.CONFIG_FILE_NAME) as f:
                if self.extractJSON(f) == False or\
                    self.validateJSON(self.cfg) is False:
                        self.cfg = cfg.new_cfg()
                        self._update_settings()
        else:
            self.cfg = cfg.new_cfg()
            self._update_settings()
        self._ui_init()
        self._store_lang_cfg()
        
        
    def extractJSON(self, f):
        try:
            self.cfg = json.load(f)
            loaded = True
        except json.decoder.JSONDecodeError:
            self.msgOut("JSON config file error", False, True)
            loaded = False
        return loaded
            

    def validateJSON(self, json_data):
        try:
            validate(instance = json_data, schema = cfg.configSchema)
        except jsonschema.exceptions.ValidationError as err:
            self.msgOut("Can't validate configuration file!\n Error: "\
                    + str(err), False, True)
            return False
        return True 


    def _store_lang_cfg(self):
        """
        load settings related to the selected dialect
        """
        Language.dialect = self.cfg['lastSession']['dialect']
        # all editors start from column 1... so I need to remove it
        Language.line_len = self.cfg['language'][Language.dialect]\
            ['lineLength'] - 1
        # single line
        Language.delim_sym = self.cfg['language'][Language.dialect]\
        ['singleLineSettings']['delimiterSymbol']
        Language.s_inter_sym = self.cfg['language'][Language.dialect]\
        ['singleLineSettings']['interruptionSymbol']
        # multi lines
        Language.delim_sym_begin = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['delimiterSymbolBegin']
        Language.delim_sym_end = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['delimiterSymbolEnd']
        Language.inter_sym = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['interruptionSymbol']
        Language.frame_on_delim = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['frameOnDelimiter']
        # as above, the editor starts from column 1
        Language.frame_ofst = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['frameOffset'] - 1
        Language.need_delim = self.cfg['language'][Language.dialect]\
        ['multiLineSettings']['needDelimiter']
        Language.upper_case = self.cfg['lastSession']['upperCase']
        Language.multi_lines = self.cfg['lastSession']['multiLines']
        Language.frame = self.cfg['lastSession']['frame']
        Language.centered = self.cfg['lastSession']['centered']
        

    def msgOut(self, msg, comment=True, italic=False):
        if italic:
            self.ui.txtOut.setFontItalic(True)
            self.ui.txtOut.append(msg + '\n')
            self.ui.txtOut.setFontItalic(False)
        else:
            self.ui.txtOut.setText(msg + '\n')
        
        # txtOut contains a comment (not an error message)
        self.txt_is_comment = comment

        
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

        lang = self.cfg['lastSession']['dialect']
        if lang == 'Python':
            self.ui.rbPython.setChecked(True)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(False)
        
        elif lang == 'C':
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(True)
            self.ui.rbMatlab.setChecked(False)

        elif lang == 'Matlab':
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(True)

        else:
            self.ui.rbPython.setChecked(False)
            self.ui.rbC.setChecked(False)
            self.ui.rbMatlab.setChecked(False)


    def create_comment(self):
        """
        check some options and creates the comment 
        """
        txt = self.ui.txtIn.toPlainText()
        comment = self._make_comment(txt)
        # out to txtbox
        self.msgOut(comment, True, False)
        # copy to clipboard?
        if self.cfg['lastSession']['copyClipboard'] == 'yes':
            clipboard.copy(comment)

       
    def _make_comment(self, txt):
        # max comment length on a line
        if (self._check_single_line(txt) == True and Language.multi_lines == 'no'):
            comment = self._single_line(txt)
        else:
            comment = self._multi_lines(txt)
        return comment


    def _single_line(self, txt):
        """
        single line default frame + centered
        """
        # do not update the config
        self.int_clbk = True
        self.ui.cbFrame.setEnabled(False)
        self.ui.cbCentered.setEnabled(False)
        self.ui.cbFrame.setChecked(True)
        self.ui.cbCentered.setChecked(True)
        self.int_clbk = False
        spaces = Language.line_len\
                - len(Language.delim_sym)\
                - 3 * cfg.SPACE_LEN\
                - len(txt)
        side_spaces = self._side_spaces(spaces)
        inter_sym = [self._make_interruption(elem) for elem in side_spaces]
        s = Language.delim_sym + ' '\
                    + inter_sym[0] + ' '\
                    + txt\
                    + ' ' + inter_sym[1]
        if Language.upper_case == 'yes':
            s = s.upper()
        return s
        

    def _multi_lines(self, txt):
        # enable options - recall settings from config
        # do not update the config
        self.int_clbk = True
        self.ui.cbFrame.setEnabled(True)
        self.ui.cbCentered.setEnabled(True)
        self.ui.cbFrame.setChecked(self._conv(
            self.cfg['lastSession']['frame']))
        self.ui.cbCentered.setChecked(self._conv(
            self.cfg['lastSession']['centered']))
        self.int_clbk = False
        #
        max_txt_len = self._max_txt_len()
        s = self._border_comm_line('begin') + '\n'
        idx_txt = self._idx_split(txt, max_txt_len)
        for b, e in zip(idx_txt[0], idx_txt[1]):
            s = s + self._comm_line(txt[b:e]) + '\n'
        s = s + self._border_comm_line('end')
        if Language.upper_case == 'yes':
            s = s.upper()
        return s


    def _max_txt_len(self):
        txt_len = Language.line_len
        if Language.need_delim == 'yes':
            txt_len -= len(Language.delim_sym_begin)
        if (Language.frame == 'yes' and Language.centered == 'yes'):
            txt_len -= 2 * len(Language.inter_sym)\
                    + 2 * cfg.SPACE_LEN
        #if Language.centered == 'yes':
            # do not remove anything
        txt_len -= Language.frame_ofst
        return txt_len


    def _check_single_line(self, txt):
        """
        consider at least 2 interruption symbols arounnd the text
        """
        avail_txt = Language.line_len\
                - len(Language.delim_sym)\
                - 3 * cfg.SPACE_LEN\
                - 2 * len(Language.inter_sym)
        if avail_txt >= len(txt):
            return True
        else:
            return False


    def _idx_split(self, txt, line_len):
        """
        return the indexes of the splitted string for each line
        !!! PAY ATTENTION !!! since the text in the editor starts with
        coloumn 1 and not 0, it is necessary consider this offset also
        in the text line length (line_len - 1)

        """
        # array with the space position of the string
        spaces = [i for i, x in enumerate(txt) if x == ' ']
        i = 0
        idx_end = []
        idx_begin = [0]
        txt_len = len(txt)
        while (txt_len - idx_begin[-1]) > line_len:
            max_col = idx_begin[-1] + line_len
            space = np.where(np.array(spaces) <= max_col)
            t = space[0][-1]
            idx_end.append(spaces[t])
            idx_begin.append(idx_end[-1] + 1)
            i+=1
        idx_end.append(txt_len)
        return [idx_begin, idx_end]


    def _border_comm_line(self, pos):
        """
        Makes the border comment line (begin/end).
        Interruption symbol length is considered.
        """
        if pos == 'begin':
            if Language.frame_on_delim == 'yes':
                spaces = Language.line_len\
                        - len(Language.delim_sym_begin)
                s = Language.delim_sym_begin\
                        + self._make_interruption(spaces)
            else:
                spaces = Language.line_len - Language.frame_ofst
                s = Language.delim_sym_begin + '\n'\
                        + Language.frame_ofst * ' '\
                        + self._make_interruption(spaces)
        else:
            if Language.frame_on_delim == 'yes':
                spaces = Language.line_len\
                        - len(Language.delim_sym_end)\
                        - Language.frame_ofst
                s = Language.frame_ofst * ' '\
                        + self._make_interruption(spaces)\
                        + Language.delim_sym_end
            else:
                spaces = Language.line_len - Language.frame_ofst
                s = Language.frame_ofst * ' '\
                        + self._make_interruption(spaces) + '\n'\
                        + Language.delim_sym_end
        return s


    def _make_interruption(self, n):
        t = np.divmod(n, len(Language.inter_sym))
        if t[1]:
            s = t[0] * Language.inter_sym + Language.inter_sym[:t[1]]
        else:
            s = t[0] * Language.inter_sym
        return s


    def _comm_line(self, txt):
        """
        return the passed line formatted with the option selected
        """
        spaces = self._max_txt_len() - len(txt)
        [pre_spaces, post_spaces] = self._side_spaces(spaces)
        if Language.need_delim == 'yes':
            if Language.frame == 'yes':
                if Language.centered == 'yes':
                    s = Language.delim_sym_begin\
                            + Language.frame_ofst * ' '\
                            + Language.inter_sym\
                            + pre_spaces * ' ' \
                            + ' ' + txt + ' '\
                            + post_spaces * ' ' \
                            + Language.inter_sym
                else:
                    # not centered
                    s = Language.delim_sym_begin\
                            + Language.frame_ofst * ' '\
                            + Language.inter_sym\
                            + ' ' + txt + ' '\
                            + spaces * ' ' \
                            + Language.inter_sym
            else:
                # no frame
                s = Language.delim_sym_begin + ' ' + txt
        else:
            # no need to start line with delimiter
            if Language.frame == 'yes':
                if Language.centered == 'yes':
                    s = Language.frame_ofst * ' '\
                            + Language.inter_sym\
                            + pre_spaces * ' ' \
                            + ' ' + txt + ' '\
                            + post_spaces * ' ' \
                            + Language.inter_sym
                else:
                    # no centered
                    s = Language.frame_ofst * ' '\
                            + Language.inter_sym\
                            + ' ' + txt + ' '\
                            + spaces * ' ' \
                            + Language.inter_sym
            else:
                # no frame
                s = Language.frame_ofst * ' '\
                        + txt
            # centered only
            if Language.centered == 'yes':
                s = Language.frame_ofst * ' '\
                        + pre_spaces * ' ' \
                        + ' ' + txt + ' '\
                        + post_spaces * ' '
        return s


    def _side_spaces(self, spaces):
        t = np.divmod(spaces, 2)
        pre = t[0]
        post = spaces - pre
        return [pre, post]
    

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


