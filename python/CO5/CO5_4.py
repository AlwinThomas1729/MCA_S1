def read_and_print_columns(file_path, columns):
    with open(file_path, 'r', newline='') as file:
        lines = file.readlines()
        for line in lines:
            row = line.strip().split(',')
            selected_columns = [row[column - 1] for column in columns]
            print(selected_columns)
csv_file_path = 'py3.csv'  # Replace with the path to your CSV file
selected_columns = [1, 3]  # Replace with the column numbers you want to extract (1-indexed)

read_and_print_columns(csv_file_path, selected_columns)
 