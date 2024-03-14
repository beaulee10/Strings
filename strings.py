def main():
    string_statement = "Welcome to Python!"
    
    print("Iterating through the string:")
    for char in string_statement:
        print(char, end=' ')
    
    print("\nCharacter with the minimum ASCII value:")
    minimum_char = min(string_statement)
    print(minimum_char)
    
    print("\nCharacter with the maximum ASCII value:")
    maximum_char = max(string_statement)
    print(maximum_char)
    
    print("\nIndex of 'o':")
    o_count = string_statement.index('o')
    print(o_count)
    
    print("\nConverting string to a list of characters:")
    char_list = list(string_statement)
    print(char_list)
    
    print("\nCount of 'o' in the string:")
    count_of_o = string_statement.count('o')
    print(count_of_o)

main()