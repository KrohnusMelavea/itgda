from Model import Model
from Vertex3D import Vertex3D
import json
import math

def read_file(file_path: str) -> str:
 data = None
 with open(file_path, "r") as file_handler:
  data = file_handler.read()
 return data
def read_json(file_path: str) -> dict:
 return json.loads(read_file(file_path))
def read_models(file_path: str) -> dict[str, Model]:
 data: dict = read_json(file_path)
 return dict(
  (name, Model.from_json(model)) 
  for name, model in data.items()
 )
 
def quaternion_rotate_3d(V: Vertex3D, A: Vertex3D) -> Vertex3D:
 cx = math.cos(A.x)
 cy = math.cos(A.y)
 cz = math.cos(A.z)
 sx = math.sin(A.x)
 sy = math.sin(A.y)
 sz = math.sin(A.z)
 x = V.x
 y = V.y
 z = V.z
 return Vertex3D(
		(x*cy + (y*sx + z*cx) * sy) * cz - (y*cx - z*sx) * sz,
		(x*cy + (y*sx + z*cx) * sy) * sz + (y*cx - z*sx) * cz,
		(y*sx + z*cx) * cy - x*sy
	)