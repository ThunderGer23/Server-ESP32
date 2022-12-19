# Importing the libraries that will be used in the program.
import time, network
from config.internet import internet
from src.sendRequests import sendRequest
from config.accessPoint import accessPoint
from config.requirements import requirements
from docs.messages import token, message, url, cont, notWifi, notClients
# Declaring the variables that will be used in the program.
sta_if = network.WLAN(network.STA_IF)
AP = network.WLAN(network.AP_IF)
sAP = None
requests = None

def main():
    """
    It waits for a client to connect to the ESP32's AP, then it receives a message from the client,
    sends it to the API, receives the response from the API, and sends it back to the client
    :return: The response is a string with the following format:
    """
    request = {
        'token': token,#'5f7be1f5-3dbb-41dc-8645-300beced1fe4',
        'message': message,
        'url': url
    }
    text = ''
    while(True):
        time.sleep(1)
        if(sta_if.isconnected()) and (len(AP.status('stations')) > 0):
            cl,addrAP = sAP.accept()
            request['message'] = cl.recv(4096)
            if(len(request['message']) == 0):
                print(cont)
                continue
            else:
                response = sendRequest(request)
                print('Response({}): '.format(len(response)),response)
                cl.send(response)
            cl.close()
        else:
            if sta_if.isconnected() != True: print(notWifi)
            if len(AP.status('stations')) == 0: print(notClients)
    return

def config():
    """
    This function configures the access point, connects to the internet, and installs the required
    libraries
    :return: Nothing.
    """
    AP, sAP = accessPoint(AP, sAP)
    sta_if = internet(sta_if)
    requests = requirements(requests)
    return

