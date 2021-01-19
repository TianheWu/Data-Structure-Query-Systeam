"""
Project title: Metro fare information table generation system
Module title: Length_algorithm
Date of coding: 2020.9.14-2020.9.17
Last modification date: 2020.9.17
Design person name: Tianhe Wu
"""


from Data_Structure.Dijkstra_DS.Pair_Class import Pair
from Data_Structure.Dijkstra_DS.Priority_queue import Priority_queue

# Define the maximum
MAX_NUM = 100005


def dijkstra_algorithm(start_station: str, graph_list: [[Pair]], station_num: int, station_name_dict: dict) -> [list]:

    # Start station index
    start_index = station_name_dict[start_station].index
    # List for length
    mem_list = [[MAX_NUM] * 2 for _ in range(station_num + 1)]
    # Define the priority_queue
    que = Priority_queue()
    # Initialization
    que.push(Pair(0, start_index))
    mem_list[start_index] = [0, start_index]

    while not que.empty():
        top_element = que.top()
        # pr = top_element.to_length
        node = top_element.index_pair
        que.pop()
        # if (pr > mem_list[node][0]):
        # continue
        for edge in graph_list[node]:
            val = edge.to_length
            node_next = edge.index_pair
            if mem_list[node_next][0] > mem_list[node][0] + val:
                # Renew the length
                mem_list[node_next][0] = mem_list[node][0] + val
                # Record previous node
                mem_list[node_next][1] = node
                que.push(Pair(mem_list[node_next][0], node_next))

    return mem_list
