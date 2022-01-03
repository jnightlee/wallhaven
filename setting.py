# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 483)
        MainWindow.setMaximumSize(QtCore.QSize(393, 483))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(393, 483))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("background-color:rgb(249, 249, 249)")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.img_set_table = QtWidgets.QWidget()
        self.img_set_table.setObjectName("img_set_table")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.img_set_table)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.purity_box = QtWidgets.QGroupBox(self.img_set_table)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.purity_box.setFont(font)
        self.purity_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.purity_box.setObjectName("purity_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.purity_box)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, 9, -1, -1)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.purity_sfw = QtWidgets.QCheckBox(self.purity_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.purity_sfw.setFont(font)
        self.purity_sfw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.purity_sfw.setChecked(False)
        self.purity_sfw.setObjectName("purity_sfw")
        self.horizontalLayout.addWidget(self.purity_sfw)
        self.purity_sketchy = QtWidgets.QCheckBox(self.purity_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.purity_sketchy.setFont(font)
        self.purity_sketchy.setFocusPolicy(QtCore.Qt.NoFocus)
        self.purity_sketchy.setObjectName("purity_sketchy")
        self.horizontalLayout.addWidget(self.purity_sketchy)
        self.gridLayout_5.addWidget(self.purity_box, 0, 0, 1, 1)
        self.category_box = QtWidgets.QGroupBox(self.img_set_table)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category_box.setFont(font)
        self.category_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.category_box.setObjectName("category_box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.category_box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cate_general = QtWidgets.QCheckBox(self.category_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cate_general.setFont(font)
        self.cate_general.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cate_general.setChecked(False)
        self.cate_general.setObjectName("cate_general")
        self.horizontalLayout_2.addWidget(self.cate_general)
        self.cate_anime = QtWidgets.QCheckBox(self.category_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cate_anime.setFont(font)
        self.cate_anime.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cate_anime.setChecked(False)
        self.cate_anime.setObjectName("cate_anime")
        self.horizontalLayout_2.addWidget(self.cate_anime)
        self.cate_people = QtWidgets.QCheckBox(self.category_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.cate_people.setFont(font)
        self.cate_people.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cate_people.setObjectName("cate_people")
        self.horizontalLayout_2.addWidget(self.cate_people)
        self.gridLayout_5.addWidget(self.category_box, 1, 0, 1, 1)
        self.sorting_box = QtWidgets.QGroupBox(self.img_set_table)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_box.setFont(font)
        self.sorting_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_box.setObjectName("sorting_box")
        self.gridLayout = QtWidgets.QGridLayout(self.sorting_box)
        self.gridLayout.setObjectName("gridLayout")
        self.sorting_views = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_views.setFont(font)
        self.sorting_views.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_views.setObjectName("sorting_views")
        self.gridLayout.addWidget(self.sorting_views, 0, 1, 1, 1)
        self.sorting_favorites = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_favorites.setFont(font)
        self.sorting_favorites.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_favorites.setObjectName("sorting_favorites")
        self.gridLayout.addWidget(self.sorting_favorites, 1, 1, 1, 1)
        self.sorting_hot = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_hot.setFont(font)
        self.sorting_hot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_hot.setObjectName("sorting_hot")
        self.gridLayout.addWidget(self.sorting_hot, 1, 2, 1, 1)
        self.sorting_toplist = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_toplist.setFont(font)
        self.sorting_toplist.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_toplist.setChecked(True)
        self.sorting_toplist.setObjectName("sorting_toplist")
        self.gridLayout.addWidget(self.sorting_toplist, 2, 0, 1, 1)
        self.top_range_box = QtWidgets.QComboBox(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.top_range_box.setFont(font)
        self.top_range_box.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.top_range_box.setStyleSheet("QComboBox {\n"
"     border:1px solid gray;\n"
"     border-radius: 3px;\n"
"     padding:1px 2px 1px 2px;\n"
"     min-width:9em;\n"
"}\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin:padding;\n"
"     subcontrol- position:top right;\n"
"     width:20px;\n"
"     border-left-width:1px;\n"
"     border-left-color:darkgray;\n"
"     border-left-style:solid;  /* just a single line */\n"
"     border-top-right-radius:3px;  /* same radius as the QComboBox */\n"
"     border-bottom-right-radius:3px;\n"
"}\n"
" \n"
"QComboBox::down-arrow {\n"
"     image:url(icon/down_arrow.png);\n"
"    width: 15px;\n"
"    height:15px;\n"
"}")
        self.top_range_box.setObjectName("top_range_box")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.top_range_box.addItem("")
        self.gridLayout.addWidget(self.top_range_box, 2, 1, 1, 1)
        self.sorting_data_added = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_data_added.setFont(font)
        self.sorting_data_added.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_data_added.setObjectName("sorting_data_added")
        self.gridLayout.addWidget(self.sorting_data_added, 0, 2, 1, 1)
        self.sorting_relevance = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_relevance.setFont(font)
        self.sorting_relevance.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_relevance.setObjectName("sorting_relevance")
        self.gridLayout.addWidget(self.sorting_relevance, 0, 0, 1, 1)
        self.sorting_random = QtWidgets.QRadioButton(self.sorting_box)
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sorting_random.setFont(font)
        self.sorting_random.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sorting_random.setObjectName("sorting_random")
        self.gridLayout.addWidget(self.sorting_random, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.sorting_box, 2, 0, 1, 1)
        self.ratios_box = QtWidgets.QGroupBox(self.img_set_table)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratios_box.setFont(font)
        self.ratios_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratios_box.setObjectName("ratios_box")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ratios_box)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ratio_10x9 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_10x9.setFont(font)
        self.ratio_10x9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_10x9.setObjectName("ratio_10x9")
        self.gridLayout_2.addWidget(self.ratio_10x9, 1, 0, 1, 1)
        self.ratio_48x9 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_48x9.setFont(font)
        self.ratio_48x9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_48x9.setObjectName("ratio_48x9")
        self.gridLayout_2.addWidget(self.ratio_48x9, 2, 1, 1, 1)
        self.ratio_10x16 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_10x16.setFont(font)
        self.ratio_10x16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_10x16.setObjectName("ratio_10x16")
        self.gridLayout_2.addWidget(self.ratio_10x16, 2, 2, 1, 1)
        self.ratio_3x2 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_3x2.setFont(font)
        self.ratio_3x2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_3x2.setObjectName("ratio_3x2")
        self.gridLayout_2.addWidget(self.ratio_3x2, 1, 3, 1, 1)
        self.ratio_9x16 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_9x16.setFont(font)
        self.ratio_9x16.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_9x16.setObjectName("ratio_9x16")
        self.gridLayout_2.addWidget(self.ratio_9x16, 0, 2, 1, 1)
        self.ratio_5x4 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_5x4.setFont(font)
        self.ratio_5x4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_5x4.setObjectName("ratio_5x4")
        self.gridLayout_2.addWidget(self.ratio_5x4, 3, 3, 1, 1)
        self.ratio_4x3 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_4x3.setFont(font)
        self.ratio_4x3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_4x3.setObjectName("ratio_4x3")
        self.gridLayout_2.addWidget(self.ratio_4x3, 2, 3, 1, 1)
        self.ratio_1x1 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_1x1.setFont(font)
        self.ratio_1x1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_1x1.setObjectName("ratio_1x1")
        self.gridLayout_2.addWidget(self.ratio_1x1, 0, 3, 1, 1)
        self.ratio_21x9 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_21x9.setFont(font)
        self.ratio_21x9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_21x9.setObjectName("ratio_21x9")
        self.gridLayout_2.addWidget(self.ratio_21x9, 0, 1, 1, 1)
        self.ratio_16x9 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_16x9.setFont(font)
        self.ratio_16x9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_16x9.setObjectName("ratio_16x9")
        self.gridLayout_2.addWidget(self.ratio_16x9, 0, 0, 1, 1)
        self.ratio_32x9 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_32x9.setFont(font)
        self.ratio_32x9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_32x9.setObjectName("ratio_32x9")
        self.gridLayout_2.addWidget(self.ratio_32x9, 1, 1, 1, 1)
        self.ratio_9x18 = QtWidgets.QCheckBox(self.ratios_box)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ratio_9x18.setFont(font)
        self.ratio_9x18.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ratio_9x18.setObjectName("ratio_9x18")
        self.gridLayout_2.addWidget(self.ratio_9x18, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.ratios_box, 3, 0, 1, 1)
        self.tabWidget.addTab(self.img_set_table, "")
        self.sys_set_tab = QtWidgets.QWidget()
        self.sys_set_tab.setObjectName("sys_set_tab")
        self.groupBox = QtWidgets.QGroupBox(self.sys_set_tab)
        self.groupBox.setGeometry(QtCore.QRect(9, 41, 351, 91))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.time_10m = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_10m.setFont(font)
        self.time_10m.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_10m.setObjectName("time_10m")
        self.gridLayout_3.addWidget(self.time_10m, 0, 1, 1, 1)
        self.time_30m = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_30m.setFont(font)
        self.time_30m.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_30m.setObjectName("time_30m")
        self.gridLayout_3.addWidget(self.time_30m, 0, 2, 1, 1)
        self.time_3h = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_3h.setFont(font)
        self.time_3h.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_3h.setObjectName("time_3h")
        self.gridLayout_3.addWidget(self.time_3h, 1, 1, 1, 1)
        self.time_1h = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_1h.setFont(font)
        self.time_1h.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_1h.setObjectName("time_1h")
        self.gridLayout_3.addWidget(self.time_1h, 1, 0, 1, 1)
        self.time_close = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_close.setFont(font)
        self.time_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_close.setChecked(True)
        self.time_close.setObjectName("time_close")
        self.gridLayout_3.addWidget(self.time_close, 0, 0, 1, 1)
        self.time_5h = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.time_5h.setFont(font)
        self.time_5h.setFocusPolicy(QtCore.Qt.NoFocus)
        self.time_5h.setObjectName("time_5h")
        self.gridLayout_3.addWidget(self.time_5h, 1, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.sys_set_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 351, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.img_path_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.img_path_label.setFont(font)
        self.img_path_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.img_path_label.setObjectName("img_path_label")
        self.horizontalLayout_4.addWidget(self.img_path_label)
        self.img_path = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.img_path.setFont(font)
        self.img_path.setFocusPolicy(QtCore.Qt.TabFocus)
        self.img_path.setObjectName("img_path")
        self.horizontalLayout_4.addWidget(self.img_path)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.err_path_tip = QtWidgets.QLabel(self.groupBox_2)
        self.err_path_tip.setEnabled(True)
        self.err_path_tip.setStyleSheet("color:rgb(255, 85, 0)")
        self.err_path_tip.setAlignment(QtCore.Qt.AlignCenter)
        self.err_path_tip.setWordWrap(False)
        self.err_path_tip.setIndent(-1)
        self.err_path_tip.setObjectName("err_path_tip")
        self.verticalLayout.addWidget(self.err_path_tip)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_dir_btn = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.open_dir_btn.setFont(font)
        self.open_dir_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.open_dir_btn.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: #ffffff; /*背景色*/ \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius:3px; /*边界圆滑*/\n"
"    border-color: rgb(189, 188, 191);\n"
"    color:black; /*字体颜色*/\n"
"    padding: 2px;\n"
"}\n"
" \n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(226, 241, 249);\n"
"    border-width: 1px;\n"
"    border-color: rgb(40, 99, 142);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #ffffff; /*伪状态经过时背景色*/ \n"
"    border-style: inset;\n"
"}\n"
"")
        self.open_dir_btn.setAutoDefault(False)
        self.open_dir_btn.setDefault(False)
        self.open_dir_btn.setFlat(False)
        self.open_dir_btn.setObjectName("open_dir_btn")
        self.horizontalLayout_3.addWidget(self.open_dir_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.change_dir_btn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_dir_btn.sizePolicy().hasHeightForWidth())
        self.change_dir_btn.setSizePolicy(sizePolicy)
        self.change_dir_btn.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.change_dir_btn.setFont(font)
        self.change_dir_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_dir_btn.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"    background-color: #ffffff; /*背景色*/ \n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius:3px; /*边界圆滑*/\n"
"    border-color: rgb(189, 188, 191);\n"
"    color:black; /*字体颜色*/\n"
"    padding: 2px;\n"
"}\n"
" \n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(226, 241, 249);\n"
"    border-width: 1px;\n"
"    border-color: rgb(40, 99, 142);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #ffffff; /*伪状态经过时背景色*/ \n"
"    border-style: inset;\n"
"}\n"
"")
        self.change_dir_btn.setObjectName("change_dir_btn")
        self.horizontalLayout_3.addWidget(self.change_dir_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.autoRun = QtWidgets.QCheckBox(self.sys_set_tab)
        self.autoRun.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.autoRun.setFont(font)
        self.autoRun.setObjectName("autoRun")
        self.tabWidget.addTab(self.sys_set_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "wallhaven v1.0"))
        self.purity_box.setTitle(_translate("MainWindow", "内容筛选"))
        self.purity_sfw.setToolTip(_translate("MainWindow", "正经图片"))
        self.purity_sfw.setText(_translate("MainWindow", "SFW"))
        self.purity_sketchy.setToolTip(_translate("MainWindow", "带点颜色"))
        self.purity_sketchy.setText(_translate("MainWindow", "Sketchy"))
        self.category_box.setTitle(_translate("MainWindow", "风格选择"))
        self.cate_general.setText(_translate("MainWindow", "普通"))
        self.cate_anime.setText(_translate("MainWindow", "二次元"))
        self.cate_people.setText(_translate("MainWindow", "三次元"))
        self.sorting_box.setTitle(_translate("MainWindow", "排序方式"))
        self.sorting_views.setText(_translate("MainWindow", "Views"))
        self.sorting_favorites.setText(_translate("MainWindow", "Favorites"))
        self.sorting_hot.setText(_translate("MainWindow", "Hot"))
        self.sorting_toplist.setText(_translate("MainWindow", "Toplist"))
        self.top_range_box.setItemText(0, _translate("MainWindow", "Last Day"))
        self.top_range_box.setItemText(1, _translate("MainWindow", "Last 3 Days"))
        self.top_range_box.setItemText(2, _translate("MainWindow", "Last Week"))
        self.top_range_box.setItemText(3, _translate("MainWindow", "Last Month"))
        self.top_range_box.setItemText(4, _translate("MainWindow", "Last 3 Months"))
        self.top_range_box.setItemText(5, _translate("MainWindow", "Last 6 Months"))
        self.top_range_box.setItemText(6, _translate("MainWindow", "Last Year"))
        self.sorting_data_added.setText(_translate("MainWindow", "Date Added"))
        self.sorting_relevance.setText(_translate("MainWindow", "Relevance"))
        self.sorting_random.setText(_translate("MainWindow", "Random"))
        self.ratios_box.setTitle(_translate("MainWindow", "图片比例"))
        self.ratio_10x9.setText(_translate("MainWindow", "10x9"))
        self.ratio_48x9.setText(_translate("MainWindow", "48x9"))
        self.ratio_10x16.setText(_translate("MainWindow", "10x16"))
        self.ratio_3x2.setText(_translate("MainWindow", "3x2"))
        self.ratio_9x16.setText(_translate("MainWindow", "9x16"))
        self.ratio_5x4.setText(_translate("MainWindow", "5x4"))
        self.ratio_4x3.setText(_translate("MainWindow", "4x3"))
        self.ratio_1x1.setText(_translate("MainWindow", "1x1"))
        self.ratio_21x9.setText(_translate("MainWindow", "21x9"))
        self.ratio_16x9.setText(_translate("MainWindow", "16x9"))
        self.ratio_32x9.setText(_translate("MainWindow", "32x9"))
        self.ratio_9x18.setText(_translate("MainWindow", "9x18"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.img_set_table), _translate("MainWindow", "图片设置"))
        self.groupBox.setTitle(_translate("MainWindow", "定时切换"))
        self.time_10m.setText(_translate("MainWindow", "10分钟"))
        self.time_30m.setText(_translate("MainWindow", "30分钟"))
        self.time_3h.setText(_translate("MainWindow", "3小时"))
        self.time_1h.setText(_translate("MainWindow", "1小时"))
        self.time_close.setText(_translate("MainWindow", "关闭"))
        self.time_5h.setText(_translate("MainWindow", "5小时"))
        self.groupBox_2.setTitle(_translate("MainWindow", "图片存储位置"))
        self.img_path_label.setText(_translate("MainWindow", "路径："))
        self.err_path_tip.setText(_translate("MainWindow", "配置文件中路径不合法，已使用默认路径。"))
        self.open_dir_btn.setText(_translate("MainWindow", "打开路径"))
        self.change_dir_btn.setText(_translate("MainWindow", "更改"))
        self.autoRun.setText(_translate("MainWindow", "开机自启"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sys_set_tab), _translate("MainWindow", "系统设置"))
