"""
Project title: Metro fare information table generation system
Module title: Process_coordinate_data
Date of coding: 2020.9.21
Last modification date: 2020.9.22
Design person name: Tianhe Wu
"""

import re
import copy
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


file_coordinate = open('D:\wutianhe_document\DS_project\Info_station.txt', encoding='utf-8')


class Map_subway:

    def __init__(self) -> None:
        plt.figure(figsize=(15, 15))
        ax = plt.gca()
        x_major_locator = MultipleLocator(0.05)
        ax.xaxis.set_major_locator(x_major_locator)
        self.lon_list = []
        self.lat_list = []
        self.cur_lon = []
        self.cur_lat = []
        self.color_dict = {'1': 'darkred', '2': 'royalblue', '4': 'mediumblue',
                           '5': 'darkmagenta', '6': 'goldenrod', '7': 'gold',
                           '8': 'seagreen', '9': 'limegreen', '10': 'dodgerblue',
                           '13': 'yellow', '01': 'orangered', '02': 'hotpink',
                           '03': 'firebrick', '04': 'deeppink', '05': 'mediumpurple',
                           '15': 'indigo', '14': 'lightpink'}
        self.legend_list = ['10号线', '2号线', '13号线', '房山线', '昌平线', '9号线', '八通线',
                            '1号线', '亦庄线', '5号线', '7号线', '8号线', '4号线/大兴线', '机场专线',
                            '15号线', '6号线', '14号线东段', '14号线西段']

        # Station name -> station lon and lat coordinate, [0] is lon [1] is lat
        self.station_info = {}

    # Match the station with coordinate
    def match(self, station_lon_lat: dict) -> None:
        for line in file_coordinate.readlines():
            line = line.strip('\n').split('\t')
            if len(line) != 1:
                if line[1] not in station_lon_lat:
                    station_lon_lat[line[1]] = [float(line[3]), float(line[4])]

        self.station_info = station_lon_lat
        file_coordinate.seek(0)
        # print(station_lon_lat) (for debug)

    # Get the coordinate and draw the line
    def get_coordinate(self) -> None:
        for line in file_coordinate.readlines():
            tmp_list = re.findall(r'\d+\.?\d*', line)
            if len(tmp_list) == 1:
                self.plot_line(self.cur_lon, self.cur_lat, self.color_dict[tmp_list[0]])
                self.cur_lon = []
                self.cur_lat = []
                continue

            self.cur_lon.append(float(tmp_list[1]))
            self.cur_lat.append(float(tmp_list[2]))
            self.lon_list.append(float(tmp_list[1]))
            self.lat_list.append(float(tmp_list[2]))

        # Set the pointer
        file_coordinate.seek(0)

    # Draw the line
    def plot_line(self, cur_lon_: list, cur_lat_: list, color_: str) -> None:
        # Remove axis
        plt.axis('off')
        # Appear chinese
        plt.rcParams['font.family'] = ['SimHei']
        # Draw subway line
        plt.plot(cur_lon_, cur_lat_, '-', color=color_, linewidth=2.4, alpha=0.5)
        # Set legend
        plt.legend(self.legend_list, bbox_to_anchor=(1, 0), loc=3, borderaxespad=0,
                   frameon=True, fontsize=11, labelspacing=1.994)

    # Draw the scatter
    def plot_station(self, is_title: bool) -> None:
        plt.xlim(min(self.lon_list) - 0.01, max(self.lon_list) + 0.01)
        plt.ylim(min(self.lat_list) - 0.01, max(self.lat_list) + 0.01)
        plt.scatter(self.lon_list, self.lat_list, label=None, c='k', marker='o', alpha=0.75, s=11)

        # Print the title of station
        if is_title == True:
            for i in self.station_info:
                plt.text(self.station_info[i][0], self.station_info[i][1], i, fontsize=8, rotation=30)

    # Draw the update graph
    def update_graph(self, station_line_: list) -> None:

        self.get_coordinate()
        self.plot_station(False)

        # For scatter
        _lon_list = []
        _lat_list = []

        for i in station_line_:
            _lon_list.append(self.station_info[i][0])
            _lat_list.append(self.station_info[i][1])

        for i in range(len(station_line_) - 1):
            str_cur = station_line_[i]
            str_next = station_line_[i + 1]

            # Draw dynamic points
            plt.scatter(self.station_info[str_cur][0], self.station_info[str_cur][1],
                        label=None, c='royalblue', marker='o', alpha=1, s=50)

            # Mark the start num and end num
            s_lon = self.station_info[str_cur][0]
            e_lon = self.station_info[str_next][0]
            s_lat = self.station_info[str_cur][1]
            e_lat = self.station_info[str_next][1]

            avg_lon = (e_lon - s_lon) / 3
            avg_lat = (e_lat - s_lat) / 3

            # Draw dynamic subway line
            while abs(e_lon - s_lon) > 0.000001 or abs(e_lat - s_lat) > 0.000001:
                lon_line = [s_lon, s_lon + avg_lon]
                lat_line = [s_lat, s_lat + avg_lat]
                plt.plot(lon_line, lat_line, '-', color='r', linewidth=3.5, alpha=1)
                if abs(e_lon - s_lon) > 0.000001:
                    s_lon += avg_lon
                if abs(e_lat - s_lat) > 0.000001:
                    s_lat += avg_lat
                plt.pause(0.009)

            plt.pause(0.1)

        # Draw the last point
        str_end = station_line_[len(station_line_) - 1]
        plt.scatter(self.station_info[str_end][0], self.station_info[str_end][1],
                   label=None, c='royalblue', marker='o', alpha=1, s=50)

        # Draw dynamic points
        plt.scatter(_lon_list, _lat_list,
                    label=None, c='royalblue', marker='o', alpha=1, s=80)
        plt.pause(0)
