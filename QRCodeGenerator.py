import pyqrcode 
from pyqrcode import QRCode
s = "https://github.com/TriCompany"
url = pyqrcode.create(s) 
url.svg("myyoutube.svg", scale = 8) 
