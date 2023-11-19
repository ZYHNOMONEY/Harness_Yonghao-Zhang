import os
import subprocess
import sys

def run_test(program, input_file, expected_output):
    command = ['python', f'prog/{program}.py']

    with open(input_file, 'r') as file:
        process = subprocess.run(command, stdin=file, text=True, capture_output=True)

    output = process.stdout
    return output == expected_output and process.returncode == 0

def main():
    test_dir = 'test/'
    test_results = []
    fail_count = 0

    for filename in os.listdir(test_dir):
        if filename.endswith('.in'):
            # Construct program name and test case name
            prog, test_name = os.path.splitext(filename)[0].split('.', 1)

            input_file_path = os.path.join(test_dir, filename)
            output_file_path = os.path.join(test_dir, f'{prog}.{test_name}.out')

            # Reading expected output
            with open(output_file_path, 'r') as file:
                expected_output = file.read()

            # Run test
            if run_test(prog, input_file_path, expected_output):
                test_results.append(f'OK: {prog} {test_name}')
            else:
                test_results.append(f'FAIL: {prog} {test_name}')
                fail_count += 1

    # Print test results
    for result in test_results:
        print(result)

    print(f'\nTotal tests: {len(test_results)}')
    print(f'Failed tests: {fail_count}')

    if fail_count > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
