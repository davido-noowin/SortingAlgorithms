import matplotlib.pyplot as plt
import numpy
import csv
from collections import defaultdict
from main import PermutationType
from pathlib import Path


def getDataPath(permutation:PermutationType, algorithm_name:str) -> Path:
    directory = Path('.') / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return (directory / permutation.value).with_suffix('.csv')


def loadData(permutation:PermutationType, algorithm_name:str):
    path = getDataPath(permutation, algorithm_name)