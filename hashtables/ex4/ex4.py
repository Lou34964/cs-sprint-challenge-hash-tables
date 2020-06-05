def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    result = []
    num_hash = {}

    for num in a:
        fixNum = abs(num)

        if fixNum not in num_hash:
            num_hash[fixNum] = 0
        else:
            num_hash[fixNum] += 1
        
        if num_hash[fixNum] > 0:
            result.append(fixNum)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
