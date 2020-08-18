# Socket Communication Setting - as SERVER


PORT = 50000
socket = server_socket_open(PORT)
txData = b"33b0a"

socket_state = server_socket_state(socket)
if socket_state:
    tp_popup("TCP/IP has opened.")
else:
    tp_popup("TCP/IP has not opened")

server_socket_write(socket, txData)

rxLength, rxData = server_socket_read(socket, length=-1, timeout=3)
if rxLength == 0:
    tp_popup("Data length: {}\n Data received: {}" .format(rxLength, rxData))

if server_socket_close(socket) == False:
    tp_popup("TCP/IP has closed.")