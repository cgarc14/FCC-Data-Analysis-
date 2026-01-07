import numpy as np

def calculate(list):

    #   Makes 'np.float64' not show while printing the output
    np.set_printoptions(legacy='1.25')

    #   Required exception for length of list 
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #   Turn list into a 3x3 Numpy array
    array = np.array(list).reshape(3,3)

    #   Get two arrays: one with the columns and the other with the rows of the 3x3 array
    axis1 = [col for col in array.T]
    axis2 = [row for row in array]

    #   The values to calculate. They are nested, empty lists that will be filled with their respective calculated values
    mean = [[], [], 0]
    variance = [[], [], 0]
    std_dev = [[], [], 0]
    max = [[], [], 0]
    min = [[], [], 0]
    total = [[], [], 0]


    #   Iterate over the columns to calculate each value and append it to it's list
    for i in axis1:

        current_mean = i.sum() / len(i)
        mean[0].append(current_mean)
        variance[0].append(((i-current_mean)**2).sum() / len(i))
        std_dev[0].append((((i-current_mean)**2).sum() / len(i))**0.5)
        max[0].append(i.max())
        min[0].append(i.min())
        total[0].append(i.sum())

    #   Same thing for the rows
    for j in axis2:

        current_mean = j.sum() / len(j)
        mean[1].append(current_mean)
        variance[1].append(((j-current_mean)**2).sum() / len(j))
        std_dev[1].append((((j-current_mean)**2).sum() / len(j))**0.5)
        max[1].append(j.max())
        min[1].append(j.min())
        total[1].append(j.sum())

    #   The 'flattened' values. They represent the original list instead of parts of the array
    mean[2] = sum(list) / len(list)
    variance[2] = sum([(value-mean[2])**2 for value in list]) / len(list)
    std_dev[2] = variance[2]**0.5
    max[2] = sorted(list)[-1]
    min[2] = sorted(list)[0]
    total[2] = sum(list)

    #   Dictionary with the final values in the required format
    calculations = {
        'mean': [[m for m in mean]],
        'variance': [[v for v in variance]],
        'standard deviation': [[[stdv for stdv in std_dev]]],
        'max': [[mx for mx in max]],
        'min': [[mn for mn in min]],
        'sum': [[s for s in total]]
        }


    return calculations

    #   Example list that is on the website
print(calculate([0,1,2,3,4,5,6,7,8]))
