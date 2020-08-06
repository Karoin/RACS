from communication_structure import Communication
from operation_structure import Operation
from doosan_library import *
from setting import *


robot_communication = Communication()
robot_operation = Operation()
first_thread = thread_run(updating, loop=True)

#def Vision_Work():
#    # 비전 데이터 받아서 움직임(비젼 데이터를 받는 명령어,비젼 데이터를 통해 움직이는 명령어, 위치 도작했다는 신호 받음)
#    vs_set_info(DR_VS_CUSTOM)              # 비젼 종류 설정
#    vs_connect(ip_addr,port_num=9999)      # 비젼 연결 명령어(IP주소와, 포트 넘버 필요)
#    vs_request(1)                          # 검출해야하는 물체 개수 (1개)
#    Vision_result()                        # 비젼 측정결과 정보 가져오기
#                                           # 측정결과로 로봇움직이는 명령어
#                                           # 위치도착 신호 보냄(VTOR)
#                                           # 클램프로 충전건 집음(클램프 동작시키는 명령어, 티칭?)  3번 트라이 하고 못잡을경우 홈으로 이동.
#    set_tool(type)                         # 툴무게 변경(충전건 잡았을경우, type = chademo, combo, normal)
#    vs_disconnect()                        # 비젼 연결 해제                  

#def Vision_result():                        # 비젼으로부터 측정결과 정보 가져오는 명령어
#    cnt, result = vs_result()
#    for i in range(cnt):
#        x = result[i][0]                    # x=x좌표
#        y = result[i][1]                    # y=y좌표
#        t = result[i][2]                    # t=회전값
#        tp_popup("x={0},y={1},t={2}".format(result[i][0],result[i][1],result[i][2]),DR_PM_MESSAGE)      

# 충전 종료 데이터를 받음(PTOR),로봇 상태 보냄(포지션 위치나 동작 여부 확인)(RTOP)


plc_socket()                                # plc 통신 연결
updating()                                  # plc 통신 하여 데이터 받음
                                            # 충전 종료 포지션으로 로봇 이동후 PLC로부터 동작 시작 데이터 받음(PTOR)
                                            # 충전 종료 동작 했다는 데이터 보냄
                                            # 티칭으로 충전건 잡은후 재대로 연결됬는지 확인하는 동작까지(티칭)
set_tool(type)                              # 툴 무게 변경(충전건 잡을 경우, type = chademo, combo, normal)
vission_socket()                            # vision 통신 연결
                                            # 이동 완료후 비젼에 데이터 보냄(?, 디스커넥트 준비 완료(?))
set_ref_coord(DR_TOOL)                      # 로봇 좌표계를 툴 좌표계로 변경
#Vision_Work()                              # 비젼 동작 함수 호출
                                            # 충전건 잡는위치까지 비젼데이터로 이동
                                            # 클램프 데이터를 받음
                                            # 충전건 클램프 on(티칭) 
set_tool(type)                              # 툴 무게 변경(충전건 놓았을경우(normal), type = chademo, combo, normal)
task_compliance_ctrl()                      # 순응제어 명령 건이 충전구에서 움직이는 동안 멈추지 않도록
release_compliance_ctrl()                   
set_stiffnessx([3000,3000,3000,200,200,200], time=3)                            #안에 있는 숫자는 기본값 차후 수정요망
set_desired_forec([0,0,-200,0,0,0],[0,0,1,0,0,0],time=1,DR_FC_MOD_REL)         #Fd=[0,0,0,0,0,0] 기본값 힘성분 3개, 모멘트 성분 3개, dir=[0,0,0,0,0,0] 기본값 1이면 해당방향 힘제어 0이면 해당 방향 compliance 제어, time=힘증가시키는데 소요 시간, 
release_force(1)                            # 충전건 집고 빠지는 동작(포스 이용,티칭) 


set_ref_coord(DR_BASE)                      # 로봇 좌표계를 베이스 좌표계로 변경
                                            # 충전건을 다시 거치대 위치로 이동(티칭)
                                            # 충전건 클램프 off(티칭)
set_tool(type)                              # 툴 무게 변경(충전건 놓았을경우(normal), type = chademo, combo, normal)
                                            # 충전건 거치 위치에서 빠지고 홈포지션으로 이동.(티칭)
                                            # 충전 종료 완료했다는 데이터 보냄(RTOP)








def get_current_position(self):
        self.currentPos, _ = get_current_posx(ref=DR_BASE)
        if self.currentPos == posx(self.home_position):
            self.outData = 1

        elif self.currentPos == posx(self.wait_position):
            self.outData = 1