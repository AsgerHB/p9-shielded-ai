import gym
from gym.utils.play import play

env = gym.make("LunarLander-v2")
observation = env.reset()

play(env, keys_to_action={
 (ord('w'), ): 2,
 (ord('a'), ): 3,
 (ord('s'), ): 0,
 (ord('d'), ): 1,
})
