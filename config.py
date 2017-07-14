import yaml

class Config:
    def __init__(self, file):
        with open('tree.yaml', 'r') as f:
            doc = yaml.load(f)