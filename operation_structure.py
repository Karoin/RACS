from communication_structure import Communication
from doosan_library import *
from setting import *

class Operation(Communication):
  def do_go_to_home_position(self):
    if self.home_positioned == True:
      self.PTOR_data[6] = self.PTOR_data[6] & self.PTOR_data['home_positioned']
      stop(DR_HOLD)   # is needed?
      movej(posx(self.HOME_POSITION), time=3)
      self.RTOP_data[7] = self.RTOP_data[7] & ~self.RTOP_dic['wait_positioned']
      self.RTOP_data[7] = self.RTOP_data[7] | self.RTOP_dic['home_positioned']

  def do_go_to_wait_position(self):
    if self.wait_positioned == True:
      movej(posx(self.WAIT_POSITION), time=3)
      self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['home_positioned']
      self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['wait_positioned']

  def do_wait(self):
    if self.PTOR_data[3] & self.PTOR_dic['wait']:
      pass
    if self.wait == True:
      self.RTOP_data[3] & self.RTOP_dic['waiting']

  def do_start_charging(self):
    if self.start == True:
      self.do_grasp_combo()
      self.do_grasp_chademo()
      self.do_combo_test()
      self.do_chademo_test()

  def do_finish_charging(self):
    pass

  def do_recover(self):
    pass

  def do_grasp_combo(self):
    self.combo_grasped = False
    if self.combo_state == True:
      # 영민 will teach the robot and its position will be passed by Global_variables.
      movej(self.combo_grasping_pos1) # turn around from home position
      movej(self.combo_grasping_pos2) # approach1
      movej(self.combo_grasping_pos3) # approach2
      movej(self.combo_grasping_pos4) # apporach3 right in front of gun
      set_tool_digital_output(2, ON)  # unclamp
      movej(self.combo_grasping_pos5) # approach4 to clamp
      set_tool_digital_output(2, OFF) # clamp
      a = 0
      while a < 5:
        a = a+1
        set_tool_digital_output(2, ON)
        wait(0.5)
        set_tool_digital_output(2, OFF)
        wait_tool_digital_input(4, ON)
        if get_tool_digital_input(4) == ON:
          set_tool(combo)   # tool weight adapted
          self.unclamp_combo = True
          wait(5)
          if self.PTOR_data[0] | self.PTOR_dic['combo_holder_unclamped']:
            movel(self.combo_grasping_pos6) # horizontally backing in 
        else:
        	exit()
        self.RTOP_data[5] = self.RTOP_data[5] & ~self.RTOP_dic['chademo_grasped']
        self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['combo_grasped']
        self.combo_grasped = True
        break
    else:
      set_tool_digital_output(2, ON)
      movej(self.combo_grasping_pos4)
      movej(self.combo_grasping_pos3) # approach2
      movej(self.combo_grasping_pos2)
      movej(self.combo_grasping_pos1)
      movej(posx(self.WAIT_POSITION), time=3)
      self.RTOP_data[7] = self.RTOP_data[7] & ~self.RTOP_dic['home_positioned']
      self.RTOP_data[7] = self.RTOP_data[7] | self.RTOP_dic['wait_positioned']
            
  def do_grasp_chademo(self):
    self.chademo_grasped = False
    if self.chademo_state == True:
      # 영민 will teach the robot and its position will be passed by Global_variables.
      movej(self.chademo_grasping_pos1) # turn around from home position
      movej(self.chademo_grasping_pos2) # approach1
      movej(self.chademo_grasping_pos3) # approach2
      movej(self.chademo_grasping_pos4) # apporach3 right in front of gun
      set_tool_digital_output(2, ON)  # unclamp
      movej(self.chademo_grasping_pos5) # approach4 to clamp
      set_tool_digital_output(2, OFF) # clamp
      a = 0
      while a < 5:
        a = a+1
        set_tool_digital_output(2, ON)
        wait(0.5)
        set_tool_digital_output(2, OFF)
        wait_tool_digital_input(4, ON)
        if get_tool_digital_input(4) == ON:
          set_tool(chademo)   # tool weight adapted
          self.unclamp_chademo = True
          wait(5)
          if self.PTOR_data[0] | self.PTOR_dic['chademo_holder_unclamped']:
            movel(self.chademo_grasping_pos6) # horizontally backing in 
        else:
          exit()
        self.RTOP_data[5] = self.RTOP_data[5] & ~self.RTOP_dic['combo']
        self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['chademo']
        self.chademo_grasped = True
        break
    else:
      set_tool_digital_output(2, ON)
      movej(self.chademo_grasping_pos4)
      movej(self.chademo_grasping_pos3) # approach2
      movej(self.chademo_grasping_pos2)
      movej(self.chademo_grasping_pos1)
      movej(posx(self.WAIT_POSITION), time=3)
      self.RTOP_data[7] = self.RTOP_data[7] & ~self.RTOP_dic['home_positioned']
      self.RTOP_data[7] = self.RTOP_data[7] | self.RTOP_dic['wait_positioned']
            

  def do_combo_test(self):
    self.RTOP_data[5] = self.RTOP_data[5] & self.RTOP_dic['combo'] == True
    self.combo_test_completed = False
    if set_tool(combo) == True:
      movej(self.combo_test_pos1)
      movej(self.combo_test_pos2)
      movej(self.combo_test_pos3)
      self.RTOP_data[6] = self.RTOP_data[6] & self.RTOP_dic['request_to_check_test_sensor']
      pass

  def do_chademo_test(self):
    self.RTOP_data[5] = self.RTOP_data[5] & self.RTOP_dic['chademo'] == True
    self.chademo_test_completed = False
    if self.chademo_grasped == True:
      pass

  # def do_release_combo(self):
  #   set_tool(normal)
  #   pass

	# def do_release_chademo(self):
  #   set_tool(normal)
  #   pass


    