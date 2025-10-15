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
