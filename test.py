import os
import subprocess

def run_test(program, input_file, expected_output, mode):
    # Run the program with the input and capture the output and exit status
    if mode == 'stdin':
        with open(input_file, 'r') as file:
            process = subprocess.run(['python', f'prog/{program}.py'], stdin=file, text=True, capture_output=True)
    else:  # mode == 'arg'
        process = subprocess.run(['python', f'prog/{program}.py', input_file], text=True, capture_output=True)
    
    output = process.stdout
    exit_status = process.returncode
    return output == expected_output and exit_status == 0

def main():
    test_dir = 'test/'
    test_results = []
    fail_count = 0

    for filename in os.listdir(test_dir):
        if filename.endswith('.in'):
            prog, _ = filename.split('.', 1)
            test_name = filename[len(prog) + 1:-3]

            with open(os.path.join(test_dir, filename), 'r') as file:
                input_data = file.read()

            with open(os.path.join(test_dir, f'{prog}.{test_name}.out'), 'r') as file:
                expected_output = file.read()

            # Test with STDIN
            if run_test(prog, os.path.join(test_dir, filename), expected_output, 'stdin'):
                test_results.append(f'OK: {prog} {test_name} (stdin)')
            else:
                test_results.append(f'FAIL: {prog} {test_name} (stdin)')
                fail_count += 1

            # Test with argument
            if os.path.exists(os.path.join(test_dir, f'{prog}.{test_name}.arg.out')):
                with open(os.path.join(test_dir, f'{prog}.{test_name}.arg.out'), 'r') as file:
                    expected_output_arg = file.read()

                if run_test(prog, os.path.join(test_dir, filename), expected_output_arg, 'arg'):
                    test_results.append(f'OK: {prog} {test_name} (arg)')
                else:
                    test_results.append(f'FAIL: {prog} {test_name} (arg)')
                    fail_count += 1

    for result in test_results:
        print(result)

    print(f'\nTotal tests: {len(test_results)}')
    print(f'Failed tests: {fail_count}')

    if fail_count > 0:
        exit(1)

if __name__ == '__main__':
    main()
