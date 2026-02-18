
def count_merge(left, right):
    if not len(left):
        return left, 0
    if not len(right):
        return right, 0
    amount = 0
    result = []
    right_index = 0
    left_index = 0
    total = len(left) + len(right)
    while len(result) < total:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            temp = left_index
            while temp < len(left):
                amount += left[temp] + right[right_index]
                # print(total)
                temp += 1

            result.append(right[right_index])
            right_index += 1
        if left_index == len(left):
            # if left[left_index - 1] > right[right_index]:
            #     total = left[left_index - 1] + right[right_index]
            #     print(total)
            result.extend(right[right_index:])
            break
        if right_index == len(right):
            # if left[left_index] > right[right_index - 1]:
            #     total = left[left_index] + right[right_index - 1]
            #     print(total)
            result.extend(left[left_index:])
            break
    return result, amount

def inverse_count(data):
    if len(data) < 2:
        return data, 0
    
    mid = len(data)//2
    left, left_amount= inverse_count(data[0:mid])
    right, right_amount = inverse_count(data[mid:])

    merged, merge_weight = count_merge(left, right)
    return merged, left_amount + right_amount + merge_weight

if __name__ == "__main__":
    import sys

    # Read all lines from stdin
    lines = sys.stdin.read().strip().split()

    #the length is the first line
    amount = int(lines[0])
    if amount <= 1000:

        #next n numbers are the array
        data = list(map(int, lines[1:amount+1]))
        
        sorted = inverse_count(data)
        print(sorted[1])

