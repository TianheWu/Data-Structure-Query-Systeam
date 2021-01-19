"""
Project title: Metro fare information table generation system
Module title: Heap_data_structure
Date of coding: 2020.9.14 - 2020.9.15
Last modification date: 2020.9.15
Design person name: Tianhe Wu
"""

from Data_Structure.Dijkstra_DS.Pair_Class import Pair

# Define max num
MAX_NUM_QUEUE = 1000005


class Priority_queue:

    def __init__(self) -> None:
        self.cur_size = 0
        self.heap_list = [MAX_NUM_QUEUE] * MAX_NUM_QUEUE

    def top(self) -> Pair:
        return self.heap_list[0]

    def empty(self) -> bool:
        return True if self.cur_size == 0 else False

    def parent(self, cur_pos_: int) -> int:
        return (cur_pos_ - 1) // 2

    # Push an element into queue
    def push(self, new_element_: Pair) -> None:
        self.heap_list[self.cur_size] = new_element_
        self.sift_up(self.cur_size)
        self.cur_size += 1

    # Pop out an element from queue[0]
    def pop(self) -> None:
        self.heap_list[0], self.heap_list[self.cur_size - 1] = self.heap_list[self.cur_size - 1], self.heap_list[0]
        self.cur_size -= 1
        if self.cur_size > 1:
            self.sift_down(0)

    def sift_up(self, cur_size_: int) -> None:
        tmp_pos = cur_size_
        tmp_var = self.heap_list[tmp_pos]

        while tmp_pos > 0 and self.heap_list[self.parent(tmp_pos)].to_length > tmp_var.to_length:
            self.heap_list[tmp_pos] = self.heap_list[self.parent(tmp_pos)]
            tmp_pos = self.parent(tmp_pos)

        self.heap_list[tmp_pos] = tmp_var

    def sift_down(self, cur_pos_: int) -> None:
        i = cur_pos_
        j = 2 * i + 1
        tmp_val = self.heap_list[i]
        while j < self.cur_size:
            if j < self.cur_size - 1 and self.heap_list[j].to_length > self.heap_list[j + 1].to_length:
                j += 1
            if tmp_val.to_length > self.heap_list[j].to_length:
                self.heap_list[i] = self.heap_list[j]
                i = j
                j = 2 * j + 1
            else:
                break
        self.heap_list[i] = tmp_val






