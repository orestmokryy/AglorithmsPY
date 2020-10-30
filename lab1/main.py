from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort

import time

from utils.csv_to_list import csv_to_list

insertion_sort = InsertionSort()
merge_sort = MergeSort()


list_of_printers = csv_to_list()

list_of_printers_price = [item.price_in_UAH for item in list_of_printers]
list_of_printers_speed = [item.speed_in_pages_per_minute for item in list_of_printers]

start = time.time()
print(insertion_sort.descending_sort(list_of_printers_speed))
stop = time.time()
print(f"time:{stop-start}")
print('-'*30)
start = time.time()
print(merge_sort.sort_ascending(list_of_printers_price))
stop = time.time()
print(f"time:{stop-start}")
