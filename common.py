import yaml

___config = None

def config():
    global ___config
    if not ___config:
        with open('config.yaml', mode = 'r') as file:
            ___config = yaml.load(file)
    return ___config
