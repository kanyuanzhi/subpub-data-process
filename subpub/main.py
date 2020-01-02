import sys

if __name__ == "__main__":
    f = open(r"subpub/out_subpub.log")
    line = f.readline()

    hits = 0.0
    misses = 0.0

    loads = 0.0
    responding_loads = 0.0
    publicating_loads = 0.0

    expiration_loads = 0.0

    while line:
        if "onContentStoreHit" in line:
            hits += 1
        elif "onContentStoreMiss" in line:
            misses += 1
        elif "responding with Data" in line:
            responding_loads += 1
        elif "publication data" in line:
            publicating_loads += 1
        elif "expirationMessage" in line:
            expiration_loads += 1
        line = f.readline()
    
    f.close()

    print(hits/(hits+misses))
    print(responding_loads)
    print(publicating_loads)
    print(responding_loads+publicating_loads)
    print(expiration_loads)