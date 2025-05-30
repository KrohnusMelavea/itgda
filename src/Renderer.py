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
import time

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
  this.camera_uniform_buffer = glGenBuffers(1)
  glBindBufferBase(GL_UNIFORM_BUFFER, this.camera_uniform_index, this.camera_uniform_buffer)

  colour_offset = 0
  this.colours_offsets = dict()
  for model_name, model in this.models.items():
   this.colours_offsets[model_name] = colour_offset
   colour_offset += len(model.colours)
  colours_data = numpy.concatenate([this.models[model].get_colours() for model in this.models])
  #colours_data = this.models["cube"].get_colours()
  this.colours_buffer = glGenBuffers(1)
  glBindBuffer(GL_SHADER_STORAGE_BUFFER, this.colours_buffer)
  glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 1, this.colours_buffer)
  glNamedBufferData(this.colours_buffer, colours_data.nbytes, None, GL_DYNAMIC_COPY)
  this.mmapped_colours_buffer = glMapNamedBufferRange(
   this.colours_buffer,
   0,
   colours_data.nbytes,
   GL_MAP_READ_BIT | GL_MAP_WRITE_BIT
  )
  this.mapped_colours_buffer = (GLfloat * (colours_data.nbytes // 4)).from_address(this.mmapped_colours_buffer)
  ctypes.memmove(this.mapped_colours_buffer, colours_data.ctypes.data, colours_data.nbytes)
  glUnmapNamedBuffer(this.colours_buffer)
  #glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

  # this.fragment_uniform_data_index = glGetUniformBlockIndex(this.shader_sets[this.active_shader_set].program, "UniformData")
  # print(this.fragment_uniform_data_index)
  # this.fragment_uniform_data = glGenBuffers(1)
  # glBindBufferBase(GL_UNIFORM_BUFFER, this.fragment_uniform_data_index, this.fragment_uniform_data)

 def destroy(this):
  glDeleteBuffers(this.camera_uniform_buffer)
  
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
  camera_projection = pyrr.matrix44.create_perspective_projection(75.0, 800 / 600, 0.1, 75.0, dtype='f')
  camera_data = numpy.concatenate((camera_view, camera_projection))
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
  #glBindBuffer(GL_SHADER_STORAGE_BUFFER, this.colours_buffer)
  #glBindBufferBase(GL_SHADER_STORAGE_BUFFER, 1, this.colours_buffer)
  #colours_data = this.models["cube"].get_colours()
  #colours_data = this.models["cube"].get_colours()
  #sglFlushMappedNamedBufferRange(this.colours_buffer, 0, colours_data.nbytes)
  #glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0)

  #uniform_data = numpy.array([this.colours_offsets[model_name]], dtype=numpy.int32)
  #glNamedBufferData(this.camera_uniform_buffer, uniform_data.nbytes, uniform_data, GL_DYNAMIC_DRAW)
  
  glUniform1i(glGetUniformLocation(this.shader_sets[this.active_shader_set].program, "colours_offset"), this.colours_offsets[model_name])

  transformation_data = numpy.array([list(entity.translation.get_coordinates()) + list(entity.rotation.get_coordinates()) + list(entity.scale.get_coordinates()) for entity in entities], dtype=numpy.float32)
  transformation_buffer = vbo.VBO(data=transformation_data, usage=GL_STATIC_DRAW, target=GL_ARRAY_BUFFER)
  
  this.models[model_name].index_buffer.bind()
  glEnableVertexAttribArray(0)
  glEnableVertexAttribArray(1)
  glEnableVertexAttribArray(2)
  glEnableVertexAttribArray(3)
  this.models[model_name].vertex_buffer.bind()
  glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, None)
  transformation_buffer.bind()
  glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(0))
  glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(12))
  glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(24))
  
  glVertexAttribDivisor(1, 1)
  glVertexAttribDivisor(2, 1)
  glVertexAttribDivisor(3, 1)
  
  glDrawElementsInstanced(GL_TRIANGLES, 12*6, GL_UNSIGNED_INT, this.models[model_name].index_buffer, len(entities))
  
  glFlush()

  this.models[model_name].index_buffer.unbind()
  this.models[model_name].vertex_buffer.unbind()
  transformation_buffer.unbind()
 