def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

my_string = "Hello World"
vowel_count = count_vowels(my_string)
print(f"The number of vowels is: {vowel_count}")

# Second

stringer = "hello"
vowels = "aeiou"

for i in stringer:
    if i in vowel:
        print(f"Vowel Found: {i}")

#3rd

def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    return v_count, c_count

# Example usage:
print(count_vowels_consonants("Hello World"))  # Output: (3, 7)
