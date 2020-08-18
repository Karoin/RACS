# Modbus 신호 등록은 터치 팬던트에서 선언하여 소스로 불러 올것.
#   def modbus_connect(self):
#     self.add_signal = add_modbus_signal("192.168.1.111", prot = 502, name = "rbase_x", reg_type = DR_MODBUS_REG_INPUT, index=0)
class Vision_Modbus:
    def RBase_position(self):                    #address는 128~255까지 사용가능
        #res, val_list = get_modubs_inputs_list(iobus_list=["rbase_x", "rbase_y", "rbase_z", "rbase_a", "rbase_b", "rbase_c"])
        self.rbase_x = get_modbus_slave(128)
        self.rbase_y = get_modbus_slave(129)
        self.rbase_z = get_modbus_slave(130)
        self.rbase_a = get_modbus_slave(131)
        self.rbase_b = get_modbus_slave(132)
        self.rbase_c = get_modbus_slave(133)

    def RTcp_position(self):
        self.rtcp_x = get_modbus_slave(134)
        self.rtcp_y = get_modbus_slave(135)
        self.rtcp_z = get_modbus_slave(136)
        self.rtcp_a = get_modbus_slave(137)
        self.rtcp_b = get_modbus_slave(138)
        self.rtcp_c = get_modbus_slave(139)

    def RLine_position(self):
        self.rline_x = get_modbus_slave(140)
        self.rline_ag = get_modbus_slave(141)
        


    def vision_position(self):
        self.rbase_pos = "[rbase_x, rbase_y, rbase_z, rbase_a, rbase_b, rbase_c]"
        self.rtcp_pos = "[rtcp_x, rtcp_y, rtcp_z, rtcp_a, rtcp_b, rtcp_c]"

    
