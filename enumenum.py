from enum import Enum #must import Enum to use enum

#declare enum using class
class TDays(Enum) :
    MONDAY = 1 #Order of values
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

#to print
print(TDays.MONDAY) #will print Tdays.MONDAY
print(TDays.FRIDAY) #will print Tdays.FRIDAY