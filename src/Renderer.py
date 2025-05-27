from Model import Model
from OpenGL.arrays import vbo
from OpenGL.GL import shaders
from OpenGL.raw.GL.ARB.vertex_array_object import (
 glGenVertexArrays,
 glBindVertexArray
)
import numpy

class Renderer:
 models: dict[str, Model]
 geometry_cache: dict[str, tuple[numpy.ndarray, numpy.ndarray]]
 
 
 
 def __init__(this, models: dict[str, Model]):
  this.models = models
  this.regenerate_cache()
 
 def add_model(this, name: str, model: Model = None):
  this.models[name] = model
  if model is not None:
   this.regenerate_cache(name)
 
 def regenerate_cache(this, name: str = None):
  if name is None:
   this.geometry_cache = dict(
    (
     name, 
     (
      model.get_vertices(), 
      model.get_indices()
     )
    )
    for name, model in this.models.items()
   )
  else:
   this.geometry_cache[name] = (
    this.models[name].get_vertices(),
    this.models[name].get_indices()
   )
 
 def draw(this, name: str):
  pass