import gym
import random

env = gym.make('FrozenLake-v0')

env.reset()
score = 0

def play_game():
    for i in range(10):
        obs, rew, done, info = env.step(random.randint(1,2))
        env.render()
        if done:
            score += rew
            break
            # scipy

print(env.observation_space) # which space the player is currently in
print(env.action_space) # actions the player can take

# 0 = Left
# 1 = Down
# 2 = Right
# 3 = Up
# obs, rew, done, info = env.step(env.action_space.sample()) # take an action

for g in range(1000):
    env.reset()
    play_game()


print(score)

