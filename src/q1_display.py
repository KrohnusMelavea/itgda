from core import read_models
from Renderer import Renderer

def main():
 MODELS_PATH = "../res/models.json"
 
 renderer = Renderer(
  read_models(MODELS_PATH)
 )
 renderer.draw("cube")

if __name__ == "__main__":
 main()