#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    tripCache = {}
    route = []

    for t in tickets:
        if t.source not in tripCache:
            tripCache[t.source] = t.destination
            if t.source is 'NONE':
                route.append(t.destination)
    
    for i in range(0, length):
        if len(route) == length:
            return route
        
        route.append(tripCache[route[i]])
