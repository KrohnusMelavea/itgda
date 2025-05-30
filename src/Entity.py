from Vertex3D import Vertex3D

class Entity:
 translation: Vertex3D
 rotation: Vertex3D
 scale: Vertex3D
 
 model_name: str
 
 def __init__(this, translation: Vertex3D, model_name: str):
  this.translation = translation
  this.rotation = Vertex3D(0, 0, 0)
  this.scale = Vertex3D(1, 1, 1)
  this.model_name = model_name