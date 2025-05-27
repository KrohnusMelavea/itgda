from core import Model, read_models

def main():
 MODELS_PATH = "../res/models.json"
 
 models: dict[str, Model] = read_models(MODELS_PATH)
 
 print(models)

if __name__ == "__main__":
 main()