
ids = ['337927669','345935878']

class GringottsController:

    def update_observations_map(self, observations):
            #because observation is a list of tuple
            for i in range(len(observations)) :
                the_observation = observations[i]

                if the_observation[1] == "dragon":
                    #convert the tuple localisation of the dragon into a list
                    loc_dragon = list(the_observation[1])
                    #update our map
                    self.user_map[loc_dragon[0]][loc_dragon[1]] = "D"

                if the_observation[0] == "vault" :
                    loc_vault = list(the_observation[1])
                    #if the location is not already define as a passage, then it's a vault
                    if self.user_map[loc_vault[0]][loc_vault[1]] != "P" :
                        self.user_map[loc_vault[0]][loc_vault[1]] = "V"

                if the_observation[1] == "sulfur":
                    #if the observation is sulfur I need to know who are my neighbors
                    #A list of my neighbors, the size is between 2 and 4 (includes)
                    neighbors = self.legal_neighbors()
                    #A variable that count the number of PT
                    num_of_PT = 0
                    loc_of_pt = []
                    #I check for each neighbor in my list his status in my map and update it if must to
                    for neighbor in neighbors:
                        if self.user_map[neighbor[0]][neighbor[1]] == 0:
                            self.user_map[neighbor[0]][neighbor[1]] = "PT"
                            num_of_PT += 1
                            loc_of_pt = [neighbor[0]][neighbor[1]]
                        if self.user_map[neighbor[0]][neighbor[1]] == "V":
                            self.user_map[neighbor[0]][neighbor[1]] = "VPT"
                    if num_of_PT == 1 :
                        self.user_map[loc_of_pt[0]][loc_of_pt[1]] = "T"

    def __init__(self, map_shape, harry_loc, initial_observations):
        self.user_map = [[0] * map_shape[1] for _ in range(map_shape[0])]
        self.initial_observations = initial_observations
        self.actual_loc = harry_loc
        self.map_shape = map_shape
        self.user_map[harry_loc[0]][harry_loc[1]] = "P"
        self.get_next_action(self, initial_observations)

    def legal_neighbors(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dx, dy in directions:
            new_x = self.actual_loc[0] + dx
            new_y = self.actual_loc[1] + dy

            if 0 <= new_x < self.map_shape[0] and 0 <= new_y < self.map_shape[1]:
                neighbors.append((new_x, new_y))

        return neighbors

    def update_actions_map(self, action):
        harry_x, harry_y  = self.actual_loc

        if len(action) == 1:
            if action[0] == 'wait':
                pass

            if action[0] == 'collect':
                self.user_map[harry_x][harry_y] = "P"

        else:
            x, y = action[1]
            if action[0] == 'destroy':
                if self.user_map[x][y] == "VPT" :
                    self.user_map[x][y] =  "V"

                if self.user_map[x][y] == "PT" or self.user_map[x][y]== "T" :
                    self.user_map[x][y] = "DT"

            elif action[0] == 'move':
                self.actual_loc = action[1]
                if self.user_map[x][y] == "UP" or self.user_map[x][y] == "DT":
                    self.user_map[x][y] = "P"

    def decision (self):
        #The current location of harry before he does an action
        x, y = self.actual_loc
        if self.user_map[x][y] == "V":
            return tuple("collect")

        neighbors = self.legal_neighbors()
        for neighbor in neighbors:
            if self.user_map[neighbor[0]][neighbor[1]] == "V":
                return tuple(("move", neighbor))

        for neighbor in neighbors:
            if self.user_map[neighbor[0]][neighbor[1]] == "VPT":
                return tuple(("destroy", neighbor))

        for neighbor in neighbors:
            if self.user_map[neighbor[0]][neighbor[1]] == "UP":
                return tuple(("move", neighbor))

        #else si les neighbors ne sont pas ni V, VPT ou UP alors ...

    def get_next_action(self, observations):
        self.update_observations_map(self,observations)
        action = self.decison()
        self.update_actions_map(action)
        return action

