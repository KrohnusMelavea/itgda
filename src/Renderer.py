from core import quaternion_rotate_3d
from Model import Model
from ShaderSet import ShaderSet
from Camera import Camera
from Vertex3D import Vertex3D
from Entity import Entity
from OpenGL.GL import (
 glClear,
 glEnable,
 glUniform3f,
 glUseProgram,
 glTranslate,
 glDrawElements,
 glGetUniformLocation,
 glVertexAttribPointer,
 glEnableVertexAttribArray,
 GL_FLOAT,
 GL_TRIANGLES,
 GL_DEPTH_TEST,
 GL_UNSIGNED_INT,
 GL_COLOR_BUFFER_BIT,
 GL_DEPTH_BUFFER_BIT
)
from OpenGL.arrays import vbo
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from pygame.locals import GL_DEPTH_SIZE
import numpy
import ctypes
import pyrr
import pygame
import math

class Renderer:
 models: dict[str, Model]
 shader_sets = list[ShaderSet]
 active_shader_set: int
 entities: list[Entity]
 
 camera_uniform_location: int

 def __init__(this, models: dict[str, Model], shader_sets: list[ShaderSet], entities: list[Entity]):
  this.models = models
  this.shader_sets = shader_sets
  this.active_shader_set = 0
  this.entities = entities
  
  this.vao = glGenVertexArrays(1)
  glBindVertexArray(this.vao)
  glEnableClientState(GL_VERTEX_ARRAY)
  
  glUseProgram(this.shader_sets[this.active_shader_set].program)
  glLinkProgram(this.shader_sets[this.active_shader_set].program)
  
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)
  glCullFace(GL_FRONT)
  glFrontFace(GL_CCW)
  this.camera_uniform_index = glGetUniformBlockIndex(this.shader_sets[this.active_shader_set].program, "UBO")
  print(this.camera_uniform_index)
  
  this.camera_uniform_buffer = glGenBuffers(1)
  glBindBufferBase(GL_UNIFORM_BUFFER, this.camera_uniform_index, this.camera_uniform_buffer)
 
 def draw(this, camera: Camera):
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  rotation_offset = quaternion_rotate_3d(Vertex3D(0, 0, 0), camera.rotation)
  camera_view = pyrr.matrix44.create_look_at(
   camera.position.get_coordinates(), 
   (
    camera.position.x + math.cos(camera.rotation.y),
    camera.position.y + 0,
    camera.position.z + math.sin(camera.rotation.y)
   ), 
   (0, 1, 0), dtype='f')
  camera_projection = pyrr.matrix44.create_perspective_projection(75.0, 1920 / 1080, 0.1, 75.0, dtype='f')
  camera_data = numpy.concatenate((camera_view, camera_projection))
  print(camera_data)
  glNamedBufferData(this.camera_uniform_buffer, camera_data.nbytes, camera_data, GL_DYNAMIC_DRAW)
  
  mapped_entities: dict[str, list[Entity]] = dict()
  for entity in this.entities:
   if entity.model_name in mapped_entities:
    mapped_entities[entity.model_name].append(entity)
   else:
    mapped_entities[entity.model_name] = [entity]
  
  for model_name in mapped_entities:
   this.draw_entities(model_name, mapped_entities[model_name])
  
 def draw_entities(this, model_name: str, entities: list[Entity]):
  transformation_data = numpy.array([list(entity.position.get_coordinates()) + [0, 0, 0, 10, 10, 10, 1, 1, 1] for entity in entities], dtype='f')
  transformation_buffer = vbo.VBO(data=transformation_data, usage="GL_DYNAMIC_DRAW", target="GL_ARRAY_BUFFER")
  
  this.models[model_name].index_buffer.bind()
  glEnableVertexAttribArray(0)
  glEnableVertexAttribArray(1)
  this.models[model_name].vertex_buffer.bind()
  glVertexAttribPointer(0, 3, GL_FLOAT, True, 12, None)
  transformation_buffer.bind()
  glVertexAttribPointer(1, 3, GL_FLOAT, True, 48, None)
  glVertexAttribPointer(1, 3, GL_FLOAT, True, 48, None)
  glVertexAttribPointer(1, 3, GL_FLOAT, True, 48, None)
  glVertexAttribPointer(1, 3, GL_FLOAT, True, 48, None)
  glVertexAttribDivisor(1, 1)
  
  glDrawElementsInstanced(GL_TRIANGLES, 12*6, GL_UNSIGNED_INT, this.models[model_name].index_buffer, len(entities))
  