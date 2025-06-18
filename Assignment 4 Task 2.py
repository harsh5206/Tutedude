# task2_write_append_file.py

def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print(f"Data successfully written to {filename}.")

def append_to_file(filename):
    more_data = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(more_data + '\n')
    print("Data successfully appended.")

def read_file(filename):
    print("\nFinal content of output.txt:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

filename = "output.txt"
write_to_file(filename)
append_to_file(filename)
read_file(filename)
