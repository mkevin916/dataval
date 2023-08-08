while True:
    input_file = input("Enter the name of the input file: ")
    if input_file.endswith('.txt'):
        break
    else:
        print("Invalid file type. Please enter a .txt file.")

with open(input_file, 'r') as file:
    data = file.read()

data = data[10:]

with open('output.txt', 'w') as file:
    file.write(data)
