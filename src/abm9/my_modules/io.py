import csv

# Read input data
def read_data():
    f = open('/Users/zivarhagverdiyeva/Documents/python/data/input/in.txt', newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row=[]
        for value in line:
            row.append(value)
            
        data.append(row)
        n_rows=len(data)
        n_cols=len(row)
    print("Number of rows: ", n_rows)
    print("Number of columns: ", n_cols)        
    f.close()
    #print(data)
    return data, n_rows, n_cols

def write_data(filepath, environment):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in environment:
            writer.writerow(row)
    