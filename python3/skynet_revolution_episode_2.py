# PATH FINDING
# DIJKSTRA

NODES = {}
EXITS = set() # Gateways
DANGER_NODES = set() # Nodes linked to multiple gateways

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in input().split()]
for _ in range(L):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [j for j in input().split()]
    NODES[n1] = {n2} if not n1 in NODES.keys() else NODES[n1] | {n2}
    NODES[n2] = {n1} if not n2 in NODES.keys() else NODES[n2] | {n1}
EXITS = {input() for _ in range(E)}

# Build list of danger nodes, linked with more than 1 exit
for e in EXITS:
    for f in EXITS - {e}:
        common_parent = NODES[e] & NODES[f]
        if common_parent:
            DANGER_NODES |= common_parent


def add_free_children(node, analyzed):
    children = set()
    if (NODES[node] & EXITS):
        for c in NODES[node] - EXITS - analyzed:
            if NODES[c] & EXITS:
                children |= {c} | add_free_children(c, analyzed | {c})
    return children

# Calculate distance between 2 nodes skipping nodes under direct threat
def distance(source, target):
    analyzed = {source}
    sources = {source}
    dist = 0
    while sources:
        children = set()
        for s in sources:
            if s == target: return dist

            analyzed.add(s)
            for n in NODES[s] - analyzed - EXITS:
                children |= {n} | add_free_children(n, analyzed)

        sources = children
        dist += 1
    return dist


def find_closest_danger_node(source):
    closest_danger, min_distance = None, None
    for d in DANGER_NODES:
        dist = distance(source, d)
        if not closest_danger or dist < min_distance:
            closest_danger, min_distance = d, dist
    return closest_danger


def get_next_link(source):
    direct_threat = NODES[source] & EXITS
    if direct_threat:
        return (source, direct_threat.pop())

    danger_node = find_closest_danger_node(source)
    if danger_node:
        DANGER_NODES.remove(danger_node)
        return (danger_node, (NODES[danger_node] & EXITS).pop())

    # Return random exit link
    for e in EXITS:
        if NODES[e]:
            return (e, NODES[e].copy().pop())

# game loop
while True:
    source = input() # The index of the node on which the Skynet agent is positioned this turn
    (n1, n2) = get_next_link(source)
    NODES[n1].remove(n2)
    NODES[n2].remove(n1)
    print("%s %s"%(n1, n2))
