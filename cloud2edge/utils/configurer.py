

class Configurer:
    def __init__(self, task_name,task, server_input_size, layers, hidden_units, random_seed):
        self.task_name = task_name
        self.task = task
        self.server_input_size = server_input_size
        self.hidden_units = hidden_units
        self.random_seed = random_seed
    
    def __call__(self):
        print(self.task_name)
        pass
