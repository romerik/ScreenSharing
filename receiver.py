from vidstream import StreamingServer
import threading

Ip = 'localhost' # The ip of the receiver that you can change whether you don't run the receiver on your own pc
port = 5555 # The port of the recever that you can change too

print("Start the receiver\nIp = {} \nPort = {}".format(Ip,port))
receiver  = StreamingServer(Ip,port)
t = threading.Thread(target=receiver.start_server)
t.start()

while input("")!='STOP':
    continue

receiver.stop_server()