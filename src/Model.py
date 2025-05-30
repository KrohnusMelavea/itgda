from Vertex3D import Vertex3D
from OpenGL.raw.GL.ARB.vertex_array_object import (
 glGenVertexArrays,
 glBindVertexArray
)
from OpenGL.arrays import vbo
import numpy

class Model:
 vertices: list[Vertex3D]
 indices: list[list[int]]
 #colours: list[Vertex3D]
 
 vertex_buffer: vbo.VBO
 index_buffer: vbo.VBO
 #colour_buffer: vbo.VBO
 
 def __init__(this, vertices: list[Vertex3D], indices: list[list[int]]):
  this.vertices = vertices
  this.indices = indices
  #this.colours = colours
  
  this.build_vertex_buffer()
  this.build_index_buffer()
  #this.build_colour_buffer()
  
 def get_vertices(this):
  return numpy.array(
   [
    list(vertex.get_coordinates())
    for vertex in this.vertices
   ], 
   dtype="f"
  )
 def get_indices(this):
  return numpy.array(
   this.indices,
   dtype=numpy.uint32
  )
 # def get_colours(this):
 #  return numpy.array(
 #    [
 #     list(colour.get_coordinates())
 #     for colour in this.colours
 #    ], 
 #    dtype="f"
 #   )

 def build_vertex_buffer(this) -> vbo.VBO:
  this.vertex_buffer = vbo.VBO(
   data=this.get_vertices(), 
   usage="GL_STATIC_DRAW", 
   target="GL_ARRAY_BUFFER"
  )
  return this.vertex_buffer
 def build_index_buffer(this) -> vbo.VBO:
  this.index_buffer = vbo.VBO(
   data=this.get_indices(),
   usage="GL_STATIC_DRAW",
   target="GL_ELEMENT_ARRAY_BUFFER"
  )
  return this.index_buffer
 # def build_colour_buffer(this) -> vbo.VBO:
 #  this.colour_buffer = vbo.VBO(
 #   data=this.get_colours(), 
 #   usage="GL_STATIC_DRAW", 
 #   target="GL_ARRAY_BUFFER"
 #  )
 #  return this.colour_buffer
  
 def from_json(data: dict):
  return Model(
   [Vertex3D.from_json(vertices) for vertices in data["vertices"]],
   data["indices"]
  )
