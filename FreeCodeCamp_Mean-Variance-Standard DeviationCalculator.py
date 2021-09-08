import numpy as np

def calculate(list):
    if len(list) < 9:
        print("List must contain nine numbers.")
    else:
        mask = np.array(list).reshape(3, 3)

        # row
        mean_row = mask.mean(axis=1).tolist()
        var_row = mask.var(axis=1).tolist()
        std_row = mask.std(axis=1).tolist()
        max_row = mask.max(axis=1).tolist()
        min_row = mask.min(axis=1).tolist()
        sum_row = mask.sum(axis=1).tolist()

        # column
        mean_col = mask.mean(axis=0).tolist()
        var_col = mask.var(axis=0).tolist()
        std_col = mask.std(axis=0).tolist()
        max_col = mask.max(axis=0).tolist()
        min_col = mask.min(axis=0).tolist()
        sum_col = mask.sum(axis=0).tolist()

        # element
        mean_ele = mask.mean().tolist()
        var_ele = mask.var().tolist()
        std_ele = mask.std().tolist()
        max_ele = mask.max().tolist()
        min_ele = mask.min().tolist()
        sum_ele = mask.sum().tolist()

        keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

        values = [[mean_row, mean_col, mean_ele], [var_row, var_col, var_ele], [std_row, std_col, std_ele],
                  [max_row, max_col, max_ele], [min_row, min_col, min_ele], [sum_row, sum_col, sum_ele]]

        calculations = dict(zip(keys, values))

    return calculations

calculate([0,1,2,3,4,5,6,7,8])