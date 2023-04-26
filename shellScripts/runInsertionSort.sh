#!/bin/sh
# executes all the insertion sort iterations

python main.py 500 --algorithm insertion_sort --permutation reverse
python main.py 750 --algorithm insertion_sort --permutation reverse
python main.py 1000 --algorithm insertion_sort --permutation reverse
python main.py 2500 --algorithm insertion_sort --permutation reverse
python main.py 5000 --algorithm insertion_sort --permutation reverse
python main.py 7500 --algorithm insertion_sort --permutation reverse
python main.py 10000 --algorithm insertion_sort --permutation reverse
python main.py 15000 --algorithm insertion_sort --permutation reverse
python main.py 25000 --algorithm insertion_sort --permutation reverse
python main.py 50000 --algorithm insertion_sort --permutation reverse
python main.py 75000 --algorithm insertion_sort --permutation reverse
python main.py 100000 --algorithm insertion_sort --permutation reverse


python main.py 500 --algorithm insertion_sort --permutation almost-sorted
python main.py 750 --algorithm insertion_sort --permutation almost-sorted
python main.py 1000 --algorithm insertion_sort --permutation almost-sorted
python main.py 2500 --algorithm insertion_sort --permutation almost-sorted
python main.py 5000 --algorithm insertion_sort --permutation almost-sorted
python main.py 7500 --algorithm insertion_sort --permutation almost-sorted
python main.py 10000 --algorithm insertion_sort --permutation almost-sorted
python main.py 15000 --algorithm insertion_sort --permutation almost-sorted
python main.py 25000 --algorithm insertion_sort --permutation almost-sorted
python main.py 50000 --algorithm insertion_sort --permutation almost-sorted
python main.py 75000 --algorithm insertion_sort --permutation almost-sorted
#python main.py 100000 --algorithm insertion_sort --permutation almost-sorted

python main.py 75000 --algorithm insertion_sort --permutation random
#python main.py 100000 --algorithm insertion_sort --permutation random