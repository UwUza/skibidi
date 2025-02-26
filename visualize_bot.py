from stable_baselines3 import PPO
from rocket_league_env import RocketLeagueEnv

# Load the trained model
model = PPO.load("models/rocket_league_bot")

# Create the environment
env = RocketLeagueEnv()

# Visualize the trained bot's actions
obs = env.reset()
done = False

while not done:
    # Get the action predicted by the trained model
    action, _states = model.predict(obs)
    # Apply the action to the environment
    obs, reward, done, info = env.step(action)
    # Render the environment to visualize the bot's performance
    env.render()
