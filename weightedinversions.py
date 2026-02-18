
def merge(left, right):
    total = 0
    if not len(left):
        return left
    if not len(right):
        return right
    
    result = []
    right_index = 0
    left_index = 0
    total = len(left) + len(right)
    while len(result) < total:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            #if the left index is greater than the right index, meaning i<j and bi>bj
            
            total += left[left_index] + right[right_index]
            print(total)
            result.append(right[right_index])
            right_index += 1
        if left_index == len(left):
            result.extend(right[right_index:])
            break
        if right_index == len(right):
            result.extend(left[left_index:])
            break
    return result

def main(data):

    if len(data) < 2:
        return data
    
    mid = len(data)//2
    left= main(data[0:mid])
    right = main(data[mid:])

    merged = merge(left, right)
    print("hi")
    return merged

if __name__ == "__main__":
    import sys

    # Read all lines from stdin
    lines = sys.stdin.read().strip().split()

    # First number is n
    n = int(lines[0])

    # The next n numbers are the array
    data = list(map(int, lines[1:n+1]))

    # Now call your merge-sort function
    result = main(data)

    # Print the sorted result (or whatever output the assignment requires)
    print(result)

