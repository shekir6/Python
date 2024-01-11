# FIRST SOLUTION
speed = float(input())

if speed <= 10:
    print('slow')
elif speed <= 50:
    print('average')
elif speed <= 150:
    print('fast')
elif speed <= 1000:
    print('ultra fast')
else:
    print('extremely fast')  

#SECOND SOLUTION

speed = float(input())

if speed <= 10:
    message = "slow"
elif speed <= 50:
    message = "average"
elif speed <= 150:
    message = "fast"
elif speed <= 1000:
    message = "ultra fast"
else:
    message = "extremely fast"

print(message)
    
          