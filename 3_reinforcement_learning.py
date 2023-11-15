import gymnasium as gym

with gym.make("InvertedPendulum-v4", render_mode="human") as env:
    action = 0.0 * env.action_space.sample()
    observation, _ = env.reset()
    for step in range(1_000_000):
        pitch = observation[1]
        action[0] = 5.0 * pitch  # 1D action: [ground_velocity]
        observation, reward, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            observation, _ = env.reset()
