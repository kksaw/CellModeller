# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CellModeller\GUI\PyGLGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CellModeller(object):
    def setupUi(self, CellModeller):
        CellModeller.setObjectName("CellModeller")
        CellModeller.resize(954, 711)   #kk: this is the window size
        self.centralwidget = QtWidgets.QWidget(CellModeller)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 0))   #kk: this is the grey thing beside the black thing
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.PyGLCMViewer = PyGLCMViewer(self.centralwidget)
        self.PyGLCMViewer.setObjectName("PyGLCMViewer")
        self.gridLayout.addWidget(self.PyGLCMViewer, 0, 2, 1, 1)
        self.PyGLCMViewer.raise_()
        self.label.raise_()
        self.line.raise_()
        CellModeller.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CellModeller)
        self.statusbar.setObjectName("statusbar")
        CellModeller.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(CellModeller)
        self.toolBar.setObjectName("toolBar")
        CellModeller.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRun = QtWidgets.QAction(CellModeller)
        self.actionRun.setCheckable(True)
        self.actionRun.setObjectName("actionRun")
        self.actionReset = QtWidgets.QAction(CellModeller)
        self.actionReset.setObjectName("actionReset")
        self.actionLoad = QtWidgets.QAction(CellModeller)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoadPickle = QtWidgets.QAction(CellModeller)
        self.actionLoadPickle.setObjectName("actionLoadPickle")
        self.actionSave_Pickles = QtWidgets.QAction(CellModeller)
        self.actionSave_Pickles.setCheckable(True)
        self.actionSave_Pickles.setObjectName("actionSave_Pickles")
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionLoadPickle)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave_Pickles)

        self.retranslateUi(CellModeller)
        self.PyGLCMViewer.selectedCell['QString'].connect(self.label.setText)
        self.actionRun.toggled['bool'].connect(self.PyGLCMViewer.toggleRun)
        self.actionLoad.triggered.connect(self.PyGLCMViewer.load)
        self.actionReset.triggered.connect(self.PyGLCMViewer.reset)
        self.actionLoadPickle.triggered.connect(self.PyGLCMViewer.loadPickle)
        self.actionSave_Pickles.toggled['bool'].connect(self.PyGLCMViewer.toggleSavePickles)
        #self.PyGLCMViewer.setSavePicklesToggle['bool'].connect(self.actionSave_Pickles.setChecked)  #kk: commented this out (does not automatically save)
        QtCore.QMetaObject.connectSlotsByName(CellModeller)

    def retranslateUi(self, CellModeller):
        _translate = QtCore.QCoreApplication.translate
        CellModeller.setWindowTitle(_translate("CellModeller", "CellModeller"))
        self.PyGLCMViewer.setWhatsThis(_translate("CellModeller", "CellModeller viewer derived from PyQGLViewertime."))
        self.toolBar.setWindowTitle(_translate("CellModeller", "toolBar"))
        self.actionRun.setText(_translate("CellModeller", "Run"))
        self.actionRun.setToolTip(_translate("CellModeller", "Run"))
        self.actionRun.setShortcut(_translate("CellModeller", "Space"))
        self.actionReset.setText(_translate("CellModeller", "Reset Simulation"))
        self.actionReset.setToolTip(_translate("CellModeller", "Reset the simulation"))
        self.actionReset.setShortcut(_translate("CellModeller", "Ctrl+R"))
        self.actionLoad.setText(_translate("CellModeller", "Load Model"))
        self.actionLoad.setToolTip(_translate("CellModeller", "Load python module"))
        self.actionLoad.setShortcut(_translate("CellModeller", "Ctrl+O"))
        self.actionLoadPickle.setText(_translate("CellModeller", "Load Pickle"))
        self.actionLoadPickle.setToolTip(_translate("CellModeller", "Load saved pickle file"))
        self.actionLoadPickle.setShortcut(_translate("CellModeller", "Ctrl+L"))
        self.actionSave_Pickles.setText(_translate("CellModeller", "Save Pickles"))
        self.actionSave_Pickles.setToolTip(_translate("CellModeller", "Save simulations data"))
        self.actionSave_Pickles.setShortcut(_translate("CellModeller", "Ctrl+S"))

from CellModeller.GUI.PyGLCMViewer import PyGLCMViewer

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CellModeller = QtWidgets.QMainWindow()
    ui = Ui_CellModeller()
    ui.setupUi(CellModeller)
    CellModeller.show()
    sys.exit(app.exec_())

