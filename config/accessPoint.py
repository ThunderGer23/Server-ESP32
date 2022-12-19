import socket

def accessPoint(AP, sAP):    
    """
    It creates an access point with the name ESP_32, channel 11, WPA2-PSK, password 12345678, and a
    maximum of 30 clients
    
    :param AP: the access point object
    :param sAP: socket for the access point
    :return: A tuple of two objects.
    """
    AP.config(essid = 'ESP_32', channel = 11, authmode = 3, password = '12345678')
    AP.config(max_clients = 30)
    AP.active(True)
    addrAP = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    sAP = socket.socket()
    sAP.bind(addrAP)
    sAP.listen(100)
    print(AP.ifconfig())
    return {AP, sAP}