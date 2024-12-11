# Function to flatten a nested list
def flatten_nested_list(nested_list):
    """
    This function takes a nested list as input and returns a flattened list.

    Parameters:
    nested_list (list): The list which may contain other nested lists.

    Returns:
    list: A single flattened list containing all elements.
    """
    # Initialize an empty list to store flattened elements
    flattened = []

    # Iterate through each element in the input list
    for item in nested_list:
        # Check if the current item is a list
        if isinstance(item, list):
            # If item is a list, recursively call the function to flatten it
            flattened.extend(flatten_nested_list(item))
        else:
            # If item is not a list, append it to the flattened list
            flattened.append(item)

    # Return the flattened list
    return flattened


# Example nested list
nested_list = [1, [2, 3], [4, [5, 6]], 7]

# Call the function to flatten the nested list
flattened_list = flatten_nested_list(nested_list)

# Output the result
print("Nested List:", nested_list)
print("Flattened List:", flattened_list)
