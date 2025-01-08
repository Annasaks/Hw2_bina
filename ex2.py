
ids = ['337927669','345935878']

class GringottsController:

    def update_observations_map(self, observations):
        return True



    def __init__(self, map_shape, harry_loc, initial_observations):
        self.user_map = list([map_shape[0]][map_shape[1]])
        self.initial_observations = initial_observations
        self.actual_loc = harry_loc
        self.neighbors = self.legal_neighbors()
        self.map_shape = map_shape
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

    def get_next_action(self, observations):
        self.update_observations_map(self,observations)
        return True

