import time
import argparse
import requirements
import random
import math
import csv
from enum import Enum
from collections.abc import Callable
from pathlib import Path



class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'random'
    REVERSE_SORTED = 'reverse'
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

DATA_DIRECTORY = Path('data')


parser = argparse.ArgumentParser(description= 'Benchmark Several Sorting Algorithms', 
                                 usage= 'main.py [size] --algorithm [sorting_algorithm] --permutation [permutation type]')

parser.add_argument('--algorithm', choices = SORTING_ALGORITHMS.keys(), dest = 'algorithm_name',
                    help = 'The sorting algorithm to use', required = True)

parser.add_argument('size', type = int, help = 'The size of the list we want to sort')

parser.add_argument('--permutation', default = 'random', choices = [e.value for e in PermutationType],
                    help = 'The default permutation to be used')


def FisherYatesShuffle(nums:list[int]) -> None:
    shortened_range =  math.floor(math.log2(len(nums)))

    while shortened_range >= 1:
        random_num = random.choice(nums)
        random_index = nums.index(random_num)
        nums[shortened_range], nums[random_index] = nums[random_index], nums[shortened_range]
        shortened_range -= 1


def getDataPath(permutation:PermutationType, algorithm_name:str) -> Path:
    directory = DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents = True, exist_ok = True)

    return (directory / permutation.value).with_suffix('.csv')


def saveData(algorithm_name:str, permutation:PermutationType, size:int, elapsed_time:int):
    path = getDataPath(permutation, algorithm_name)

    with path.open('a', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([size, elapsed_time])


def generateList(size:int, permutation:PermutationType) -> list[int]:
    nums = list(range(size))

    match permutation:
        case PermutationType.UNIFORMLY_DISTRIBUTED:
            random.shuffle(nums)
        case PermutationType.REVERSE_SORTED:
            nums.sort(reverse = True)
        case PermutationType.ALMOST_SORTED:
            FisherYatesShuffle(nums)

    return nums


def benchmark(algorithm:Callable[[list[int]], None], size:int, permutation:PermutationType) -> None:
    nums = generateList(size, permutation)
    
    # timing the algorithm
    start_time = time.process_time_ns()
    algorithm(nums)
    end_time = time.process_time_ns()

    elapsed_time = end_time - start_time

    saveData(args.algorithm_name, permutation, size, elapsed_time)

    print(elapsed_time)


if __name__ == '__main__':
    args = parser.parse_args()
    args.permutation = PermutationType(args.permutation)
    args.algorithm = SORTING_ALGORITHMS[args.algorithm_name]

    benchmark(args.algorithm, args.size, args.permutation)