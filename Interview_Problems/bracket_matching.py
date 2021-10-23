# Function to check if some sequence of brackets is valid or not
# Runs in O(n) time, O(n) space where
# n := length of string
def is_valid(brackets):
    # Initialize stack
    stack = []

    # Iterate through string
    for b in brackets:

        # If you find an open bracket, add it to stack
        if b in "[({":
            stack.append(b)
        else:
            
            # If there is a close bracket with no open, test fails
            if len(stack) == 0:
                return False

            # If there is a closing bracket that matches the recent open bracket,
            # pop from stack and continue iterations
            elif (b == "]" and stack[~0] == "[") or (b == ")" and stack[~0] == "(") or (b == "}" and stack[~0] == "{"):
                stack.pop()
                continue
            
            # Otherwise no good, fail test
            else:
                return False

    # Return true if there are no opens left on the stack
    return len(stack) == 0

print(is_valid("]("))