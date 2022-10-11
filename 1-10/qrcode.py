import pyqrcode

s = 'https://www.google.com'
url = pyqrcode.create(s)

url.svg("qrcode.svg", scale=8)