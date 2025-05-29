from Shader import Shader
from OpenGL.GL import shaders
from OpenGL.GL.shaders import ShaderProgram

class ShaderSet:
 shaders: list[Shader]
 program: ShaderProgram
 
 def __init__(this, shader_source_paths: list[str]):
  this.shaders = [
   Shader(shader_source_path)
   for shader_source_path in shader_source_paths
  ]
  this.compile()
 
 def compile(this) -> ShaderProgram:
  this.program = shaders.compileProgram(*[shader.binary for shader in this.shaders])
  return this.program