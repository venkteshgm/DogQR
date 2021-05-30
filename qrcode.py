# # Import QRCode from pyqrcode
# import pyqrcode
# import png
# from pyqrcode import QRCode
  
  
# # String which represents the QR code
# # s = "www.geeksforgeeks.org"
# s = 'http://192.168.0.8:8000'
  
# # Generate QR code
# url = pyqrcode.create(s)
  
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)
  
# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale = 6)




# import pyqrcode
# from PIL import Image
# # import Image
# # Generate the qr code and save as png
# # qrobj = pyqrcode.create('https://stackoverflow.com')
# qrobj = pyqrcode.create('http://192.168.0.8:8000')
# with open('qrcode.png', 'wb') as f:
#     qrobj.png(f, scale=10)

# # Now open that png image to put the logo
# img = Image.open('qrcode.png')
# width, height = img.size

# # How big the logo we want to put in the qr code png
# logo_size = 50

# # Open the logo image
# logo = Image.open('test.png')

# # Calculate xmin, ymin, xmax, ymax to put the logo
# xmin = ymin = int((width / 2) - (logo_size / 2))
# xmax = ymax = int((width / 2) + (logo_size / 2))

# # resize the logo as calculated
# logo = logo.resize((xmax - xmin, ymax - ymin))

# # put the logo in the qr code
# img.paste(logo, (xmin, ymin, xmax, ymax))

# img.show()

import pyqrcode
from PIL import Image
# url = pyqrcode.QRCode('http://www.eqxiu.com',error = 'H')
url = pyqrcode.QRCode('http://192.168.0.8:8000',error = 'H')
url.png('test.png',scale=10)
im = Image.open('test.png')
im = im.convert("RGBA")
logo = Image.open('logo.png')
box = (135,135,235,235)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()