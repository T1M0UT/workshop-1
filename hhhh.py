import datetime
import csv
import pandas as pd

def read_file(path_file):
    '''
    The function reads file and do list of data

    '''
    to_do = []
    with open(path_file, 'r') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for line in file_reader:
            line1 = line[0].split(";")
            to_do.append(line1)
    return to_do

def all_time(list_with_deeds):
    '''
    The function shows dataframe to the user all plans to do for all time

    '''
    list_to_do = []
    what_have_done = []
    success = []
    failure = []
    for i in list_with_deeds:
        list_to_do.append(i[0])
        what_have_done.append(i[1])
        success.append(i[2])
        failure.append(i[3])
    function1 = pd.DataFrame({'TASK AND DAY': list_to_do, 'NUMBER OF TIMES': what_have_done, 'SUCCESS': success, 'FAILURE': failure }) 
    print(function1)
# all_time(read_file("Книга1.csv"))


def add_point(list_with_deeds):
    '''
    The function allows user to add 1 point when he have done task
    '''
    
    print("Choose a goal to add points(number):")
    num = input(">>> ")
    goal = today_goal().split("\n")[num-1]
    newres = []
    for i in list_with_deeds:
        if " ".join(i) == goal:
            newres.append(i)
    return 0

print(add_point(read_file("Книга1.csv")))

def today_goal():
    pass