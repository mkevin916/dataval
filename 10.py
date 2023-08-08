input_file = input("Enter the name of the input file: ")

with open(input_file, 'r') as file:
    data = file.read()

data = data[10:]

with open('output.txt', 'w') as file:
    file.write(data)