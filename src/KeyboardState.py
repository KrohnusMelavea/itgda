import pygame

class KeyboardState:
 w: bool
 a: bool
 s: bool
 d: bool
 space: bool
 shift: bool
 u_arrow: bool
 r_arrow: bool
 d_arrow: bool
 l_arrow: bool
 q: bool
 e: bool
 k1: bool
 k2: bool
 k3: bool
 k4: bool
 k5: bool
 k6: bool
 
 def __init__(this):
  state = pygame.key.get_pressed()
  this.w = state[pygame.K_w]
  this.a = state[pygame.K_a]
  this.s = state[pygame.K_s]
  this.d = state[pygame.K_d]
  this.space = state[pygame.K_SPACE]
  this.shift = state[pygame.K_LSHIFT] or state[pygame.K_RSHIFT]
  this.u_arrow = state[pygame.K_UP]
  this.r_arrow = state[pygame.K_RIGHT]
  this.d_arrow = state[pygame.K_DOWN]
  this.l_arrow = state[pygame.K_LEFT]
  this.q = state[pygame.K_q]
  this.e = state[pygame.K_e]
  this.k1 = state[pygame.K_1]
  this.k2 = state[pygame.K_2]
  this.k3 = state[pygame.K_3]
  this.k4 = state[pygame.K_4]
  this.k5 = state[pygame.K_5]
  this.k6 = state[pygame.K_6]
 
 def update(this, event_type: int, event_key: int):
  match event_type:
   case pygame.KEYUP:
    match event_key:
     case pygame.K_w:
      this.w = False
     case pygame.K_a:
      this.a = False
     case pygame.K_s:
      this.s = False
     case pygame.K_d:
      this.d = False
     case pygame.K_SPACE:
      this.space = False
     case pygame.K_LSHIFT:
      this.shift = False
     case pygame.K_RSHIFT:
      this.shift = False
     case pygame.K_UP:
      this.u_arrow = False
     case pygame.K_RIGHT:
      this.r_arrow = False
     case pygame.K_DOWN:
      this.d_arrow = False
     case pygame.K_LEFT:
      this.l_arrow = False
     case pygame.K_q:
      this.q = False
     case pygame.K_e:
      this.e = False
     case pygame.K_1:
      this.k1 = False
     case pygame.K_2:
      this.k2 = False
     case pygame.K_3:
      this.k3 = False
     case pygame.K_4:
      this.k4 = False
     case pygame.K_5:
      this.k5 = False
     case pygame.K_6:
      this.k6 = False
   case pygame.KEYDOWN:
    match event_key:
     case pygame.K_w:
      this.w = True
     case pygame.K_a:
      this.a = True
     case pygame.K_s:
      this.s = True
     case pygame.K_d:
      this.d = True
     case pygame.K_SPACE:
      this.space = True
     case pygame.K_LSHIFT:
      this.shift = True
     case pygame.K_RSHIFT:
      this.shift = True
     case pygame.K_UP:
      this.u_arrow = True
     case pygame.K_RIGHT:
      this.r_arrow = True
     case pygame.K_DOWN:
      this.d_arrow = True
     case pygame.K_LEFT:
      this.l_arrow = True
     case pygame.K_q:
      this.q = True
     case pygame.K_e:
      this.e = True
     case pygame.K_1:
      this.k1 = True
     case pygame.K_2:
      this.k2 = True
     case pygame.K_3:
      this.k3 = True
     case pygame.K_4:
      this.k4 = True
     case pygame.K_5:
      this.k5 = True
     case pygame.K_6:
      this.k6 = True