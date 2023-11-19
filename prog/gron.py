import json
import sys
import argparse

def flatten_json(y, base_obj_name):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '.')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '.')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def read_json_input(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return json.load(sys.stdin)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Flatten JSON with a custom base object name.')
    parser.add_argument('--obj', default='json', help='Specify the base object name.')
    parser.add_argument('file', nargs='?', help='The JSON file to process.', default=None)
    return parser.parse_args()

def main():
    try:
        args = parse_arguments()

        json_data = read_json_input(args.file)

        flattened_data = flatten_json(json_data, args.obj)

        for k, v in flattened_data.items():
            print(f"{args.obj}.{k} = {json.dumps(v)}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
