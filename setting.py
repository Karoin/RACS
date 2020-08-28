from doosan_library import *

class Setting:
  # Position setting
  HOME_POSITION = [0, 0, 0, 0, 0, 0]
  WAIT_POSITION = [0, 0, 0, 0, 0, 0]
  # Data setting
  PTOR_data = [0 for _ in range(8)]
  RTOP_data = [0 for _ in range(8)]
  # Default setting -- assign variables ahead for your readability
  DEFAULT = None                             # Default Value
  raw_data = encodedRTOP_data = None
  comm_state = vis_state = clamp_state = btn_state = unclamp_state = unbtn_state = None
  wait = start = finish = recover = None
  _current_position = None                   # Current position of robot used only in that function
  home_positioned = wait_positioned = None
  unclamp_combo = unclamp_chademo = None     # SIGNAL: ROBOT -> PLC
  combo_grasped = chademo_grasped = None     # Value to confirm whether grasping CHAdeMO is carried out successfully
  combo_test_completed = chademo_test_completed = None
  combo_test_failed = chademo_test_failed = None
  combo_state = chademo_state = None
  combo_top = combo_bottom = chademo_top = chademo_bottom = None  # Sensor status from PLC

  # Combo Grasping
  combo_grasping_pos1 = Global_g_combo1
  combo_grasping_pos2 = Global_g_combo2
  combo_grasping_pos3 = Global_g_combo3
  combo_grasping_pos4 = Global_g_combo4
  combo_grasping_pos5 = Global_g_combo5
  combo_grasping_pos6 = Global_g_combo6
  # CHAdeMO Grasping
  chademo_grasping_pos1 = Global_g_chademo1
  chademo_grasping_pos2 = Global_g_chademo2
  chademo_grasping_pos3 = Global_g_chademo3
  chademo_grasping_pos4 = Global_g_chademo4
  chademo_grasping_pos5 = Global_g_chademo5
  chademo_grasping_pos6 = Global_g_chademo6
  # Combo Test
  combo_test_pos1 = Global_t_combo1
  combo_test_pos2 = Global_t_combo2
  combo_test_pos3 = Global_t_combo3
  combo_test_pos4 = Global_t_combo4
  combo_test_pos5 = Global_t_combo5
  combo_test_pos6 = Global_t_combo6
  # CHAdeMO Test
  chademo_test_pos1 = Global_t_chademo1
  chademo_test_pos2 = Global_t_chademo2
  chademo_test_pos3 = Global_t_chademo3
  chademo_test_pos4 = Global_t_chademo4
  chademo_test_pos5 = Global_t_chademo5
  chademo_test_pos6 = Global_t_chademo6
  # 
  # Basic Assigments 
  PTOR_dic = {
    'manual': 0x01, 'auto': 0x02, 'teach': 0x04, 'remote': 0x08, 'play': 0x10,              #0
    'cycle_start': 0x01, 'hold': 0x02, 'servo_on': 0x04, 'emergency_stop': 0x08, 'alram_reset': 0x10, 'robot_running': 0x20,                            #1, 정수로 보내야함
    'vision_calibration': 1, 'combo': 2, 'chademo': 3,                                      #2, 정수로 보내야함
    'home_position_start': 1, 'wait_position_start': 2, 'robot_recovery_start': 3, 'gun_check_start': 4, 'gun_return_start': 5, 'charger_start': 6, 'discarger_start': 7, 'calibration_start': 8,           #3, 정수로 보내야함
    'clamp_unit_clamped':0x01, 'clamp_unit_unclamped': 0x02, 'gun_check_ok': 0x04, 'gun_check_ng': 0x08, 'gun_docking_completed': 0x10,                 #4
  }

  RTOP_dic = {
    'teach': 0x04, 'remote': 0x08, 'play': 0x10,                                            #0
    'cycle_start': 0x01, 'hold': 0x02, 'servo_on': 0x04, 'emergency_stop': 0x08, 'alram_reset': 0x10, 'robot_running': 0x20,                            #1, 정수로 보내야함
    'vision_calibration': 1, 'combo': 2, 'chademo': 3,                                      #2, 정수로 보내야함
    'home_position': 1, 'wait_position': 2, 'robot_recovery': 3, 'gun_check': 4, 'gun_return': 5, 'charger': 6, 'discarger': 7, 'calibration': 8,           #3, 정수로 보내야함
    'clamp_unit_clamp_request':0x01, 'clamp_unit_unclamp_request': 0x02,                    #4                        
  }




    
    # # Basic Assigments 
    # PTOR_dic = {
    #     'comm_connected': 0x01, 'connect_vision': 0x02, 'emergency_pushed': 0x80,               #0
    #     'nomal': 1, 'emergency_Stop': 2, 'vision_error': 3,                            #1, 정수로 보내야함
    #     'combo_holder_clamp': 0x01, 'combo_holder_unclamped': 0x02, 'chademo_holder_clamped': 0x04, 'chademo_holder_unclamped': 0x08,               #2
    #     'combo_top_turned_on': 0x10, 'combo_bottom_turned_on': 0x20, 'chademo_top_turned_on': 0x40, 'chademo_bottom_turned_on': 0x80,               #2
    #     'test_mode':0x01, 'auto_mode': 0x02,                                                    #4
    #     'grasp_combo': 0x01, 'grasp_chademo': 0x02,                                             #5
    #     #'test_combo': 0x10, 'test_chademo': 0x20,                                              #5
    #     'wait': 1, 'go_to_wait_position': 2,'go_to_home_position': 3, 'start_charging': 4, 'finish_charging': 5, 'recover': 6,    #6, 정수로 보내야함
    #     'test_complete': 1,                                                                  #7, 정수로 보내야함
        
    
    # }
    # RTOP_dic = {
    #     'comm_connected': 0x01, 'vision_connected': 0x02, 'emergency_pushed': 0x80,             #0
    #     'nomal': 1, 'emergency_stop': 2, 'vision_error': 3,                              #1, 정수로 보내야함
    #     'clamped': 0x01, 'unclamped': 0x02, 'pushed': 0x04, 'unpushed': 0x08,                   #2                              
    #     'test_mode': 0x01, 'auto_mode': 0x02,                                                   #4
    #     'combo': 0x01, 'chademo': 0x02,                                         #5
    #     'waiting': 1, 'holder_clamp_request': 2, 'holder_unclamp_request': 3, 'request_to_check_test_sensor': 4,                        #6, 정수로 보내야함
    #     #'charging': 0x02, 'finished_charging': 0x04, 'recovered': 0x08,        
    #     #'combo_tested': 0x10, 'chademo_tested': 0x20,                                          
    #     'motion_complete': 1, 'wait_positioned': 2, 'home_positioned': 2                        #7, 정수로 보내야함
    # }
    # Communication setting
  PLC_PORT = 50000
    # VISION_PORT = 60000
    # Open Ports
  plc_socket = server_socket_open(PLC_PORT)

    
    # Open it later.....
    # vission_socket = server_socket_open(VISION_PORT)
