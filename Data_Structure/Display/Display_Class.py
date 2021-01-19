"""
Project title: Metro fare information table generation system
Module title: Display_function
Date of coding: 2020.9.17
Last modification date: 2020.12.16
Design person name: Tianhe Wu
"""


class Display:

    def __init__(self, start_name_: str, end_name_: str, list_station_: [list], station_idx_: dict,
                 name_dict_: dict) -> None:
        self.start_name = start_name_
        self.end_name = end_name_
        self.list_station = list_station_
        # Station index -> name
        self.station_idx = station_idx_
        # Name -> class station
        self.name_dict = name_dict_
        self.frame_str_all = ''
        self.frame_str_basic = ''

    # GUI one station to others station length and money
    def display_all(self) -> None:
        for i in range(len(self.list_station)):
            print(self.start_name, '->', self.station_idx[i], '距离为', self.list_station[i][0], '公里', '需要',
                  self.get_money(i), '元')

    # GUI the string in Frame_UI
    def display_all_ui(self) -> str:
        for i in range(len(self.list_station)):
            self.frame_str_all += str(self.start_name) + ' -> ' + str(self.station_idx[i]) + ' 距离为 ' + \
                                  str(self.list_station[i][0]) + ' 公里 ' + '需要 ' + str(self.get_money(i)) + ' 元 ' + '\n'
        return self.frame_str_all

    # DFS to find the start station
    def dfs(self, cur_end: int, start: int, line_list: list) -> None:
        line_list.append(self.station_idx[cur_end])
        if cur_end == start:
            return
        self.dfs(self.list_station[cur_end][1], start, line_list)

    # GUI route about the min length
    def display_line(self) -> list:
        line_list = []
        start_idx = self.name_dict[self.start_name].index
        end_idx = self.name_dict[self.end_name].index
        self.dfs(end_idx, start_idx, line_list)
        line_list.reverse()
        # print(line_list)
        return line_list

    # GUI route about the min length UI
    def display_line_ui(self) -> str:
        line_list = []
        start_idx = self.name_dict[self.start_name].index
        end_idx = self.name_dict[self.end_name].index
        self.dfs(end_idx, start_idx, line_list)
        line_list.reverse()
        return str(line_list)

    # GUI the two station
    def display_basic(self) -> None:
        end_idx = self.name_dict[self.end_name].index
        print(self.start_name, '到', self.end_name, '距离为', self.list_station[end_idx][0], '票价为：',
              self.get_money(end_idx))

    # GUI the two station in UI
    def display_basic_ui(self) -> str:
        end_idx = self.name_dict[self.end_name].index
        self.frame_str_basic += str(self.start_name) + ' 到 ' + str(self.end_name) + ' 距离为 ' \
                                + str(self.list_station[end_idx][0]) + ' 票价为：' + str(self.get_money(end_idx))
        return self.frame_str_basic

    # Compute the money
    def get_money(self, idx_: int) -> int:
        money = 0
        if self.list_station[idx_][0] < 6:
            money = 3
        elif self.list_station[idx_][0] < 12:
            money = 4
        elif self.list_station[idx_][0] < 22:
            money = 5
        elif self.list_station[idx_][0] < 32:
            money = 6
        elif self.list_station[idx_][0] < 52:
            money = 7
        elif self.list_station[idx_][0] < 72:
            money = 8
        elif self.list_station[idx_][0] < 92:
            money = 9
        return money
