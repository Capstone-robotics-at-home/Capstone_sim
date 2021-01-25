from mujoco_py import load_model_from_path, MjSim, MjViewer

model_path = "xml/bot_env_v1.xml"
model = load_model_from_path(model_path)
sim = MjSim(model)
viewer = MjViewer(sim)

for t in range(5000):
    action = 0.4 if t % 100 < 25 or t % 100 >74 else -0.4
    sim.step(action)
    viewer.render() 