import csv
import yaml

def read_csv_file(file_path) -> list:
    data = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append([float(value) for value in row])
    return data

def read_yaml_file(file_path) -> dict:
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data

def write_yaml_file(file_path, data: dict):
    with open(file_path, 'w') as f:
        yaml.dump(data, f)



if __name__ == "__main__":
    INPUT_CSV_PATH = "scripts/trajectory_data/sampled_trajectory.csv"
    INPUT_YAML_PATH = "config/raw_waypoints/input.yaml"
    OUTPUT_YAML_PATH = "scripts/yaml_trajectory_data/output.yaml"

    csv_data = read_csv_file(INPUT_CSV_PATH)
    yaml_data = read_yaml_file(INPUT_YAML_PATH)

    camera_positions = yaml_data[5]["camera_positions"]

    