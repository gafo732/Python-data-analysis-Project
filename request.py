import requests
import json
import pandas as pd

url = "http://127.0.0.1:5000/api/"

duration = 120
codec = "flv"
width = 1280
height = 720
bitrate = 70000
frames = 6000
fps = frames/duration
i = frames/2
p = frames/4
b = frames/4
size = 90000
i_size = size/3
p_size = size/3
b_size = size/3
o_codec = "mpeg4"
o_bitrate = 75000
o_fps = 60
o_height = 2160
o_width = 3840
umem = 60000


request_exemple = [duration, codec,width,height,bitrate,fps,i,p,b,frames,i_size,p_size,b_size,size,o_codec,o_bitrate,o_fps,o_width,o_height,umem]
jsondata = json.dumps(request_exemple)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

response = requests.post(url, data=jsondata, headers=headers)

print(f"Le temps de transcodage de votre video devrait etre de : {response.json()['result']} secondes.")
