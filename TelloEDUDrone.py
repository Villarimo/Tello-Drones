# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py
#wifi adress D8DDCF
import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nChristopher Villarimo")
print("Program Name: Flight School - Square ")
print("Date: 3.22.2022 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')
        sendmsg("go 188 0 60 50")
        sendmsg("go 210 0 70 50")
        sendmsg("curve 123 73 0 123 123 0 50")
        sendmsg("ccw 90")
        sendmsg("curve 123 73 0 123 123 0 50")
        sendmsg("ccw 90")
        sendmsg("go 210 0 -80 50")


        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
