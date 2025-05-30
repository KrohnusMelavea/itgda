class Vertex3D:
 pass

class Vertex3D:
 x: float
 y: float
 z: float
 
 def __init__(this, x: float, y: float, z: float):
  this.x = x
  this.y = y
  this.z = z
 
 def __add__(this, other: Vertex3D) -> Vertex3D:
  return Vertex3D(this.x + other.x, this.y + other.y, this.z + other.z)
 
 def __mul__(this, other: Vertex3D):
  return Vertex3D(this.x * other.x, this.y * other.y, this.z * other.z)

 def get_coordinates(this) -> tuple[float, float, float]:
  return this.x, this.y, this.z
 
 def from_x(x: float) -> Vertex3D:
  return Vertex3D(x, 0, 0)
 def from_y(y: float) -> Vertex3D:
  return Vertex3D(0, y, 0)
 def from_z(z: float) -> Vertex3D:
  return Vertex3D(0, 0, z)

 def from_json(data: dict):
  return Vertex3D(
   data["x"],
   data["y"],
   data["z"]
  )
