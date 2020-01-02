import sys

if __name__ == "__main__":
    f = open(r"reactive/out_reactive.log")
    line = f.readline()

    hits = 0.0
    misses = 0.0

    loads = 0.0
    responding_loads = 0.0
    all_messages = 0.0
    expiration_messages = 0.0

    valid_messages = 0.0

    while line:
        if "onContentStoreHit interest" in line:
            hits += 1
        elif "onContentStoreMiss" in line:
            misses += 1
        elif "allMessages" in line:
            all_messages += 1
        elif "expirationMessages" in line:
            expiration_messages += 1
        elif "validMessages" in line:
            valid_messages += 1
        elif "responding with Data" in line:
            responding_loads += 1
        line = f.readline()
    
    f.close()

    print(hits)
    print(misses)
    print(hits/(hits+misses))
    print(all_messages)
    print(expiration_messages)
    print(valid_messages)
    print(responding_loads)
    print(expiration_messages+responding_loads)