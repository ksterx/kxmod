import yaml


class YAMLEditor:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            return yaml.load(f)
