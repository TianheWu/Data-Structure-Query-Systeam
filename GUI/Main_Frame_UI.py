"""
Project title: Metro fare information table generation system
Module title: Run_FrameUI
Date of coding: 2020.11.27
Last modification date: 2020.12.16
Design person name: Tianhe Wu
"""

import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from GUI.Frame_UI import Ui_Form
from Initialization.Init.Init_DS import Init_DS
from Initialization.Init.Init_Map import Init_Map


class Main_Frame(QWidget, Ui_Form):

    def __init__(self, parent=None) -> None:
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Set the button print
        self.print_button.clicked.connect(self.display_all)
        self.print_button_2.clicked.connect(self.display_basic)
        self.draw_button.clicked.connect(self.display_update_map)
        self.draw_pic.clicked.connect(self.display_map)

        # Set the button close
        self.exit_button.clicked.connect(self.close)

        # Set image  --------------------------------------------------------------------------
        pixmap_1 = QPixmap('D:\wutianhe_document\DS_project\label_image_1.png')
        self.image_1.setPixmap(pixmap_1)
        self.image_1.setScaledContents(True)

        pixmap_2 = QPixmap('D:\wutianhe_document\DS_project\line1.png')
        self.label_3.setPixmap(pixmap_2)
        self.label_3.setScaledContents(True)

        pixmap_3 = QPixmap('D:\wutianhe_document\DS_project\lin2.png')
        self.label_4.setPixmap(pixmap_3)
        self.label_4.setScaledContents(True)

        pixmap_4 = QPixmap('D:\wutianhe_document\DS_project\line4.png')
        self.label_6.setPixmap(pixmap_4)
        self.label_6.setScaledContents(True)

        pixmap_5 = QPixmap('D:\wutianhe_document\DS_project\line5.png')
        self.label_7.setPixmap(pixmap_5)
        self.label_7.setScaledContents(True)

        pixmap_6 = QPixmap('D:\wutianhe_document\DS_project\line6.png')
        self.label_8.setPixmap(pixmap_6)
        self.label_8.setScaledContents(True)

        pixmap_7 = QPixmap('D:\wutianhe_document\DS_project\line7.png')
        self.label_9.setPixmap(pixmap_7)
        self.label_9.setScaledContents(True)

        pixmap_8 = QPixmap('D:\wutianhe_document\DS_project\line8.png')
        self.label_10.setPixmap(pixmap_8)
        self.label_10.setScaledContents(True)

        pixmap_9 = QPixmap('D:\wutianhe_document\DS_project\line9.png')
        self.label_11.setPixmap(pixmap_9)
        self.label_11.setScaledContents(True)

        pixmap_10 = QPixmap('D:\wutianhe_document\DS_project\line10.png')
        self.label_12.setPixmap(pixmap_10)
        self.label_12.setScaledContents(True)

        pixmap_11 = QPixmap('D:\wutianhe_document\DS_project\line13.png')
        self.label_13.setPixmap(pixmap_11)
        self.label_13.setScaledContents(True)

        pixmap_12 = QPixmap('D:\wutianhe_document\DS_project\line14_1.png')
        self.label_14.setPixmap(pixmap_12)
        self.label_14.setScaledContents(True)

        pixmap_13 = QPixmap('D:\wutianhe_document\DS_project\line14_2.png')
        self.label_15.setPixmap(pixmap_13)
        self.label_15.setScaledContents(True)

        pixmap_14 = QPixmap('D:\wutianhe_document\DS_project\line01.png')
        self.label_16.setPixmap(pixmap_14)
        self.label_16.setScaledContents(True)

        pixmap_15 = QPixmap('D:\wutianhe_document\DS_project\line02.png')
        self.label_17.setPixmap(pixmap_15)
        self.label_17.setScaledContents(True)

        pixmap_16 = QPixmap('D:\wutianhe_document\DS_project\line03.png')
        self.label_18.setPixmap(pixmap_16)
        self.label_18.setScaledContents(True)

        pixmap_17 = QPixmap('D:\wutianhe_document\DS_project\line04.png')
        self.label_19.setPixmap(pixmap_17)
        self.label_19.setScaledContents(True)

        pixmap_18 = QPixmap('D:\wutianhe_document\DS_project\line05.png')
        self.label_20.setPixmap(pixmap_18)
        self.label_20.setScaledContents(True)

        pixmap_19 = QPixmap('D:\wutianhe_document\DS_project\line06.png')
        self.label_21.setPixmap(pixmap_19)
        self.label_21.setScaledContents(True)

        # Set image done -----------------------------------------------------------------

        # Initialize the ds
        self.init_ds = Init_DS()
        self.init_ds.init_graph()

        # Draw the dynamic route
        self.draw_list_tmp = []
        # self.display_map()

    # GUI all station info
    def display_all(self) -> None:
        # Get the start station and end station from text
        start = self.start_text.text()
        if start == '':
            self.output_text_2.setText('请输入地铁站名称')
            return
        if start not in self.init_ds.station_name_dict:
            self.output_text_2.setText('没有该地铁站')
            return
        self.output_text_2.setText('')
        self.init_ds.init_display_all(start)

        # Output the content into table
        # Define the lines
        line_1 = []
        line_2 = []
        line_4 = []
        line_5 = []
        line_6 = []
        line_7 = []
        line_8 = []
        line_9 = []
        line_10 = []
        line_13 = []
        # 14 line east
        line_14_1 = []
        # 14 line west
        line_14_2 = []
        line_15 = []
        # 八通线
        line_01 = []
        # 昌平线
        line_02 = []
        # 大兴线
        line_03 = []
        # 房山线
        line_04 = []
        # 机场线
        line_05 = []
        # 亦庄线
        line_06 = []

        # Insert the index into lines list
        for i in range(len(self.init_ds.display_all_c.list_station)):
            station_name = str(self.init_ds.display_all_c.station_idx[i])
            if self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '1号线':
                line_1.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '2号线':
                line_2.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '4号线':
                line_4.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '5号线':
                line_5.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '6号线':
                line_6.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '7号线':
                line_7.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '8号线':
                line_8.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '9号线':
                line_9.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '10号线':
                line_10.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '13号线':
                line_13.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '14号线东段':
                line_14_1.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '14号线西段':
                line_14_2.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '15号线':
                line_15.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '八通线':
                line_01.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '昌平线':
                line_02.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '大兴线':
                line_03.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '房山线':
                line_04.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '机场线':
                line_05.append(i)
            elif self.init_ds.display_all_c.name_dict[station_name].subway_line_index == '亦庄线':
                line_06.append(i)

        # Set the table size and content
        self.table_widget_1.setColumnCount(3)
        self.table_widget_1.setRowCount(len(line_1))

        # Input the data into tables
        for i in range(len(line_1)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_1[i]])
            self.table_widget_1.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_1.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_1[i]][0], '.3f'))))
            self.table_widget_1.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_1[i]))))

        # Set the table size and content
        self.table_widget_2.setColumnCount(3)
        self.table_widget_2.setRowCount(len(line_2))

        for i in range(len(line_2)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_2[i]])
            self.table_widget_2.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_2.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_2[i]][0], '.3f'))))
            self.table_widget_2.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_2[i]))))

        # Set the table size and content
        self.table_widget_3.setColumnCount(3)
        self.table_widget_3.setRowCount(len(line_4))

        for i in range(len(line_4)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_4[i]])
            self.table_widget_3.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_3.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_4[i]][0], '.3f'))))
            self.table_widget_3.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_4[i]))))

        # Set the table size and content
        self.table_widget_4.setColumnCount(3)
        self.table_widget_4.setRowCount(len(line_5))

        for i in range(len(line_5)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_5[i]])
            self.table_widget_4.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_4.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_5[i]][0], '.3f'))))
            self.table_widget_4.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_5[i]))))

        # Set the table size and content
        self.table_widget_5.setColumnCount(3)
        self.table_widget_5.setRowCount(len(line_6))

        for i in range(len(line_6)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_6[i]])
            self.table_widget_5.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_5.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_6[i]][0], '.3f'))))
            self.table_widget_5.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_6[i]))))

        # Set the table size and content
        self.table_widget_6.setColumnCount(3)
        self.table_widget_6.setRowCount(len(line_7))

        for i in range(len(line_7)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_7[i]])
            self.table_widget_6.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_6.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_7[i]][0], '.3f'))))
            self.table_widget_6.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_7[i]))))

        # Set the table size and content
        self.table_widget_7.setColumnCount(3)
        self.table_widget_7.setRowCount(len(line_8))

        for i in range(len(line_8)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_8[i]])
            self.table_widget_7.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_7.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_8[i]][0], '.3f'))))
            self.table_widget_7.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_8[i]))))

        # Set the table size and content
        self.table_widget_8.setColumnCount(3)
        self.table_widget_8.setRowCount(len(line_9))

        for i in range(len(line_9)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_9[i]])
            self.table_widget_8.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_8.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_9[i]][0], '.3f'))))
            self.table_widget_8.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_9[i]))))

        # Set the table size and content
        self.table_widget_9.setColumnCount(3)
        self.table_widget_9.setRowCount(len(line_10))

        for i in range(len(line_10)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_10[i]])
            self.table_widget_9.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_9.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_10[i]][0], '.3f'))))
            self.table_widget_9.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_10[i]))))

        # Set the table size and content
        self.table_widget_10.setColumnCount(3)
        self.table_widget_10.setRowCount(len(line_13))

        for i in range(len(line_13)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_13[i]])
            self.table_widget_10.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_10.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_13[i]][0], '.3f'))))
            self.table_widget_10.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_13[i]))))

        # Set the table size and content
        self.table_widget_11.setColumnCount(3)
        self.table_widget_11.setRowCount(len(line_14_1))

        for i in range(len(line_14_1)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_14_1[i]])
            self.table_widget_11.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_11.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_14_1[i]][0], '.3f'))))
            self.table_widget_11.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_14_1[i]))))

        # Set the table size and content
        self.table_widget_12.setColumnCount(3)
        self.table_widget_12.setRowCount(len(line_14_2))

        for i in range(len(line_14_2)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_14_2[i]])
            self.table_widget_12.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_12.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_14_2[i]][0], '.3f'))))
            self.table_widget_12.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_14_2[i]))))

        # Set the table size and content
        self.table_widget_13.setColumnCount(3)
        self.table_widget_13.setRowCount(len(line_01))

        for i in range(len(line_01)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_01[i]])
            self.table_widget_13.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_13.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_01[i]][0], '.3f'))))
            self.table_widget_13.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_01[i]))))

        # Set the table size and content
        self.table_widget_14.setColumnCount(3)
        self.table_widget_14.setRowCount(len(line_02))

        for i in range(len(line_02)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_02[i]])
            self.table_widget_14.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_14.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_02[i]][0], '.3f'))))
            self.table_widget_14.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_02[i]))))

        # Set the table size and content
        self.table_widget_15.setColumnCount(3)
        self.table_widget_15.setRowCount(len(line_03))

        for i in range(len(line_03)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_03[i]])
            self.table_widget_15.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_15.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_03[i]][0], '.3f'))))
            self.table_widget_15.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_03[i]))))

        # Set the table size and content
        self.table_widget_16.setColumnCount(3)
        self.table_widget_16.setRowCount(len(line_04))

        for i in range(len(line_04)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_04[i]])
            self.table_widget_16.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_16.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_04[i]][0], '.3f'))))
            self.table_widget_16.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_04[i]))))

        # Set the table size and content
        self.table_widget_17.setColumnCount(3)
        self.table_widget_17.setRowCount(len(line_05))

        for i in range(len(line_05)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_05[i]])
            self.table_widget_17.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_17.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_05[i]][0], '.3f'))))
            self.table_widget_17.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_05[i]))))

        # Set the table size and content
        self.table_widget_18.setColumnCount(3)
        self.table_widget_18.setRowCount(len(line_06))

        for i in range(len(line_06)):
            station_name = str(self.init_ds.display_all_c.station_idx[line_06[i]])
            self.table_widget_18.setItem(i, 0, QTableWidgetItem(station_name))
            self.table_widget_18.setItem(i, 1, QTableWidgetItem(
                str(format(self.init_ds.display_all_c.list_station[line_06[i]][0], '.3f'))))
            self.table_widget_18.setItem(i, 2, QTableWidgetItem(str(self.init_ds.display_all_c.get_money(line_06[i]))))

    # GUI the two station info
    def display_basic(self) -> None:
        # Input the start station and end station
        start = self.start_text.text()
        end = self.end_text.text()
        if start == '' or end == '':
            self.output_text_2.setText('请输入地铁站名称')
            return
        if start not in self.init_ds.station_name_dict or end not in self.init_ds.station_name_dict:
            self.output_text_2.setText('没有该地铁站')
            return
        self.output_text_2.setText('')
        self.init_ds.init_display_basic(start, end)
        display_str_1 = self.init_ds.display_basic_c.display_basic_ui()
        # Get the station name in min length
        line_tmp = self.init_ds.display_basic_c.display_line()
        display_str_2 = ''
        for i in range(len(line_tmp) - 1):
            display_str_2 += str(line_tmp[i]) + ' -> '
        display_str_2 += line_tmp[len(line_tmp) - 1]

        # Get special route line
        self.draw_list_tmp = self.init_ds.display_basic_c.display_line()
        self.output_text_2.setText(display_str_1 + '\n' + '最短线路路径为：' + '\n' + display_str_2)
        self.init_ds.display_basic_c.frame_str_basic = ''

    # GUI the map graph (Useless)
    def display_map(self) -> None:
        self.init_map = Init_Map()
        self.init_map.draw_map()

    # GUI the new map graph
    def display_update_map(self) -> None:
        # Initialize the map
        if len(self.draw_list_tmp) == 0:
            return
        self.init_map = Init_Map()
        self.init_map.draw_new_map(self.draw_list_tmp)


# Run the whole project
def run() -> None:
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    my_win = Main_Frame()
    my_win.show()
    sys.exit(app.exec_())
