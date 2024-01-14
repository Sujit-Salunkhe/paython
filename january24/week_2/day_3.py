time ='12:01:00AM'

# print(time[-2])

# if time[-2] == "P":
#     if time[0] == "1" and time [1] == '2':
#             return 
    

def convert_To_24(timer):
    if time[-2] == "P":
        if time[0] == "1" and time [1] == '2':
            return timer[:8]
        else:
            a = int(time[0] + time[1])
            # print(timer[2:8])
            timer_24 = 12 + a
            return str(timer_24) + timer[2:8]
    else:
        if time[0] == "1" and time [1] == '2':
            return '00'+timer[2:8]
        else:
            return timer[:8]
  
        
        
print(convert_To_24(time))  
            