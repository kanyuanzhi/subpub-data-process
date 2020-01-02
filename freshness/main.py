import sys

if __name__ == "__main__":
    f = open(r"freshness/out_freshness.log")
    line = f.readline()

    hits = 0.0
    misses = 0.0

    loads = 0.0

    expiration_loads = 0.0

    while line:
        if "onContentStoreHit" in line:
            hits += 1
        elif "onContentStoreMiss" in line:
            misses += 1
        elif "responding with Data" in line or "publication data" in line:
            loads += 1
        elif "expirationMessage" in line:
            expiration_loads += 1
        line = f.readline()
    
    f.close()

    print(hits/(hits+misses))
    print(loads)
    print(expiration_loads)