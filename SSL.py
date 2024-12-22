import os

os.system('openssl genrsa -out key.pem 2048')
os.system('openssl req -new -x509 -key key.pem -out cert.pem -days 365')