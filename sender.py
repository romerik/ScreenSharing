from vidstream import ScreenShareClient
import threading

Ip = input("Enter the receiver Ip adress : ")
port = int(input("Enter the port of the receiver : "))


print("Start sending video to the receiver which adress is {} and port is {}".format(Ip,port))
sender = ScreenShareClient(Ip,port)

t = threading.Thread(target=sender.start_stream)
t.start()
while input("") != 'STOP':
    continue

sender.stop_stream()