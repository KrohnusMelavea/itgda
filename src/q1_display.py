from core import read_models, quaternion_rotate_3d
from ShaderSet import ShaderSet
from Renderer import Renderer
from Entity import Entity
from Vertex3D import Vertex3D
from Camera import Camera
from KeyboardState import KeyboardState
import pygame
import time
import math
import pyrr

def main():
 MODELS_PATH = "../res/models.json"
 
 pygame.init()
 screen_width = pygame.display.Info().current_w
 screen_height = pygame.display.Info().current_h
 window = pygame.display.set_mode((800, 600), pygame.OPENGL | pygame.DOUBLEBUF)
 
 renderer = Renderer(
  read_models(MODELS_PATH),
  [
   ShaderSet([
    "../res/sha/default.frag",
    "../res/sha/default.vert"
   ])
  ],
  [
   Entity(Vertex3D(0, 0, 0), "cube"),
   Entity(Vertex3D(0, 5, 0), "pyramid"),
   Entity(Vertex3D(0, -5, 0), "prism"),
  ]
 )
 
 keyboard_state = KeyboardState()
 camera = Camera(position=Vertex3D(0, 0, 10), rotation = Vertex3D(0, 0, 0))
 movement_speed = 0.008
 rotation_speed = 0.002
 
 running = True
 while True:
  for event in pygame.event.get():
   if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
    keyboard_state.update(event.type, event.key)
    if event.key == pygame.K_ESCAPE:
     running = False
     break
      
  if not running:
   break

  if keyboard_state.u_arrow:
   camera.rotation.x += rotation_speed
  if keyboard_state.r_arrow:
   camera.rotation.y -= rotation_speed
  if keyboard_state.d_arrow:
   camera.rotation.x -= rotation_speed
  if keyboard_state.l_arrow:
   camera.rotation.y += rotation_speed
  if keyboard_state.q:
   camera.rotation.z += rotation_speed
  if keyboard_state.e:
   camera.rotation.z -= rotation_speed
  if keyboard_state.w:
   camera.position += quaternion_rotate_3d(Vertex3D(0, 0, -movement_speed), camera.rotation)
  if keyboard_state.a:
   camera.position += quaternion_rotate_3d(Vertex3D(-movement_speed, 0, 0), camera.rotation)
  if keyboard_state.s:
   camera.position += quaternion_rotate_3d(Vertex3D(0, 0, movement_speed), camera.rotation)
  if keyboard_state.d:
   camera.position += quaternion_rotate_3d(Vertex3D(movement_speed, 0, 0), camera.rotation)
  if keyboard_state.space:
   camera.position += quaternion_rotate_3d(Vertex3D(0, movement_speed, 0), camera.rotation)
  if keyboard_state.shift:
   camera.position += quaternion_rotate_3d(Vertex3D(0, -movement_speed, 0), camera.rotation)

   
  renderer.draw(camera)
  pygame.display.flip()
  
 pygame.display.quit()
 pygame.quit()
  
if __name__ == "__main__":
 main()