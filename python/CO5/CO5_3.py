def read_and_print_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        lines = file.readlines()

        for line in lines:
            # Split the line into a list of strings using a comma as the delimiter
            row = line.strip().split(',')
            print(row)

# Example usage:
csv_file_path = 'py3.csv'  # Replace with the path to your CSV file
read_and_print_csv(csv_file_path)