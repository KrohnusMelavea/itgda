from Vertex3D import *

class Model:
 vertices: list[Vertex3D]
 indices: list[list[int]]
 
 def __init__(this, vertices: Vertex3D, indices: list[list[int]]):
  this.vertices = vertices
  this.indices = indices
  
 def from_json(data: dict):
  return Model(
   [Vertex3D.from_json(vertices) for vertices in data["vertices"]],
   data["indices"]
  )