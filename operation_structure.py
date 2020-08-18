from communication_structure import Communication
from doosan_library import *
from setting import *

class Operation(Communication):
    def do_go_to_home_position(self):
        if self.home_positioned == True:
            stop(DR_HOLD)   # is needed?
            movel(posx(self.HOME_POSITION), time=3)
            self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['wait_positioned']
            self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['home_positioned']

    def do_go_to_wait_position(self):
        if self.wait_positioned == True:
            movel(posx(self.WAIT_POSITION), time=3)
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
            movel(self.combo_grasping_pos1) # turn around from home position
            movel(self.combo_grasping_pos2) # approach1
            movel(self.combo_grasping_pos3) # approach2
            movel(self.combo_grasping_pos4) # apporach3 right in front of gun
            set_tool_digital_output(1, ON)  # unclamp
            movel(self.combo_grasping_pos5) # approach4 to clamp
            set_tool_digital_output(1, OFF) # clamp
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
        
    def do_grasp_chademo(self):
        self.chademo_grasped = False
        if self.chademo_state == True:
            # 영민 will teach the robot and its position will be passed by Global_variables.
            movel(self.chademo_grasping_pos1) # turn around from home position
            movel(self.chademo_grasping_pos2) # approach1
            movel(self.chademo_grasping_pos3) # approach2
            movel(self.chademo_grasping_pos4) # apporach3 right in front of gun
            set_tool_digital_output(1, ON)  # unclamp
            movel(self.chademo_grasping_pos5) # approach4 to clamp
            set_tool_digital_output(1, OFF) # clamp
            set_tool(chademo)   # tool weight adapted
            self.unclamp_chademo = True
            wait(5)
            if self.PTOR_data[0] | self.PTOR_dic['chademo_holder_unclamped']:
                movel(self.chademo_grasping_pos6) # horizontally backing in 
            else:
                exit()
            self.RTOP_data[5] = self.RTOP_data[5] & ~self.RTOP_dic['combo_grasped']
            self.RTOP_data[5] = self.RTOP_data[5] | self.RTOP_dic['chademo_grasped']
            self.chademo_grasped = True

    def do_combo_test(self):
        self.combo_test_completed = False
        if self.combo_grasped == True:
            movel(self.combo_test_pos1)
            movel(self.combo_test_pos2)

            pass

    def do_chademo_test(self):
        self.chademo_test_completed = False
        if self.chademo_grasped == True:
            pass

    def do_release_combo(self):
        set_tool(normal)

    def do_release_chademo(self):
        set_tool(normal)


    