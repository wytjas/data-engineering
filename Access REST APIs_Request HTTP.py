import requests

import os 
from PIL import Image
from IPython.display import IFrame

#Get Request with URL Parameters
url_get='http://httpbin.org/get'
r=requests.get(url_get,params=payload)

#Post Requests
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
