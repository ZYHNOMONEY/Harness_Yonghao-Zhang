import json
import sys

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
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

def main():

    try:
        # Determine input source (file or STDIN)
        file_path = sys.argv[1] if len(sys.argv) > 1 else None
        json_data = read_json_input(file_path)

        # Flatten the JSON data
        flattened_data = flatten_json(json_data)

        # Output the flattened JSON
        for k, v in flattened_data.items():
            print(f"json.{k} = {json.dumps(v)}")
    except Exception as e:
        print(f"Error:{e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
