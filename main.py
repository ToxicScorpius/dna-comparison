from itertools import zip_longest

# Reads the file and assigns their value to a string
file_1 = open("homo_sapiens_hbb.fasta", "r")
file_2 = open("pan_troglodytes_hbb.fasta", "r")
str_file_1 = file_1.read()
str_file_2 = file_2.read()

# Deletes all line breaks
str_file_1 = str_file_1.replace("\n", "")
str_file_2 = str_file_2.replace("\n", "")

files_list = [str_file_1, str_file_2]

# Defines the amount of matches and differences
n_match, n_diff = 0, 0

print(str_file_1)
print(str_file_2)

# Associates each character to one another and shows differences
# Then counts the amount of matches and differences
for n_iter, (c_str1, c_str2) in enumerate(zip_longest(str_file_1, str_file_2), 1):
    if c_str1 != c_str2:
        print(f"{n_iter}: {c_str1}, {c_str2}")
        n_diff += 1
    else:
        n_match += 1

# Displays the amount of differences
print(f"{n_diff} differences")

# Displays the percentage of similarity, with a 2 digits precision
longest_str = max(files_list, key=len)
similarity = "{:.2f}".format(n_match * 100 / len(longest_str))
print(f"{similarity}% similar")
