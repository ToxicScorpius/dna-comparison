from itertools import zip_longest
import timeit

start = timeit.default_timer()

# Opens the file, ignores the header and turns lines into iterables
def iter_adn_seq(path):
    with open(path) as file:
        for line in file:
            if line.startswith(">"):
                continue
            yield from line.strip()

n_diff, n_match = 0, 0

# Associates each character to one another and shows differences
# Then counts the amount of matches and differences
for n_iter, (c_str1, c_str2) in\
        enumerate(zip_longest(iter_adn_seq("sars_cov2.fasta"), iter_adn_seq("sars_tor2.fasta")), 1):
    if c_str1 != c_str2:
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
