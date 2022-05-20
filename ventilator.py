import time
import zmq

context = zmq.Context()
zmq_socket = context.socket(zmq.PUSH)
zmq_socket.bind("tcp://127.0.0.1:5559")
    
    
    
    
pol_us = int(input("üs sayısını giriniz=  "))
x= int(input("taban değerini giriniz=  "))

katsayilar= []

for i in range(0, pol_us+1):
    i = int(input("katsayı değeri giriniz =  "))
    katsayilar.append(i)


print(katsayilar)
         
    
liste=[pol_us,x,katsayilar]

zmq_socket.send_pyobj(liste)

    
   
