import time
import argparse
import numpy
import matplotlib
import requirements
from enum import Enum


def generateList(size:int) -> list[int]:
    pass


class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'
    ALREADY_SORTED = 'sorted'
    ALMOST_SORTED = 'almost-sorted'


SORTING_ALGORITHMS = {
    'insertion_sort' : requirements.insertion_sort, 
    'shell_sort1' : requirements.shell_sort1, 
    'shell_sort2' : requirements.shell_sort2, 
    'shell_sort3' : requirements.shell_sort3, 
    'shell_sort4' : requirements.shell_sort4, 
    'merge_sort' : requirements.merge_sort, 
    'hybrid_sort1' : requirements.hybrid_sort1, 
    'hybrid_sort2' : requirements.hybrid_sort2, 
    'hybrid_sort3' : requirements.hybrid_sort3
}


parser = argparse.ArgumentParser(description= 'Benchmark Several Sorting Algorithms', 
                                 usage= 'main.py [size] --algorithm [sorting_algorithm] --permutation [permutation type]')

parser.add_argument('--algorithm', choices = SORTING_ALGORITHMS.keys(), dest = 'algorithm_name',
                    help = 'The sorting algorithm to use', required = True)

parser.add_argument('size', type = int, help = 'The size of the list we want to sort')

parser.add_argument('--permutation', default = 'random', choices = [e.value for e in PermutationType],
                    help = 'The default permutation to be used')

args = parser.parse_args()
args.permutation = PermutationType(args.permutation)
args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]


nums = [8, 4, 1, 6, 7]
args.algorithm(nums)
print(nums)