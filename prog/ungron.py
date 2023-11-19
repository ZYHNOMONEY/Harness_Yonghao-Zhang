import json
import argparse


def ungron(lines):
    result = {}

    for line in lines:
        path, value = line.split(' = ')
        value = json.loads(value)
        keys = path.split('.')
        current_level = result

        for i, key in enumerate(keys):
            if '[' in key:
                key, index = key.split('[')
                # remove the closing bracket and convert to int
                index = int(index[:-1])
                current_level = current_level.setdefault(key, [])

                if len(current_level) <= index:
                    current_level.extend(
                        [{}] * (index + 1 - len(current_level)))

                if i == len(keys) - 1:
                    current_level[index] = value
                else:
                    current_level = current_level[index]
            else:
                if i == len(keys) - 1:
                    current_level[key] = value
                else:
                    current_level = current_level.setdefault(key, {})

    return result


parser = argparse.ArgumentParser(
    description="Ungron: Convert flattened JSON back to structured JSON")
parser.add_argument('filename', help="File containing flattened JSON")

args = parser.parse_args()

with open(args.filename, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

ungroned_data = ungron(lines)
print(json.dumps(ungroned_data, indent=4))