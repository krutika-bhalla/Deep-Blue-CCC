from flask import Flask, render_template, Response
from imutils.video import VideoStream
import numpy as np
import matplotlib.pyplot as plt
import threading
import argparse
import datetime
import imutils
import time
import cv2
import socket 

app = Flask(__name__)


cnt = []
name = []


@app.route('/')
def index():
    # rendering webpage

    # s = socket.socket()             # Create a socket object
    host = ["192.168.0.110", "192.168.0.105"]  #Ip address that the TCPServer  is there
    files=["Srinidhi.txt","Srinath.txt"]
    port = [50000,50001]  # Reserve a port for your service every new transfer wants a new port or you must wait.


    while True:

        for i in range(2):
            
            s = socket.socket()     
            s.connect((host[i], port[i]))
            s.send(b"Hello server!")

            data = s.recv(1024)
            data = data.decode('utf-8')

            print(data)
            
            cnt, name, jimg = data.split(",")
            if i==0:
                name1="Srinidhi"
                cnt1=cnt
                img1 = jimg
            elif i==1:
                name2="Srinath"
                cnt2=cnt
                img2 = jimg



            # print('data=%s', (data))

            # with open(files[i], 'wb') as f:
            #     print ('file opened')
            #     while True:
            #         print('receiving data...')
            #         data = s.recv(1024)
            #         print('data=%s', (data))
            #         if not data:
                        
            #             break
            #         # write data to a file
            #         f.write(data)

            # f.close()
            #print('Successfully get the file')
            s.close()
            #print('connection closed')
        
        return render_template('index.html', count1=cnt1, name1=name1, count2=cnt2, name2=name2, img1=img1, img2=img2)


if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='192.168.0.107', debug=False)