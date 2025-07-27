# Define the global variable
counter = 0

def change_counter():
    global counter  # Declare that we're using the global variable
    counter += 1    # Modify the global variable

# Example usage:
print("Before:", counter)
change_counter()
print("After:", counter)