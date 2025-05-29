from Vertex3D import Vertex3D

class Camera:
 position: Vertex3D
 rotation: Vertex3D
 
 def __init__(this, position: Vertex3D, rotation: Vertex3D):
  this.position = position
  this.rotation = rotation