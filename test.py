import random

def random_array(n, low=0, high=1000):
    """Return a list of n random integers between low and high."""
    return [random.randint(low, high) for _ in range(n)]

def write_input_file(n, filename="./input.txt", low=0, high=1000):
    """Generate a random array and write it to an input.txt file in HW2 format."""
    arr = random_array(n, low, high)

    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        f.write(" ".join(map(str, arr)) + "\n")

    return arr  # optional, so you can see what was generated
arr = write_input_file(1000000)