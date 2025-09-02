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

import asyncio

async def chunk_text_async(text, chunk_size=1000):
    """
    Asynchronously chunk long text into pieces of at most chunk_size characters.
    Yields each chunk.
    """
    for i in range(0, len(text), chunk_size):
        await asyncio.sleep(0)  # Yield control to event loop
        yield text[i:i+chunk_size]

# Example usage:
# async for chunk in chunk_text_async(long_text, 1024):
#     process(chunk)

def parser_output(text):
    return text.split('\n')


if __name__ == "__main__":
    try:
        write_to_file("test.txt", "Hello, World!\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

    try:
        append_to_file("test.txt", "Hello my name is Yosef\n")
    except Exception as e:
        print(f"Error appending to file: {e}")


    while True:
        input_text = input("Enter your text: ")
        if input_text == "exit":
            break
        
        # Try to convert to integer, handle errors gracefully
        try:    
            val = int(input_text)
            print(f"Converted to integer: {val}")
        except ValueError:
            print(f"'{input_text}' is not a valid integer, storing as text")
        
        append_to_file("test.txt", input_text + "\n")
    
    print(read_from_file("test.txt"))

