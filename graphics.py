class PlotTraj:
    def __init__(self,filename):
        with open(filename) as f:
            self.data = f.read()
        
        self.data = self.data.split('\n\n')
        self.masses = []
        self.names = []
        self.trajectories = []
        sub_trajectories = []
        
        for heading in self.data:
            part = heading.split('\n')
            
            if part[0] == 'NUM_BODIES':
                self.num_bodies = int(part[1])
            if part[0] == 'NUM_STEPS':
                self.num_steps = int(part[1])
            if part[0] == 'MASSES':
                for i in range(self.num_bodies):
                    self.masses.append(part[i+1]) 
            if part[0] == 'NAMES':
                for i in range(self.num_bodies):
                    self.names.append(part[i+1])
            if part[0] == 'TRAJECTORIES':
                for i in range(self.num_steps):
                    for j in range(2):
                        sub_trajectories.append(part[j])
                    self.trajectories.append(sub_trajectories)

    def _update(self, frame):
        pass

    def animate(self):
        pass

obj = PlotTraj('trajectory.txt')
