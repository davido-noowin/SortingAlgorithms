import matplotlib.pyplot as plt
import numpy
import csv
from collections import defaultdict
from main import PermutationType
from pathlib import Path


DATA_DIRECTORY = Path('CS161\\SortingAlgorithms\\data')

def getDataPath(permutation:PermutationType, algorithm_name:str) -> Path:
    directory =  DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return (directory / permutation.value).with_suffix('.csv')


def loadData(permutation:PermutationType, algorithm_name:str) -> dict[int, list[int]]:
    path = getDataPath(permutation, algorithm_name)
    print(path)

    data = defaultdict(list)
    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[int(row[0])].append(int(row[1]))

    return data


def loadAverageData(permutation:PermutationType, algorithm_name:str) -> tuple[list[int], list[int]]:
    data = loadData(permutation, algorithm_name)
    sizes = []
    average_times = []

    for size, elapsed_times in sorted(data.items()):
        sizes.append(size)
        average_times.append(sum(elapsed_times) / len(elapsed_times))

    return sizes, average_times


def addToPlot(permutation:PermutationType, algorithm_name:str, color:str):
    sizes, average_times = loadAverageData(permutation, algorithm_name)

    x,y = sizes[3:], average_times[3:]
    logx, logy = numpy.log(x), numpy.log(y)

    # making a best fit line
    m, b = numpy.polyfit(logx, logy, 1)
    fit = numpy.poly1d((m, b))

    plt.loglog(sizes, average_times, '.', base = 2, color = color)

    expected_y = fit(logx)

    
    # plotting the line of best fit
    equation = f'{algorithm_name} ({permutation.value}): log C(n) ~ {numpy.round(m, 5)} log n + {numpy.round(b, 5)})'
    plt.loglog(x, numpy.exp(expected_y), base = 2, color = color, label = equation)

    #plt.text(2**9, y[-1], equation).set_color(color)
    plt.xlabel('Input Size (n, # of elements)')
    plt.ylabel('Elapsed Time (in nanoseconds)')
    plt.title(f'{algorithm_name} Plot')
    
    return equation



if __name__ == '__main__':
    e1 = addToPlot(PermutationType.UNIFORMLY_DISTRIBUTED, 'merge_sort', 'red')
    e2 = addToPlot(PermutationType.ALMOST_SORTED, 'merge_sort', 'green')
    e3 = addToPlot(PermutationType.REVERSE_SORTED, 'merge_sort', 'blue')
    plt.legend([None, e1, None, e2, None, e3], loc = 'upper left')

    plt.show()