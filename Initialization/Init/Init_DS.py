"""
Project title: Metro fare information table generation system
Module title: Main_algorithm
Date of coding: 2020.9.13-
Last modification date: 2020.11.28
Design person name: Tianhe Wu
"""

from Initialization.Data_Read.Init_Station import build_adjacency
from Algorithm.Dijkstra import dijkstra_algorithm
from Data_Structure.Display.Display_Class import Display


class Init_DS:

    def __init__(self) -> None:
        # Station name: str -> class Station
        self.station_name_dict = {}
        # Station index: int -> station name: str
        self.station_index_dict = {}
        # Initialize adjacency list: [[Pair]]
        self.graph_list = [[] for _ in range(700)]
        self._list_station_ = [[]]

    # Init the graph
    def init_graph(self) -> None:
        # Build adjacency list (Undirected graph)
        build_adjacency(self.station_name_dict, self.station_index_dict, self.graph_list)

    # Init the display_class all
    def init_display_all(self, user_start_station: str) -> None:
        self._list_station_ = dijkstra_algorithm(user_start_station, self.graph_list, 287, self.station_name_dict)
        self.display_all_c = Display(user_start_station, '', self._list_station_,
                          self.station_index_dict, self.station_name_dict)

    # Init the display_class pair
    def init_display_basic(self, user_start_station: str, user_end_station: str) -> None:
        self._list_station_ = dijkstra_algorithm(user_start_station, self.graph_list, 287, self.station_name_dict)
        self.display_basic_c = Display(user_start_station, user_end_station, self._list_station_,
                          self.station_index_dict, self.station_name_dict)

