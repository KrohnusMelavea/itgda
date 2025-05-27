from Model import Model
from OpenGL.arrays import vbo
from OpenGL.raw.GL.ARB.vertex_array_object import (
 glGenVertexArrays,
 glBindVertexArray
)

class Renderer:
 models: dict[str, Model]
 
 def __init__(this, models: dict[str, Model]):
  this.models = models
 
 def draw(this, name: str):
  print(this.models[name])
  print(this.models[name].get_vertices())