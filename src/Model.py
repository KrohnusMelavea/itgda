from Vertex3D import Vertex3D
import numpy

class Model:
 vertices: list[Vertex3D]
 indices: list[list[int]]
 
 def __init__(this, vertices: Vertex3D, indices: list[list[int]]):
  this.vertices = vertices
  this.indices = indices
  
 def get_vertices(this):
  return numpy.array(
   [
    list(vertex.get_coordinates())
    for vertex in this.vertices
   ], 
  dtype="f"
 )
 def get_indices(this):
  return numpy.array(this.indices)
  
 def from_json(data: dict):
  return Model(
   [Vertex3D.from_json(vertices) for vertices in data["vertices"]],
   data["indices"]
  )