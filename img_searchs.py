import requests
import json

def search_img(name_pic):
  url = "https://google.serper.dev/images"
  payload = json.dumps({
    "q": name_pic
  })
  headers = {
    'X-API-KEY': '9323443f7399b752c9c8cd327e7fb636a5e04df1',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  result = []
  try:
      for i in response.json()["images"]:
          rasm = i["imageUrl"]
          if ".png" in rasm:
            result.append(rasm.split(".png")[0]+".png")
          elif ".jpg" in rasm:
            result.append(rasm.split(".jpg")[0]+".jpg")
          elif ".webp" in rasm:
            result.append(rasm.split(".webp")[0]+".webp")
      return result[:25]
  except:
      pass
