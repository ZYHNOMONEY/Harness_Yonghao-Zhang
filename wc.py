def word_count(filename):
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

        return num_lines, num_words, num_chars
    except FileNotFoundError:
        return "File not found."