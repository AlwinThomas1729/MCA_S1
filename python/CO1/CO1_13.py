# Take comma-separated color names input from the user
input_color_names = input("Enter comma-separated color names: ")

# Create a list of colors
color_list = input_color_names.split(',')

if color_list:
    # Display the first and last colors
    print("First color:", color_list[0])
    print("Last color:", color_list[-1])
else:
    print("No colors entered.")
