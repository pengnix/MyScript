#!/usr/bin/env python
from Crypto.Cipher import AES
key = "82062cd517d245ea"
iv =  "30d288ba1a67315d"
file_read = open("input.txt", 'rb')
content = file_read.read()
file_read.close()
obj = AES.new(key, AES.MODE_CBC, iv)
output = obj.decrypt(content)
file_write = open("output.txt", 'w')
file_write.write(output.decode("utf-8").strip('\0'))
file_write.close()