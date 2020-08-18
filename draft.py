from datastructure import *

PLC_PORT = 20002
VISION_PORT = 20003


# defaultPos = [0, 0, 0, 0, 0, 0]

plcSocket = server_socket_open(PLC_PORT)
visSocket = server_socket_open(VISION_PORT)

def read_data():
    '''
    CHANGES TO BE MADE:
    length / data type of 'plcData' / vision data handling.. / VISION_PORT / 
    '''
    if server_socket_state(plcSocket) == 1:
        plcDataLength, plcData = server_socket_read(plcSocket, length=-1, timeout=1)
        if plcData != None:
            position, movement, chargingType, connection = convert_data(plcData)
            update_data(plcDataList, index=0, plcData)

    if server_socket_state(visSocket) == 1:
        visDataLength, visData = server_socket_read(visSocket, length=-1, timout=1)
        if visData != None:
            update_data(visDataList, index=0, visData)

def convert_data(data):
    position = data[0:2]
    movement = data[2:5]
    chargingType = data[5:7]
    connection = data[7:9]
    return position, movement, chargingType, connection

def send_data():    # to PLC
    if server_socket_state(plcSocket) == 1:
        server_socket_write(plcSocket, myStatus[0])

# Thread done -- reading only
comThID = thread_run(read_data, loop=True)

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

def decide_motion():
    pass

def plug_in():
    # 충전기 앞까지 티칭하고....
    while plcDataList[0] == motion.get('plugIn'):
        # 업데이트 되고 있는 비젼데이터를 받아서..
        update_data(myStatus, 0, motion.get('plugIn'))
    



server_socket_close(socket)



# ex) 
def update_data(data, list, index=0, length=1):
    for i in range(length):
        list[i] = data
