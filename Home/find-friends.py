# "How to find friends" downloaded: Sun Jul 31 18:33:14 2016
def check_connection(network, first, second):
    groups = []
    for a, b in [connection.split("-") for connection in network]:
        foundin = []
        # for each existing set, check if either robut is already in here
        for group in groups:
            if a in group or b in group:
                # mark set for merging
                foundin.append(group)
        # if we found any sets for the robuts, add them into the first
        if len(foundin):
            foundin[0].add(a)
            foundin[0].add(b)
            # merge in any extra sets and remove the originals
            for extra in foundin[1:]:
                foundin[0].update(extra)
                groups.remove(extra)
        # otherwise make a new set and put the robuts in it
        else:
            groups.append({a, b})

    # look for a set with both robuts
    return any({first, second}.issubset(group) for group in groups)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("one-two", "three-four", "two-three", "five-six", "seven-eight"),
        "one", "eight") == True, "it's-a me"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
