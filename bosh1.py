#!/bin/python3

import math
import os
import random
import re
import sys
import ast



def data_transformer(data,group_size):
    data_transformed = []
    temp_array = []
           
    for i in data:
        if type(i)==int:
            temp_array.append(i)
            
    data_transformed = split_by_size(temp_array,group_size)
    print(data_transformed)

def split_by_size(temp_array, group_size):
     result = []
     while len(temp_array) > group_size:
         part = temp_array[:group_size]
         result.append(part)
         temp_array   = temp_array[group_size:]
     result.append(temp_array)
     return result

data = [1,2,True,3,5,5,'string1',5.6,8,6,3,2.1,'string2']
data_transformer(data, 3)