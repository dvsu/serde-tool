import yaml
import json


source_dir = './example.json'
source = None


with open(source_dir, 'r') as source_file:
    source = json.load(source_file)

with open('example.yaml', 'w') as example_yaml:
    yaml.safe_dump(source, example_yaml)
