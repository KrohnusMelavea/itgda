from Vertex3D import Vertex3D

class Entity:
 translation: Vertex3D # Question 2: Instance-Based Translation
 rotation: Vertex3D    # Question 3: Instance-Based Rotation
 scale: Vertex3D       # Question 4: Instance-based Scaling
 
 model_name: str
 
 def __init__(
  this, 
  translation: Vertex3D, # Question 2: Instance-Based Translation
  model_name: str
 ):
  this.translation = translation    # Question 2: Instance-Based Translation
  this.rotation = Vertex3D(0, 0, 0) # Question 3: Instance-Based Rotation
  this.scale = Vertex3D(1, 1, 1)    # Question 4: Instance-Based Scaling
  this.model_name = model_name