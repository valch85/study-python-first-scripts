#!/bin/python3
"""
Site Reliability Engineer Interview
    They gave me the below question to solve in 30 mins.
    Based on customer research, we know that our guests get confused when they are searching for accommodation and they found multiple hotels
    with the same name in the same city.
    To avoid this, we want to create a tool to identify "confusing" cities: cities with at least 3 hotels with the same name.
    Given a list of tuples (hotel_id, hotel_name, city) return a list of all "confusing" cities.

    Input: [
      {hotel_1234, "Sheraton", "Amsterdam"} ,
      {hotel_1000, "Sheraton", "Buenos Aires"} ,
      {hotel_1001, "Hilton", "Amsterdam"} ,
      {hotel_1002, "Royal Palace", "Bogota"} ,
      {hotel_1003, "Hilton", "Amsterdam"} ,
      {hotel_1004, "Sheraton", "Buenos Aires"} ,
      {hotel_1005, "Sheraton", "Buenos Aires"}
    ]

    Output: [ "Buenos Aires" ]
"""
from collections import Counter

Input = [
("hotel_1234", "Sheraton", "Amsterdam") ,
("hotel_1000", "Sheraton", "Buenos Aires") ,
("hotel_1001", "Hilton", "Amsterdam") ,
("hotel_1002", "Royal Palace", "Bogota") ,
("hotel_1003", "Hilton", "Amsterdam") ,
("hotel_1004", "Sheraton", "Buenos Aires") ,
("hotel_1005", "Sheraton", "Buenos Aires")
]

confusing_cities = []
counter = {}
whithout_hnumber = []
"""
for i,v in Counter((elem[1],elem[2]) for elem in Input).items():
    #dict_items([(('Sheraton', 'Amsterdam'), 1), (('Sheraton', 'Buenos Aires'), 3), (('Hilton', 'Amsterdam'), 2), (('Royal Palace', 'Bogota'), 1)])
    print("i=" + str(i))
    print("v=" + str(v))
    if v >= 3:
        confusing_cities.append(i[1])
"""
# get rid of hotel number
for elem in Input:
    whithout_hnumber.append(elem[1:])

# count element whithout_hnumber
for elem in whithout_hnumber:
    if elem not in counter:
        counter[elem] = 0
    counter[elem] += 1

print(counter)

for i, v in counter:
    if v >= 3:
        confusing_cities.append(i[1])

print(confusing_cities)

