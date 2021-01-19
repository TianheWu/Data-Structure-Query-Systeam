"""
Project title: Metro fare information table generation system
Module title: Main_GUI
Date of coding: 2020.9.21
Last modification date: 2020.12.16
Design person name: Tianhe Wu
"""

from Initialization.Data_Read.Init_Coordinate import Map_subway
import matplotlib.pyplot as plt


class Init_Map:

    def __init__(self) -> None:
        # Get coordinate of stations
        self.map_subway = Map_subway()
        # Station name -> lon and lat, str -> list [lon, lat]
        self.station_lon_lat = {}
        self.init_match()

    # Match the station coordinate with station name
    def init_match(self) -> None:
        self.map_subway.match(self.station_lon_lat)

    # Draw the map
    def draw_map(self) -> None:
        # Draw the line of station
        self.map_subway.get_coordinate()
        # Draw the point of station
        self.map_subway.plot_station(True)
        # Show the graph of the station map
        plt.show()

    # Update the map
    def draw_new_map(self, route_list: list) -> None:
        self.map_subway.update_graph(route_list)




