import upip

def requirements(requests):    
    """
    `upip.install('urequests')`
    
    This is the function that installs the urequests module
    
    :param requests: The number of requests to make
    :return: The urequests module
    """
    upip.debug = True
    upip.install('urequests')
    import urequests
    return urequests