import rlgym  # Make sure rlgym is imported

class RocketLeagueEnv:
    def __init__(self):
        # Create the environment instance
        self.env = rlgym.make()  # Assuming rlgym.make() properly creates the environment
    
    def reset(self):
        # Reset the environment and get the initial state
        self._prev_state = self.env.reset()  # Reset the environment
        return self._prev_state  # Return the initial state
    
    def step(self, action):
        # Perform a step in the environment based on the action
        state, reward, done, info = self.env.step(action)
        return state, reward, done, info  # Return the new state, reward, done flag, and info
    
    def render(self):
        # You can optionally add a render method to visualize the environment if needed
        self.env.render()
