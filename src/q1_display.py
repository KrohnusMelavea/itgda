from core import read_models
from ShaderSet import ShaderSet
from Renderer import Renderer
from Entity import Entity
from Vertex3D import Vertex3D
from Camera import Camera
from KeyboardState import KeyboardState
import pygame
import time
import math

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
   Entity(Vertex3D(0, 0, -5), "cube")
  ]
 )
 
 keyboard_state = KeyboardState()
 camera = Camera(position=Vertex3D(0, 0, 0), rotation = Vertex3D(0, math.pi * 1.5, 0))
 movement_speed = 0.005
 rotation_speed = 0.001
 
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
  
  if keyboard_state.l_arrow:
   camera.rotation.y -= rotation_speed
  if keyboard_state.r_arrow:
   camera.rotation.y += rotation_speed
  if keyboard_state.w:
   camera.position.x += movement_speed * math.cos(camera.rotation.y)
   camera.position.z += movement_speed * math.sin(camera.rotation.y)
  if keyboard_state.a:
   camera.position.x += movement_speed * math.cos(camera.rotation.y + math.pi * 1.5)
   camera.position.z += movement_speed * math.sin(camera.rotation.y + math.pi * 1.5)
  if keyboard_state.s:
   camera.position.x += movement_speed * math.cos(camera.rotation.y + math.pi)
   camera.position.z += movement_speed * math.sin(camera.rotation.y + math.pi)
  if keyboard_state.d:
   camera.position.x += movement_speed * math.cos(camera.rotation.y + math.pi * 0.5)
   camera.position.z += movement_speed * math.sin(camera.rotation.y + math.pi * 0.5)
  if keyboard_state.space:
   camera.position.y += movement_speed
  if keyboard_state.shift:
   camera.position.y -= movement_speed
   
  renderer.draw(camera)
  pygame.display.flip()
  
 pygame.display.quit()
 pygame.quit()
  
if __name__ == "__main__":
 main()