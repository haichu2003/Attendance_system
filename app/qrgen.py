import pyqrcode


def qr(data):
    pqr = pyqrcode.create(data)
    filename = "./image/test.png"
    pqr.png(filename, scale=10)
    return filename