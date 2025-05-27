class Vertex3D:
 x: float
 y: float
 z: float
 
 def __init__(this, x: float, y: float, z: float):
  this.x = x
  this.y = y
  this.z = z
  
 def from_json(data: dict):
  return Vertex3D(
   data["x"],
   data["y"],
   data["z"]
  )
