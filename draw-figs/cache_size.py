import sys
# import matplotlib.pyplot as plt

if __name__ == "__main__":
    cache_size = []
    load_reactive = []
    load_subpub = []
    load_freshness = []
    load_nocache = []

    hitratio_reactive = []
    hitratio_subpub = []
    hitratio_freshness = []
    hitratio_nocache = []
    
    f = open(r"draw-figs/cache_size.txt")
    line = f.readline()
        line = line.split(" ")
        cache_size.append(int(line[1]))
        seq = line[8][:-1]
        name = line[14][:-1]

        line = f.readline()
    
    f.close()