# Function to check if two strings are isomorphic
def is_isomorphic(s, t):
    if len(s) != len(t):  # If lengths are different, they cannot be isomorphic
        return False
    
    # Create two dictionaries to map characters from s to t and vice versa
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Check if the mapping from s to t is consistent
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check if the mapping from t to s is consistent
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

# Input two strings
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check if the strings are isomorphic
if is_isomorphic(s, t):
    print(f"'{s}' and '{t}' are isomorphic.")
else:
    print(f"'{s}' and '{t}' are NOT isomorphic.")