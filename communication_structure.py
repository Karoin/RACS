from doosan_library import *
from setting import *

class Communication(Setting):
    def get_PTOR_data(self):
        _, self.raw_data = server_socket_read(self.plc_socket, length=-1, timeout=2)
        self.comm_state = server_socket_state(self.plc_socket)

    def split_and_decode(self):
        for i in range(len(self.PTOR_data)):
            j = i*2
            self.PTOR_data[i] = self.raw_data[j:(j+2)]
            self.PTOR_data[i] = int(self.PTOR_data[i], 16)

    def communication_check(self):
        if self.PTOR_data[0] & self.PTOR_dic['comm_connected']:
            self.comm_state = True
            print("Communication Successful!")
            self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['comm_connected']
        else:
            self.comm_state = False
            print("Communication Unsuccessful!")
            self.RTOP_data[0] = self.RTOP_data[0] & ~self.RTOP_dic['comm_connected']
            
    def vision_check(self):
        if self.comm_state:
            if self.PTOR_data[0] & self.PTOR_dic['connect_vision']:
                self.vis_state = True
                print("Vision Connection Successful!")
                self.RTOP_data[0] = self.RTOP_data[0] | self.RTOP_dic['vision_connected']
            else:
                self.vis_state = False
                print("Vision Connection Unsuccessful!")
                self.RTOP_data[0] = self.RTOP_data[0] & ~self.RTOP_dic['vision_connected']
        else:
            print("Communication Unsuccessful!")

    def IO_check(self):
        if self.comm_state:
            self.clamp_state = get_tool_digital_input(1)    # for future use
            self.btn_state = get_tool_digital_input(2)     # for future use
            if (self.PTOR_data[1] & self.PTOR_dic['clamp']) or (self.clamp_state):
                set_tool_digital_output(1, ON)
                print("Clamped!")
                self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['clamped']
            else:
                set_tool_digital_output(1, OFF)
                print("Unclamped!")
                self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['clamped']

            if (self.PTOR_data[1] & self.PTOR_dic['pushed']) or (self.btn_state):
                set_tool_digital_output(2, ON)
                print("Pushed!")
                self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['pushed']
            else:
                set_tool_digital_output(2, OFF)
                print("Unpushed!")
                self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['pushed']
        else:
            print("Communication Unsuccessful!")

    def holder_check(self):
        # COMBO
        if self.unclamp_combo == True:
            self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['unclamp_chademo_holder']
            self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['unclamp_combo_holder']
            print("Unclamp Combo Holder!")
        else:
            self.unclamp_combo = False
        # CHAdeMO
        if self.unclamp_chademo == True:
            self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['unclamp_combo_holder']
            self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['unclamp_chademo_holder']
            print("Unclamp CHAdeMO Holder!")
        else:
            self.unclamp_chademo = False

    def test_sensor_check(self):
        if self.comm_state:
            if self.PTOR_data[1] & self.PTOR_dic['combo_top_turned_on']:
                self.combo_test_completed = True
            else:
                self.combo_test_completed = False
            if self.PTOR_data[1] & self.PTOR_dic['combo_bottom_turned_on']:
                self.combo_test_failed = True


    def emergency_check(self):
        if self.PTOR_data[0] & self.PTOR_dic['emergency_pushed']:
            print("Emergency Pushed!")
            server_socket_close(self.plc_socket)
            exit()

    def position_check(self):
        if self.comm_state:
            self._current_position, _ = get_current_posx(ref=DR_BASE)
            if self.PTOR_data[1] & self.PTOR_dic['go_to_home_position']:
                self.home_positioned = True
                if self._current_position == posx(self.HOME_POSITION):
                    self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['wait_positioned']
                    self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['home_positioned']
            else:
                # RTOP_data will be handled in 'operation_structure'
                self.home_positioned = False
            if self.PTOR_data[1] & self.PTOR_dic['go_to_wait_position']:
                self.wait_positioned = True
                if self._current_position == posx(self.WAIT_POSITION):
                    self.RTOP_data[1] = self.RTOP_data[1] & ~self.RTOP_dic['home_positioned']
                    self.RTOP_data[1] = self.RTOP_data[1] | self.RTOP_dic['wait_positioned']
            else:
                # RTOP_data will be handled in 'operation_structure'
                self.wait_positioned = False
        else:
            print("Communication Unsuccessful!")

    def command_check(self):
        if self.comm_state:
            if self.PTOR_data[3] & self.PTOR_dic['wait']:
                self.wait = True
            else:
                self.wait = False
            if self.PTOR_data[3] & self.PTOR_dic['start_charging']:
                self.start = True
            else:
                self.start = False
            if self.PTOR_data[3] & self.PTOR_dic['finish_charging']:
                self.finish = True
            else:
                self.finish = False
            if self.PTOR_data[3] & self.PTOR_dic['recover']:
                self.recover = True
            else:
                self.recover = False
        else:
            print("Communication Unsuccessful!")

    def charging_type_check(self):
        if self.comm_state:
            if self.PTOR_data[5] & self.PTOR_dic['grasp_combo']:
                self.combo_state = True
            else:
                self.combo_state = False
            if self.PTOR_data[5] & self.PTOR_dic['grasp_chademo']:
                self.chademo_state = True
            else:
                self.chademo_state = False
        else:
            print("Communication Unsuccessful!")

    def encode_and_merge(self):
        self.encodedRTOP_data = b''
        for i in range(len(self.PTOR_data)):
            self.PTOR_data[i] = str(hex(self.PTOR_data[i]))
            self.PTOR_data[i] = self.PTOR_data[i][2:].encode()
            self.encodedRTOP_data += self.PTOR_data[i]

    def send_RTOP_data(self):
        server_socket_write(self.plc_socket, self.encodedRTOP_data)

    def reset_data(self):
        self.RTOP_data = [0 for _ in range(8)]
