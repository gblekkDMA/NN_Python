import gym
import random

# VARIABLES
env = gym.make('FrozenLake-v0')
score = 0
numGames = 1000
numSteps = 10

# Set Up Game
env.reset()

print(env.observation_space) # which space the player is currently in
print(env.action_space) # actions the player can take

# Instructions
# 0 = Left
# 1 = Down
# 2 = Right
# 3 = Up

# obs, rew, done, info = env.step(env.action_space.sample()) # take an action
def PlayGame():
    global score
    for i in range(numSteps):
        obs, rew, done, info = env.step(random.randint(1,2))
        #env.render()
        if done:
            score += rew
            break



# Main Game Loop
for g in range(numGames):
    env.reset()
    PlayGame()

print(score)