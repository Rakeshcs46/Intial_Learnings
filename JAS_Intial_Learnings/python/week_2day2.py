#Topics for today  String Functions 

# import re
#
#
# input_str = "mom"
# reversed_str = input_str[::-1]
#
# if input_str == reversed_str:
#     print("The entered string is symmetrical")
# else:
#     print("The entered string is not symmetrical")
#
# if re.match("^(\w+)\Z", input_str) and input_str == input_str[::-1]:
#     print("The entered string is palindrome")
# else:
#     print("The entered string is not palindrome")
#
#
# import datetime,time
#
# first = input("Enter the first time in military hours:")
# second = input( "Enter the second time in military hours:")
# first_t= datetime.time(hour=int(first[0:2]), minute=int(first[2:4]))
# second_t= datetime.time(hour=int(second[0:2]), minute=int(second[2:4]))
# hour = ( second.hour-first.hour )
# minute= (second.hour-first.hour)
# fmt = ("%H ,%M")
# print (first_t.strftime(fmt) , second_t.strftime(fmt))
#
#
#
# def time_diference(time1, time2):
#     hour_change = abs(int(time1[:2]) - int(time2[:2]))
#     minute_change = int(time2[2:]) - int(time1[2:])
#     # Change hours to equivalent minutes so you're really comparing apples to apples
#     total_minute_change = hour_change * 60 + minute_change
#     return total_minutes_change
#
# def print_time(minute_difference):
#     # Display the answer back to the user
#
# print_time(time_difference(first, second))
