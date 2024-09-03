def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

# Test cases
print(is_valid("{}()[]"))  
print(is_valid("{(){}[]}"))
print(is_valid("([()])")) 
print(is_valid("[]{(})")) 
print(is_valid("[]{{{}}()}(())")) 