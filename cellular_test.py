import psutil
import time
import subprocess
from Hologram.CustomCloud import CustomCloud


def hologram_network_connect():
    hologram_network_disconnect()
    time.sleep(2)
    cloud = CustomCloud(None, network='cellular')
    cloud.network.disable_at_sockets_mode()
    res = cloud.network.connect()
    message = ""
    if res:
        message = "PPP session started"
    else:
        message = "Failed to start PPP"

    print(message)


def hologram_network_disconnect():
    print('Checking for existing PPP sessions')
    for proc in psutil.process_iter():

        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except:
            print("Failed to check for existing PPP sessions")

        if 'pppd' in pinfo['name']:
            print('Found existing PPP session on pid: %s' % pinfo['pid'])
            print('Killing pid %s now' % pinfo['pid'])
            process = psutil.Process(pinfo['pid'])
            process.terminate()
            process.wait()


hologram_network_connect()
time.sleep(2)

ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", "www.google.com"], stdout=subprocess.PIPE).stdout.read()
print(ping_response.decode())

time.sleep(2)
hologram_network_disconnect()
