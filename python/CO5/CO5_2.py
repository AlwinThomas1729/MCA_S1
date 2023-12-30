def copy_odd_lines(input_file, output_file):
    with open(input_file, 'r') as input_fp, open(output_file, 'w') as output_fp:
        lines = input_fp.readlines()

        odd_lines = []
        for index, line in enumerate(lines):
            if index % 2 == 0:
                odd_lines.append(line)

        output_fp.writelines(odd_lines)

# Example usage:
input_file_path = 'py.txt'  # Replace with the path to your input file
output_file_path = 'output.txt'  # Replace with the desired output file path

copy_odd_lines(input_file_path, output_file_path)
