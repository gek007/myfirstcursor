def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)

def parser_input(text):
    return text.split('\n')

def parser_output(text):
    return text.split('\n')



if __name__ == "__main__":
    write_to_file("test.txt", "Hello, World!\n")
    append_to_file("test.txt", "Hello my name is Yosef\n")
    input_text = input("Enter your text: ")
    append_to_file("test.txt", input_text)
    print(read_from_file("test.txt"))

