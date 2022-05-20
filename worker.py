import time
import zmq
import random



  
context = zmq.Context()
worker_receiver = context.socket(zmq.PULL)
worker_receiver.connect("tcp://127.0.0.1:5559")
    
    
# send work
worker_sender = context.socket(zmq.PUSH)
worker_sender.connect("tcp://localhost:5050")
    
#req rep sink

sink = context.socket(zmq.REQ)
sink.connect("tcp://127.0.0.1:7000")



    
    
    
while True:
        
    term= worker_receiver.recv_pyobj()
 
    print(term)
    
 
    katsayilar= term[2]   
    
 
    liste1= []
    for i in range(term[0]+1):
        liste1.append(i)
    liste1.reverse()
    print(liste1)

    resultt =[]
    for i in range(len(liste1)):
        val=  katsayilar[i] * pow(term[1], liste1[i])
        print(val)
        resultt.append(val)
    
    
    print(resultt)
    sink.send_pyobj(resultt)
  
    
   
    
