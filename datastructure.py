''' COMMUNICATION '''

# Dataframe
'''
The integer number, 'x' in 'range(x)' can be changed to 
any number if you want to resize the data frame of each client.
'''
plcDataList = [0 for _ in range(8)]
myStatus = [0 for _ in range(8)]
visDataList = [0 for _ in range(20)]

# Robot Motion(Position Segment)
motion = {
    'homePos': 10,
    'waitPos': 20,
    'combo': 30,
    'chademo': 31,
    'plugIn': 40,
    'plugOut': 50,
    'visionCheck': 60, # what's this?
    'moving': 100,
    'recovering': 150,
}

# PLC <--> Robot Interface Map


defaultPos = (0,0,0,0,0,0)

print(type(defaultPos))
print(defaultPos)