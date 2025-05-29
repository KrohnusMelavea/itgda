from Vertex3D import Vertex3D

class Entity:
 position: Vertex3D
 model_name: str
 
 def __init__(this, position: Vertex3D, model_name: str):
  this.position = position
  this.model_name = model_name