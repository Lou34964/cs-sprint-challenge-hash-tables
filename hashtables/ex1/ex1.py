def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    Wcache = {}

    for i in range(len(weights)):

        weight = weights[i]

        if weight in Wcache:

            Pi = Wcache[weight]

            return (i, Pi)
        
        Wcache[limit - weight] = i

    return None

if __name__ == "__main__":
    ws = [10,21,30,45,2]
    l = 5
    li = 66
    print(get_indices_of_item_weights(ws,l,li))