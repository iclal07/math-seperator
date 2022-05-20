import time
import zmq



context = zmq.Context()
results_receiver = context.socket(zmq.PULL)
results_receiver.bind("tcp://*:5050")

#•reg rep
worker = context.socket(zmq.REP)
worker.bind("tcp://*:7000")

wor_recv= worker.recv_pyobj()

    

   
  
   
    
toplam = 0
     
for i in wor_recv:
    toplam +=i
       
        
print(toplam)

