from core import read_file
from OpenGL.GL import (
 shaders,
 GL_VERTEX_SHADER,
 GL_FRAGMENT_SHADER
)

class Shader:
 path: str
 source: str
 binary: int
 
 def __init__(this, file_path: str):
  this.path = file_path
  this.source = read_file(this.path)
  this.binary = shaders.compileShader(
   this.source, 
   Shader.get_shader_type_from_file_path(this.path)
  )

 def reload_from_file(this):
  source: str = read_file(this.path)
  if source != this.source:
   this.source = source
   this.reload_from_source()
 def reload_from_source(this):
  this.binary = shaders.compileShader(
   this.source, 
   Shader.get_shader_type_from_file_path(this.path)
  )
 
 def get_shader_type_from_file_path(file_path: str):
  if file_path.endswith(".vert"):
   return GL_VERTEX_SHADER
  elif file_path.endswith(".frag"):
   return GL_FRAGMENT_SHADER
  
  raise Exception(f"Unable to Infer Shader Type from Shader Source File Path: {file_path}")
 