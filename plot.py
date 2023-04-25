import matplotlib.pyplot as plt
import numpy
import csv
from collections import defaultdict
from main import PermutationType
from pathlib import Path

DATA_DIRECTORY = Path('data')

def getDataPath(permutation:PermutationType, algorithm_name:str) -> Path:
    directory =  DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return (directory / permutation.value).with_suffix('.csv')


def loadData(permutation:PermutationType, algorithm_name:str) -> dict[int, list[int]]:
    path = getDataPath(permutation, algorithm_name)

    data = defaultdict(list)
    with path.open() as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data[int(row[0])].append(int(row[1]))

    return data

print(loadData(PermutationType.UNIFORMLY_DISTRIBUTED, 'merge_sort'))