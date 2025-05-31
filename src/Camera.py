from Vertex3D import Vertex3D

class Camera:
 position: Vertex3D
 rotation: Vertex3D
 global_scale: Vertex3D
 
 def __init__(this, position: Vertex3D, rotation: Vertex3D):
  this.position = position
  this.rotation = rotation
  this.global_scale = Vertex3D(1.0, 1.0, 1.0)