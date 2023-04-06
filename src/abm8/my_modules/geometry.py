import math
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
def get_distance(x0, y0, x1, y1):
    euc = math.sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))
    return euc