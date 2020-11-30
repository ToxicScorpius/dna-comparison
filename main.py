from itertools import zip_longest
import random
import string

# Strings consist of selected characters
letters = string.ascii_lowercase

# Generates 2 strings of random length and characters
string1 = "".join(random.choice(letters) for i in range(random.randint(1, 20)))
string2 = "".join(random.choice(letters) for i in range(random.randint(1, 20)))
# Makes a list with these strings
list_str = [string1, string2]

# Defines the amount of matches and differences
n_match, n_diff = 0, 0

print(string1)
print(string2)

# Associates each character to one another and shows differences
# Then counts the amount of matches and differences
for n_iter, (c_str1, c_str2) in enumerate(zip_longest(string1, string2)):
    if c_str1 != c_str2:
        print(f"{n_iter}: {c_str1}, {c_str2}")
        n_diff += 1
    else:
        n_match += 1

# Displays the amount of differences
print(f"{n_diff} differences")

# Displays the percentage of similarity
longest_str = max(list_str, key=len)
similarity = "{:.2f}".format(n_match * 100 / len(longest_str))
print(f"{similarity}% similar")
