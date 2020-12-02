from itertools import zip_longest
import timeit

start = timeit.default_timer()


# Opens the file, ignores the header and turns lines into iterables
def iter_dna_seq(path):
    with open(path) as file:
        for line in file:
            if line.startswith(">"):
                continue
            yield from line.strip()


# Counts the number of characters in the file, line by line
def dna_seq_len(path):
    file_len = 0
    with open(path) as file:
        for line in file:
            line = line.rstrip("\r\n")  # Deletes line breaks
            file_len += len(line)  # Adds line characters count to total
        return file_len


n_diff, n_match = 0, 0

# Associates each character to one another and shows differences
# Then counts the amount of matches and differences
for n_iter, (c_str1, c_str2) in\
        enumerate(zip_longest(iter_dna_seq("a.txt"),
                              iter_dna_seq("b.txt")),
                  1):
    if c_str1 != c_str2:
        if c_str1 is None or c_str2 is None:  # If a file ends
            longest_str = max(dna_seq_len("a.txt"), dna_seq_len("b.txt"))
            shortest_str = min(dna_seq_len("a.txt"), dna_seq_len("b.txt"))
            n_diff += (longest_str - shortest_str)
            break
        print(f"{n_iter}: {c_str1}, {c_str2}")
        n_diff += 1

    else:
        n_match += 1

# Displays the amount of differences
print(f"{n_diff} differences")

# Displays the percentage of similarity, with a 2 digits precision
similarity = "{:.2f}".format(n_match * 100 / n_iter)
print(f"{similarity}% similar")

stop = timeit.default_timer()
print(f"Time: {stop - start}s")
