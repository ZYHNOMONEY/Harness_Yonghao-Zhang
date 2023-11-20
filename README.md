## Name: Yonghao Zhang
## Stevens login: yzhang8
##  URL: https://github.com/ZYHNOMONEY/Harness_Yonghao-Zhang
##  Time spent: 18h
##  Code Test:
 ### Word_count program: 
* 1: tested **`count_content` Function:**    Takes a string `content` as input. Counts the number of lines, words, and characters in the `content`.Returns these counts as a tuple.
* 2:tested **`process_file` Function:**   Tries to open and read the contents of the file. If successful, calls `count_content` with the file's content and returns the result.
* 3:tested **`parse_arguments` Function:**  Adds options to count lines (`-l` or `--lines`), words (`-w` or `--words`), and characters (`-c` or `--characters`). Returns the parsed arguments.
### Gron program:
* 1:tested **`flatten_json` Function:**   Take a JSON file and recursively flattens the JSON structure, converting nested objects and arrays into a flat dictionary with dot-separated keys. Returns the flattened dictionary.
* 2:tested **`read_json_input` Function:**   Takes an optional file path.  If a file path is provided, reads JSON data from the file. Otherwise, reads JSON data from the standard input (`sys.stdin`). Returns the loaded JSON data.
* 3:tested **`parse_arguments` Function:**  Sets up an argument parser for the script. Defines an optional argument `--obj` to specify the base object name, with a default value of 'json'. Defines a positional argument `file` for the JSON file to process. This argument is optional and defaults to `None`. Returns the parsed arguments.
### Ungron program:
* 1:tested **`ungron` Function:**    Accepts a list of lines, each representing a flattened JSON key-value pair. Splits each line into a path and a value. The value is converted back into a JSON object using `json.loads`. Returns the reconstructed, nested JSON object.
* 2:tested **Argument Parsing:**    The script uses `argparse` to define a command-line interface. It requires one argument, `filename`, which is the path to the file containing the flattened JSON data.
## Issues can not resolve:
* `ungron` and `wc` can not pass CI. After long time debug....it finally workout.
##  Example issue solved:
In flattened JSON, nested structures are reduced to a single level. During reconstruction, it’s important to correctly identify and create nested dictionaries or arrays, ensuring the consistency of the data structure. the nested structure reconstruction is handled by the `create_structure` function. This function is designed to take a base path and a dictionary representing a directory structure, and then it creates the corresponding directories and files on the file system.
##  Extensions：
* 1: wc multiple files.
* 2: wc flags to control output.
* 3: gron control the base-object name.