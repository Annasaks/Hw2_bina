
ids = ['337927669','345935878']

class GringottsController:

    def update_observations_map(self, observations):
        pass

    def __init__(self, map_shape, harry_loc, initial_observations):
        user_map = list([map_shape[0]][map_shape[1]])
        actual_loc = harry_loc
        self.get_next_action(self, initial_observations)

    def get_next_action(self, observations):
        self.update_observations_map(self, observations)
