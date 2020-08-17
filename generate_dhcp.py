import yaml
from jinja2 import Template


def load_yaml(file):
    with open(file) as f:
        data = yaml.safe_load(f)
    return data
    

def generate_config(file, data):
    with open(file) as f:
        temp = Template(f.read())
    return temp.render(data)



def main():
    print(load_yaml('quanto.yaml'))
    
    print(generate_config('config_template', load_yaml('quanto.yaml')))
    
    
if __name__ == "__main__":
    main()

