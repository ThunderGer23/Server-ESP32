import time

def internet(sta_if):
    """
    It activates the station interface, scans for networks, connects to the network, and then checks if
    it's connected. If it's not connected, it prints an 'A' and waits 100ms. If it is connected, it
    prints an exclamation mark and a new line
    
    :param sta_if: The name of the station interface
    :return: the sta_if object.
    """
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect('Totalplay-64AA','64AA2A07y2jxWzgP')
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        time.sleep_ms(100)
        continue
    print('!\nConnected!\n')
    return sta_if