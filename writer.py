def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    write_to_file("test.txt", "Hello, World!")
    print(read_from_file("test.txt"))