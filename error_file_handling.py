# ERROR HANDLING IN FILE OPERATIONS AND FILE READ AND WRITE

import os

# Define the names for the input and output files.
# input_filename = "input.txt" # We will now get this from the user.
output_filename = "output.txt"

def create_sample_file(filename):
    """
    Creates a simple text file with some content for the program to read.
    This is for demonstration purposes so the program has a file to work with.
    """
    try:
        # Use a 'with' statement for safe and automatic file handling.
        with open(filename, 'w') as f:
            f.write("This is the first line.\n")
            f.write("This line is in lowercase.\n")
            f.write("Let's see what happens to all this text.")
        print(f"Successfully created a sample file: {filename}")
    except IOError as e:
        print(f"Error creating file {filename}: {e}")

def modify_file(input_file, output_file):
    """
    Reads the content of an input file, modifies the text, and writes it to an output file.
    """
    # Check if the input file exists before trying to open it.
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found.")
        return # Exit the function if the file doesn't exist.

    print(f"Reading from {input_file} and writing to {output_file}...")
    try:
        # Step 1: Read the content from the input file.
        with open(input_file, 'r') as f_in:
            # .read() reads the entire content of the file into a single string.
            content = f_in.read()
            # print("Original content:\n", content) # Uncomment to see original content

        # Step 2: Modify the content.
        # .upper() is a string method that converts all characters to uppercase.
        modified_content = content.upper()
        # print("Modified content:\n", modified_content) # Uncomment to see modified content

        # Step 3: Write the modified content to the output file.
        with open(output_file, 'w') as f_out:
            f_out.write(modified_content)
        
        print(f"File modification and saving complete. Check the new file: {output_file}")
    
    except IOError as e:
        # This will catch other I/O errors that might occur.
        print(f"An I/O error occurred: {e}")

# Main part of the program
if __name__ == "__main__":
    # First, get the filename from the user.
    input_filename = input("Please enter the name of the file you want to process: ")
    
    # Then, run the main function to read, modify, and write the files.
    modify_file(input_filename, output_filename)
