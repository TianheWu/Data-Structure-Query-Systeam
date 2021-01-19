"""
Project title: Metro fare information table generation system
Module title: Process_station_data
Date of coding: 2020.9.12 - 2020.9.15
Last modification date: 2020.9.17
Design person name: Tianhe Wu
"""


from Data_Structure.Dijkstra_DS.Pair_Class import Pair

# Define the index for every station
STATION_INDEX = 0


# Define the class station
class Station:

    def __init__(self, subway_line_index_: str, station_name_: str = '', to_next_length_: int = 0) -> None:

        # Belong which subway line
        self.subway_line_index = subway_line_index_
        # Station name
        self.station_name = station_name_
        # The length to the next station
        self.to_next_length = to_next_length_
        # Station index
        self.index = STATION_INDEX
        self.plus_index()

    def plus_index(self) -> None:
        global STATION_INDEX
        STATION_INDEX += 1


# Build adjacency
def build_adjacency(station_name_dict: dict, station_index_dict: dict, graph_list: [[Pair]]) -> None:

    file_object = open('D:\wutianhe_document\DS_project\BaseSubWayInfo.txt', encoding='utf-8')

    for line in file_object.readlines():

        line = line.strip('\n')
        line = line.split('，')
        if len(line) == 1:
            continue

        # Input the data except the last data
        for i in range(3, len(line) - 3, 2):

            if line[i] not in station_name_dict:
                # Current station
                station_name_dict[line[i]] = Station(line[1], line[i], float(line[i + 1]))
                station_index_dict[STATION_INDEX - 1] = line[i]

            if line[i + 2] not in station_name_dict:
                # Next station
                station_name_dict[line[i + 2]] = Station(line[1], line[i + 2], float(line[i + 3]))
                station_index_dict[STATION_INDEX - 1] = line[i + 2]

            # Append element from index to target index
            graph_list[station_name_dict[line[i]].index].append(
                Pair(float(line[i + 1]), station_name_dict[line[i + 2]].index))
            graph_list[station_name_dict[line[i + 2]].index].append(
                Pair(float(line[i + 1]), station_name_dict[line[i]].index))

        # Input the last data
        if line[-1] not in station_name_dict:
            station_name_dict[line[-1]] = Station(line[1], line[-1], float(line[-2]))
            station_index_dict[STATION_INDEX - 1] = line[-1]

        graph_list[station_name_dict[line[-1]].index].append(Pair(float(line[-2]), station_name_dict[line[-3]].index))
        graph_list[station_name_dict[line[-3]].index].append(Pair(float(line[-2]), station_name_dict[line[-1]].index))

    # print(STATION_INDEX)
