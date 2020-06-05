# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    queryHash = {}

    for query in queries:
        if query not in queryHash:
            queryHash[query] = query
    
    for file in files:
        fileName = file.split('/')[-1]
        if fileName in queryHash:
            result.append(file)


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
