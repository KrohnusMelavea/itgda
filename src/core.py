from Model import Model
import json

def read_file(file_path: str) -> str:
 data = None
 with open(file_path, "r") as file_handler:
  data = file_handler.read()
 return data
def read_json(file_path: str) -> dict:
 return json.loads(read_file(file_path))
def read_models(file_path: str) -> dict[str, Model]:
 data: dict = read_json(file_path)
 return dict(
  (name, Model.from_json(model)) 
  for name, model in data.items()
 )