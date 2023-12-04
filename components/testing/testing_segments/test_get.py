from components.request import request

def test():
    getRequest = request(type="GET", data={"User-Agent": "Chrome", "Accept": "application/json"})
    getRequest.data