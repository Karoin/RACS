from test_running import robot_communication

def tool_type(self):
    if self.robot_communication.PTOR_data[5] == '0x20':
        self.set_tool(chademo)
        self.robot_communication.RTOP_data[5] = '0x08'
    elif self.robot_communication.PTOR_data[5] == '0x10':
        self.set_tool(combo)
        self.robot_communication.RTOP_data[5] = '0x04'
    else: print("Fail to Charging type!")

def disconnnet_type(self):
    if self.robot_communication.PTOR_data[5] == '0x20':
        self.sub_program_run(Chademo_Disconnect)
        self.robot_communication.RTOP_data[5] = '0x20'
    elif self.robot_communication.PTOR_data[5] == '0x10':
        self.sub_program_run(combo_Disconnect)
        self.robot_communication.RTOP_data[5] = '0x10'
    else: print("Fail to Disconnect type!")


if self.robot_communication.PTOR_data[3] == '0x04': # 충전 종료 데이터 받음(PTOR)
    self.robot_communication.RTOP_data[3] = '0x04'
    self.robot_communication.RTOP_data[5] == '0x'
        

                # 충전 종료 동작 했다는 데이터 보냄
    # 티칭으로 충전건 앞까지 이동(티칭)
    set_ref_coord(DR_TOOL)                      # 로봇 좌표계를 툴 좌표계로 변경
    vision_socket()                             # vision 통신 연결
                                            # 이동 완료후 비젼에 데이터 보냄(?, 연결해제 준비 완료 신호(위치 도착))
    #Vision_Work()                              # 비젼 동작 함수 호출
                                            # 충전건 잡는위치까지 비젼데이터로 이동
    if robot_communication.PTOR_data[0] == '0x04':      # 클램프 데이터를 받음
        set_tool_digital_output(1, ON)          # 클램프 ON
        robot_communication.RTOP_data[1] = '0x04'
    wait(1.0)
    tool_type()                                 # tool 타입 별 툴 무게 설정
    wait(0.5)
    task_compliance_ctrl()                      # 순응제어 명령 건이 충전구에서 움직이는 동안 멈추지 않도록
    release_compliance_ctrl()                   
    set_stiffnessx([3000,3000,3000,200,200,200], time=3)                            # 안에 있는 숫자는 기본값([3000,3000,3000,200,200,200]) 차후 수정요망
    set_desired_forec([0,0,-200,0,0,0],[0,0,1,0,0,0],time=1, DR_FC_MOD_REL)         # 기본값(Fd=[0,0,0,0,0,0]) 힘성분 3개, 모멘트 성분 3개, 기본값(dir=[0,0,0,0,0,0]) 1이면 해당방향 힘제어 0이면 해당 방향 compliance 제어, time=힘증가시키는데 소요 시간, 
    release_force(1)                            # 충전건 집고 빠지는 동작(포스 이용,티칭) 
    set_ref_coord(DR_BASE)                      # 로봇 좌표계를 베이스 좌표계로 변경
    # 충전건을 다시 거치대 위치로 이동(티칭)
    disconnnet_type()
    if robot_communication.PTOR_data[0] == '0x04':  # 클램프 데이터를 받음
        set_tool_digital_output(1, OFF)          # 충전건 클램프 OFF                                            
    set_tool(normal)                          # 툴 무게 변경(충전건 잡지 않았을 경우(normal))
    # 충전건 거치 위치에서 빠지고 홈포지션으로 이동.(티칭)
                                            # 충전 종료 완료했다는 데이터 보냄(RTOP)

else :
     print("Fail to Robot Disconnect!")




# def Vision_Work():
#    # 비전 데이터 받아서 움직임(비젼 데이터를 받는 명령어,비젼 데이터를 통해 움직이는 명령어, 위치 도작했다는 신호 받음)
#    vs_set_info(DR_VS_CUSTOM)              # 비젼 종류 설정
#    vs_connect(ip_addr,port_num=9999)      # 비젼 연결 명령어(IP주소와, 포트 넘버 필요)
#    vs_request(1)                          # 검출해야하는 물체 개수 (1개)
#    Vision_result()                        # 비젼 측정결과 정보 가져오기
#                                           # 측정결과로 로봇움직이는 명령어
#                                           # 위치도착 신호 보냄(VTOR)
#                                           # 클램프로 충전건 집음(클램프 동작시키는 명령어, 티칭?)  3번 트라이 하고 못잡을경우 홈으로 이동.
#    set_tool(type)                         # 툴무게 변경(충전건 잡았을경우, type = chademo, combo)
#    vs_disconnect()                        # 비젼 연결 해제                  
# def Vision_result():                      # 비젼으로부터 측정결과 정보 가져오는 명령어
#    cnt, result = vs_result()
#    for i in range(cnt):
#        x = result[i][0]                    # x=x좌표
#        y = result[i][1]                    # y=y좌표
#        t = result[i][2]                    # t=회전값
#        tp_popup("x={0},y={1},t={2}".format(result[i][0],result[i][1],result[i][2]),DR_PM_MESSAGE)