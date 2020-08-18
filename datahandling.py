


# COMMUNICATION

def read_data():
    '''
    CHANGES TO BE MADE:
    length / data type of 'plcData' / vision data handling.. / VISION_PORT / 
    '''
    if server_socket_state(plcSocket) == 1:
        plcDataLength, plcData = server_socket_read(plcSocket, length=-1, timeout=1)
        if plcData != None:
            plcDataList[FIRST] = plcData
    if server_socket_state(visSocket) == 1:
        visDataLength, visData = server_socket_read(visSocket, length=-1, timout=1)
        if visData != None:
            visDataList[FIRST] = visData

def dataConversion():
    pass    # if needed.
