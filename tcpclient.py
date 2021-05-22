import socket

target_host = 'd2.taha.sch.ir'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((target_host,target_port))
client.send(b"GET / HTTP/1.1\r\nHost:https:// d2.taha.sch.ir\r\n\r\n")
response = client.recv(4096)

print(response.decode())
client.close()
