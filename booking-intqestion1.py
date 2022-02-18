#!/bin/python3
"""
Site Reliability Engineer Interview
    They gave me the below question to solve in 30 mins.
    Based on customer research, we know that our guests get confused when they are searching for accommodation and they found multiple hotels
    with the same name in the same city.
    To avoid this, we want to create a tool to identify "confusing" cities: cities with at least 3 hotels with the same name.
    Given a list of tuples (hotel_id, hotel_name, city) return a list of all "confusing" cities.

    Input: [
      {hotel_1234, "Sheraton", "Amsterdam"},
      {hotel_1000, "Sheraton", "Buenos Aires"},
      {hotel_1001, "Hilton", "Amsterdam"},
      {hotel_1002, "Royal Palace", "Bogota"},
      {hotel_1003, "Hilton", "Amsterdam"},
      {hotel_1004, "Sheraton", "Buenos Aires"},
      {hotel_1005, "Sheraton", "Buenos Aires"}
    ]

    Output: [ "Buenos Aires" ]
"""
from collections import Counter

Input_wrong = [
("hotel_1234", "Sheraton", "Amsterdam"),
("hotel_1000", "Sheraton", "Buenos Aires"),
("hotel_1001", "Hilton", "Amsterdam"),
("hotel_1002", "Royal Palace", "Bogota"),
("hotel_1003", "Hilton", "Amsterdam"),
("hotel_1004", "Sheraton", "Buenos Aires"),
("hotel_1005", "Sheraton", "Buenos Aires")
]

Input_correct = [
{"hotel_1234", "Sheraton", "Amsterdam"},
{"hotel_1000", "Sheraton", "Buenos Aires"},
{"hotel_1001", "Hilton", "Amsterdam"},
{"hotel_1002", "Royal Palace", "Bogota"},
{"hotel_1003", "Hilton", "Amsterdam"},
{"hotel_1004", "Sheraton", "Buenos Aires"},
{"hotel_1005", "Sheraton", "Buenos Aires"}
]

#1ST solution via Counter
confusing_cities = []
for i,v in Counter((elem[1],elem[2]) for elem in Input_wrong).items():
    #dict_items([(('Sheraton', 'Amsterdam'), 1), (('Sheraton', 'Buenos Aires'), 3), (('Hilton', 'Amsterdam'), 2), (('Royal Palace', 'Bogota'), 1)])
    if v >= 3:
        confusing_cities.append(i[1])
print("1ST solution")
print(confusing_cities)


#2ND solution plain
confusing_cities = []
counter = {}
whithout_hnumber = []
# get rid of hotel number
for elem in Input_wrong:
    whithout_hnumber.append(elem[1:])
# count element whithout_hnumber
for elem in whithout_hnumber:
    if elem not in counter:
        counter[elem] = 0
    counter[elem] += 1
# counter output is: {('Sheraton', 'Amsterdam'): 1, ('Sheraton', 'Buenos Aires'): 3, ('Hilton', 'Amsterdam'): 2, ('Royal Palace', 'Bogota'): 1}
#iterate by keys of dict (like ('Sheraton', 'Amsterdam'))
for key in counter:
    #get value of the dict that is amount of same hotels in the same city
    if int(counter[key]) >= 3:
        confusing_cities.append(key[1])
print("2ND solution")
print(confusing_cities)

#3D solution via intersection not finished
intersection = {}

for i in Input_correct:
    intersection = set.intersection(i)
print("3D solution")
print(list(intersection)[1])
