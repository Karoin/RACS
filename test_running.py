from communication_structure import Communication
from operation_structure import Operation
from doosan_library import *
from setting import *

robot_communication = Communication()
robot_operation = Operation()

# 1st - COMMUNICATION
first_thread = thread_run(updating, loop=True)
# 2nd - EMERGENCY CHECK
second_thread = thread_run(robot_communication.emergency_check, loop=True)

def updating():
    robot_communication.get_PTOR_data()
    robot_communication.split_and_decode()
    robot_communication.communication_check()
    robot_communication.vision_check()
    robot_communication.IO_check()
    robot_communication.holder_check()
    robot_communication.position_check()  # Done without udpates from 'Operation'
    robot_communication.command_check()   # Done without udpates from 'Operation'
    robot_communication.charging_type_check() # Done without udpates from 'Operation'
    robot_communication.encode_and_merge()
    robot_communication.send_RTOP_data()
    robot_communication.reset_data()

set_tool(normal)

# 로봇 동작 관련
while True:
    pass
