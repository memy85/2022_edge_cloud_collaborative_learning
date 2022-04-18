

class Receiver:
    
    def __init__(self, my_ip_address, receiver_ip_address):
        self.ip_address = my_ip_address
        # self.receiver_ip_address = receiver_ip_address
    
    @call
    def receive_function(self):
        '''
        This function receives data from other devices(server, edge) 
        and returns the status to the mangager
        '''
        pass
    
    def listen(self):
        '''
        This function is activated when the manager decides to listen
        from other devices. If other signals are captured, and then it will
        initialize receiving function
        '''
        pass
    
    
        
        