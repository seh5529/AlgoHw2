import time
def count_merge(left, right):
    if not len(left):
        return left, 0
    if not len(right):
        return right, 0
    amount = 0
    prefix = [0] * len(left) 
    prefix[0] = left[0] 
    for i in range(1, len(left)): 
        prefix[i] = prefix[i-1] + left[i]
    result = []
    right_index = 0
    left_index = 0
    total = len(left) + len(right)
    while len(result) < total:
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            #how many are left to the right of the left index
            remaining = len(left) - left_index
            #prefix[-1] is the entire prefix left sum, so prefix_total - (prefix of everything before the left_index)
            sum_left = prefix[-1] - (prefix[left_index-1] if left_index > 0 else 0) 
            #
            amount += sum_left + remaining * right[right_index]

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

    #next n numbers are the array
    data = list(map(int, lines[1:amount+1]))
    
    sorted = inverse_count(data)
    print(sorted[1])

