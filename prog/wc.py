import argparse
import sys

def count_content(content):
    lines = content.count('\n') + 1 if content else 0
    words = len(content.split()) if content else 0
    chars = len(content) if content else 0
    return lines, words, chars

def process_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return count_content(content)
    except FileNotFoundError:
        print(f"File not found: {file_name}", file=sys.stderr)
        return None

def display_results(counts, file_name, args):
    if counts:
        line_str = f"{counts[0]:7}" if args.lines else ""
        word_str = f"{counts[1]:7}" if args.words else ""
        char_str = f"{counts[2]:7}" if args.characters else ""
        print(f"{line_str}{word_str}{char_str} {file_name}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Word Count Program')
    parser.add_argument('files', nargs='+', help='Files to process')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-c', '--characters', action='store_true', help='Count characters')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if not (args.lines or args.words or args.characters):
        args.lines = args.words = args.characters = True

    total = [0, 0, 0]
    for file_name in args.files:
        result = process_file(file_name)
        if result:
            display_results(result, file_name, args)
            total = [sum(x) for x in zip(total, result)]

    if len(args.files) > 1:
        display_results(total, 'total', args)

if __name__ == "__main__":
    main()
