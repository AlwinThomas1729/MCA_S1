def write_dict_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        # Write header
        header = list(data.keys())
        file.write(','.join(header) + '\n')

        # Write data
        values = [str(data[key]) for key in header]
        file.write(','.join(values) + '\n')

def read_and_display_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        lines = file.readlines()

        # Display header
        header = lines[0].strip().split(',')
        print(f"Header: {header}")

        # Display data
        data = lines[1].strip().split(',')
        print(f"Data: {data}")

# Example usage:
csv_file_path = 'example.csv'  # Replace with the desired CSV file path
data_to_write = {'Name': 'John', 'Age': 25, 'City': 'New York'}

# Write the dictionary to CSV
write_dict_to_csv(csv_file_path, data_to_write)

# Read and display the CSV content
read_and_display_csv(csv_file_path)
