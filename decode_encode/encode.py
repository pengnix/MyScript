#!/usr/bin/env python
from Crypto.Cipher import AES
key = "82062cd517d245ea"
iv =  "30d288ba1a67315d"
file_read = open("input.txt", 'r')
content = file_read.read().encode("utf-8")
file_read.close()
obj = AES.new(key, AES.MODE_CBC, iv)
print(len(content))
length = 16 - (len(content) % 16)
content = content + bytes(b'\0')*length
print(len(content))
print(len(content.decode("utf-8")))
output = obj.encrypt(content)
file_write = open("output.txt", 'wb')
file_write.write(output)
file_write.close()
