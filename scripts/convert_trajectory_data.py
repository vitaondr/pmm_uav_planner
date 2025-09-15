import csv
import yaml
import numpy as np


def read_csv_file(file_path) -> list:
    data = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append([float(value) for value in row])
    return data


def read_yaml_file(file_path) -> dict:
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return data


def write_yaml_file(file_path, data: dict):
    with open(file_path, "w") as f:
        yaml.dump(data, f)


def project_to_plane(v: np.ndarray, n: np.ndarray) -> np.ndarray:
    nn = n.T @ n
    if nn == 0:
        print("Error: Normal vector is zero.")
        return None
    I = np.eye(3)
    P = I - n @ n.T / nn
    v_p = P @ v

    v_p = v_p / np.linalg.norm(v_p)

    return v_p


def convert_to_R(
    position: np.ndarray, velocity: np.ndarray, acceleration: np.ndarray
) -> np.ndarray:
    # Placeholder for actual conversion logic
    print("Position:", position)
    print("Velocity:", velocity)
    print("Acceleration:", acceleration)
    z_axis = acceleration / np.linalg.norm(acceleration)
    x_axis = project_to_plane(velocity, z_axis)
    if x_axis is None:
        print("Error: Cannot project onto plane.")
        return []

    y_axis = np.cross(z_axis, x_axis)
    if np.linalg.norm(y_axis) == 0:
        print("Error: Y-axis is zero.")
        return []

    R = np.column_stack((x_axis, y_axis, z_axis))

    return R

    return [0.0, 0.0, 0.0, 1.0]


if __name__ == "__main__":
    INPUT_CSV_PATH = "scripts/trajectory_data/sampled_trajectory.csv"
    INPUT_YAML_PATH = "config/raw_waypoints/input.yaml"
    OUTPUT_YAML_PATH = "scripts/yaml_trajectory_data/output.yaml"

    csv_data = read_csv_file(INPUT_CSV_PATH)
    yaml_data = read_yaml_file(INPUT_YAML_PATH)

    camera_positions = yaml_data[5]["camera_positions"]

    for point in csv_data:
        print(point)
        position = np.array(point[1:4])
        velocity = np.array(point[4:7])
        acceleration = np.array(point[7:10])

        rotation = convert_to_quaternion(position, velocity, acceleration)
