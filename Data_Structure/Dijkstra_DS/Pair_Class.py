"""
Project title: Metro fare information table generation system
Module title: Pair_class
Date of coding: 2020.9.15
Last modification date: 2020.9.15
Design person name: Tianhe Wu
"""


# Define the pair node: station index with to_station length
class Pair:

    def __init__(self, to_length_: float, index_pair_: int) -> None:
        self.to_length = to_length_
        self.index_pair = index_pair_
