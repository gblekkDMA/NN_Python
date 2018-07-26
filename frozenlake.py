import gym
import random

env = gym.make('FrozenLake-v0')

# s - start f - frozen h - hole g - goal

# 0 = LEFT
# 1 = DOWN
# 2 = RIGHT
# 3 = UP

print(env.observation_space)
print(env.action_space)
env.reset()  #this is what will reset the environment to the starting state––always use this first.


# for _ in range(10):
#     obs, rew, done, info = env.step(1)
#     env.render()
#     if done:
#         break
#
#
# env.reset()
# for _ in range(100):
#     obs, rew, done, info = env.step(env.action_space.sample())
#     print("Observation: "+str(obs))
#     env.render()
#     if done:
#         break

score = 0
#for a bunch of  episodes
for _ in range(10000):
    #refresh and render the initial state
    env.reset()
    for t in range(100):   #take 100 steps
     #   obs, rew, done, info = env.step(env.action_space.sample()) # take a random action
        obs, rew, done, info = env.step(random.randint(1, 2))
        #print(obs) #The observation, which is where the player is
        if done:  #The player either hit a hole or the goal
            score += rew  # you get +1 for reaching the goal, 0 otherwise. This will tell us how many successful attempts we had
            env.render()  # Take a look at the final state, may want to comment out
            break
print(score)  # Take a look at how many successes