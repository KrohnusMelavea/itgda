class Vertex4D:
 pass

class Vertex4D:
 x: float
 y: float
 z: float
 w: float
 
 def __init__(this, x: float, y: float, z: float, w: float):
  this.x = x
  this.y = y
  this.z = z
  this.w = w
 
 def __add__(this, other: Vertex4D) -> Vertex4D:
  return Vertex4D(this.x + other.x, this.y + other.y, this.z + other.z, this.w * other.w)
 
 def __mul__(this, other: Vertex4D):
  return Vertex4D(this.x * other.x, this.y * other.y, this.z * other.z, this.w * other.w)

 def get_coordinates(this) -> tuple[float, float, float, float]:
  return this.x, this.y, this.z. this.w
 
 def from_x(x: float) -> Vertex4D:
  return Vertex4D(x, 0, 0, 0)
 def from_y(y: float) -> Vertex4D:
  return Vertex4D(0, y, 0, 0)
 def from_z(z: float) -> Vertex4D:
  return Vertex4D(0, 0, z, 0)
 def from_w(w: float) -> Vertex4D:
  return Vertex4D(0, 0, 0, w)
