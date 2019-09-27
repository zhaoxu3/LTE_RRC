from ixv import wv          # import the Ixia IoT Golden AP (wv) module from ixv
from Run_Ap_Test import *
from Get_Para import *
# Connect to the chassis and reserve a port, then store the resulting port name
# Get ie_elements(Beacon;Probe Response;Authentication Response;Associate Response;)
dictlist = []                                                   #ie_element para config
pathlist =[ r'E:\AP_Grap_analyse\Beacon analyse.xls',r'E:\AP_Grap_analyse\Probe Rsp analyse.xls',r'E:\AP_Grap_analyse\Auth Rsp analyse.xls',r'E:\AP_Grap_analyse\Assoc Rsp analyse.xls']
for i in range(4):
    start_row = 12
    while start_row<237:
        print(start_row)
        str = read_excel(pathlist[i],'2.4g_11n',start_row,3)
        if str == '':
           pass
        else:
            dictlist.append(Excel_handle(pathlist[i],str,""))
        start_row = start_row + 1
timeout = 240
test_chassis = '192.168.1.1'
test_port = '2.1'
test_channel = 3
bss = dict(bss='MyBss')
port = wv.port.setup(chassis=test_chassis, slot=test_port, channel=test_channel)
print "Reserved - ", port
ap_24g11n_config = {
  'bssid': '00:13:e9:12:44:55',
  'beacon_interval': 100,
  'ssid': 'ASUS RT-AC66U',
  'phy_type': '11n',
  'ie_elements':dictlist
}
wv.bss.setup(port, bss, config=ap_24g11n_config)  # Here's an example of mixing dictionary arguments with a keyword argument
print "config ok"
wv.bss.activate(bss)
print "activate ok"
device = wv.bss.wait_for_device(bss, timeout_seconds=timeout)
wv.port.download_capture(port, file="capture")
wv.bss.deactivate(bss)
time.sleep(2)
wv.port.release(port)
"""
def ap_tester(ap_config):
    
    Takes a dictionary for the AP config and the dictionary for the Test parameters.
    outlines the sequence of the script.
    setup the port, activate the AP and connect up, run trials, teardown.
    
    ap_setup(port, ap_24g11n_config)
    save_capture=1
    ap_teardown(port, save_capture)
    return "pass"
print "Test Start2_4G"
ap_tester()
print "Test Start5G"
ap_tester()
"""
