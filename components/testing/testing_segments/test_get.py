from components.request import request


def test():
  getRequest = request(
      type="GET",
      data={
          "User-Agent":
          "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
          "Accept": "application/json"
  })

  reqResult = getRequest.request("https://httpbin.org/get")
  
  if reqResult.status_code != 200:
    raise Exception(f"Request failed with status code {reqResult.status_code}")
  else:
    pass
