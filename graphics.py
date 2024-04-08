class PlotTraj:
    def __init__(self,filename):
        with open(filename) as f:
            self.data = f.read()
        
        self.data = self.data.split('\n\n')
        self.masses = []
        self.names = []
        self.radii = []
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
            if part[0] == 'RADII':
                for i in range(self.num_bodies):
                    self.radii.append(part[i+1])
            if part[0] == 'TRAJECTORIES':
                for i in range(self.num_steps):
                    sub_trajectories = part[i+1].split(' ')
                    #self.trajectories.append(sub_trajectories)
                    sub_trajectories.pop(0)
                    x = sub_trajectories[::2]
                    y = sub_trajectories[1::2]
                    self.trajectories.append(list(zip(x,y)))

                #outputs the trajectories in 3d array format:
                #    1:  [(x1, y1), (x2, y2),..(xn, yn)]
                #    2:  [(x1, y1), (x2, y2),..(xn, yn)]

    def _update(self, frame):
        pass

    def animate(self):
        pass

obj = PlotTraj('trajectory.txt')