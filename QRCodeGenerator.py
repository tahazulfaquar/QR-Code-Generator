import pyqrcode 
from pyqrcode import QRCod
  
# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"
  
# Generate QR code 
url = pyqrcode.creat(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scle = 8) 
