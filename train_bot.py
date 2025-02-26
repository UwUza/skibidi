from stable_baselines3 import PPO
from rocket_league_env import RocketLeagueEnv  # Import your custom Rocket League environment

# Initialize the environment
env = RocketLeagueEnv()

# Initialize the PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)  # Adjust the total_timesteps as needed

# Save the model after training
model.save("ppo_rocket_league_model")
