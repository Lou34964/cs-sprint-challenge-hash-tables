# import hashtable

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # ht = hashtable.HashTable(8)

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









# def has_negatives(a):
#     """
#     YOUR CODE HERE
#     """
#     # Your code here
#     ht = hashtable.HashTable(8)

#     # print(f"\n\na: {a}\n\n")

#     result = []
#     num_hash = {}

#     for num in a:
#         fixNum = abs(num)

#         if fixNum not in ht.storage:
#             print(f'fixNum: {str(fixNum)}')
#             ht.put(str(fixNum),0)
#             # num_hash[fixNum] = 0
#         else:
#             ht.storage[ht.get(str(fixNum))] += 1
#             # num_hash[fixNum] += 1
        
#         if ht.storage[str(fixNum)] > 0:
#             result.append(fixNum)

#     return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
