from ixv import wv          # import the Ixia IoT Golden AP (wv) module from ixv
import time
# Connect to the chassis and reserve a port, then store the resulting port name
timeout = 240
test_chassis = '192.168.1.1'
test_port = '2.1'
test_channel = 3
bss = dict(bss='MyBss')
port = wv.port.setup(chassis=test_chassis, slot=test_port, channel=test_channel)
print "Reserved - ", port
#**********************************参数设置**************************************

def ap_setup(port, ap_config):
    """
    Turn on the AP and wait for the client to connect
    if client doesnt connect up within timeout, throw an exception
    Return the device dictionary of the connected devices
    """
    wv.bss.setup(port, bss, config=ap_config) # Here's an example of mixing dictionary arguments with a keyword argument
    wv.bss.activate(bss)
    print '***********************************'
    print 'Waiting for device'
    device = wv.bss.wait_for_device(bss, timeout_seconds=timeout)
    print "Device Connected"
    return device
#****************测试之前定义参数save_capture==1   ****************************
def ap_teardown(port, save_capture):
    """
    save a capture if desired.
    End the test, turn off the AP, and release the port.
    """
    if save_capture:
        wv.port.download_capture(port, file="capture")
    wv.bss.deactivate(bss)
    time.sleep(2)
    wv.port.release(port)


