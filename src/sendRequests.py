import json as ujson

def sendRequest(req):
    """
    It takes a dictionary as an argument, and sends a POST request to the url in the dictionary, with
    the token and message in the dictionary as the body of the request
    
    :param req: The request object
    :return: The response from the server.
    """
    global requests
    token = req["token"]
    message = req['message']
    url = req['url']
    request = {'token': token,'message': message}
    post_data = ujson.dumps(request).encode('utf8')
    print("\n\n",str(post_data),"\n\n")
    res = requests.post(url,headers = {'content-type': 'application/json'},data=post_data)
    return res.text