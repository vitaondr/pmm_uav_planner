from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq

import yaml

ruamel_yaml = YAML()
ruamel_yaml.width = 4096          # avoid line wrapping

def flow(seq):
    s = CommentedSeq(seq)
    s.fa.set_flow_style()   # force [a, b, c] style
    return s

def read_yaml_file(file_path) -> dict:
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data


def write_yaml_file(file_path, data: dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        ruamel_yaml.dump(data, f)


if __name__ == "__main__":
    INPUT_PATH = "config/raw_waypoints/input.yaml"
    OUTPUT_PATH = "config/waypoints/output.yaml"

    yaml_data = read_yaml_file(INPUT_PATH)

    start = yaml_data[0]["start"]
    goal = yaml_data[1]["goal"]


    points = []
    for point in yaml_data[4]["path"]:
        points.append([float(point["x"]), float(point["y"]), float(point["z"])])

    new_data = {
        "start": {"position": flow(start), "velocity": flow([0.0, 0.0, 0.0])},
        "end": {"position": flow(goal), "velocity": flow([0.0, 0.0, 0.0])},
        "waypoints": flow(points)
    }
    write_yaml_file(OUTPUT_PATH, new_data)