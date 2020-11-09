import mujoco_py
import os

# model = mujoco_py.load_model_from_path(dirname(dirname(mujoco_py.__file__)))
# sim = mujoco_py.MjSim(model)
# print(sim.data.pqos)
# starter web: https://openai.github.io/mujoco-py/build/html/reference.html

mj_path, _ = mujoco_py.utils.discover_mujoco() # Mujoco directory 
# xml_path = os.path.join(mj_path, 'model', 'hello.xml')  # default xml dir
current_work_dir = os.getcwd()
xml_path = os.path.join(current_work_dir,'hello.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)

print(sim.data.qpos)