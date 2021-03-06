#!/usr/bin/env python3
"""
Won't use timeit module as there isn't an easy or elegant way to pass code or
extract result

You have to pass a string of code and it uses this:
    code = compile(src, dummy_src_name, "exec")
    eval(code, globals(), ns)
I have no idea why it doesn't support passing in any callable.

Actually it does! it isn't well documented...

    >>> from timeit import Timer
    >>> time_list_creation = Timer(stmt=lambda: list(range(10**6)))
    >>> time_list_creation.timeit(10)
    0.44386727098026313
    In [70]: Timer(stmt=lambda: list(range(10**6))).timeit(10)
    Out[70]: 0.41654246201505885
    In [71]: Timer(stmt=lambda: list(range(10**6))).timeit(100)
    Out[71]: 3.9120825139980298
    In [72]: Timer(stmt=lambda: list(range(10**6))).timeit(1000)
    Out[72]: 39.69789917700109

    >>> res = Timer(stmt=lambda: list(range(10**6))).repeat(10, 1)
    # 10 is number of results, 1 is number of times to execute statment
    # here res has list of all results


At some point I went from:
In [13]: %run main.py
2.8395652770996092e-05
5.6242942810058595e-05
To:
In [16]: %run main.py
0.04266829490661621
0.0888298511505127

tested:
    - is it by passing args?
But couldn't recreate

process_time returns value in factional seconds of the sum of system and user
CPU time of current process. Does not include time elapsed during sleep.
Only difference between consecutive calls is valid

fractional second is part of the time that is not an integer.
Given 123.9 time, the fractional second is 0.9

Note that teimit module uses perf_counter as its default
"""
import time
import statistics
import json

import matplotlib.pyplot as plt
import numpy as np

default_timer = time.perf_counter  # process_time


def timeit(callable_, runs=10):

    def inner(*args, **kwargs):

        def timeit():
            start = default_timer()
            callable_(*args, **kwargs)
            end = default_timer()
            return end - start

        times = [timeit() for _ in range(runs)]

        avg = statistics.mean(times)
        best = min(times)
        worst = min(times)

        return best, avg, worst

    return inner


@timeit
def create(container, count):
    return container(range(count))


@timeit
def contains(container, target):
    return target in container


def print_stats_report(best, avg, worst):
    tmpl = "best:  {}\nmean:  {}\nworst: {}\n"
    msg = tmpl.format(best, avg, worst)
    print(msg)


def print_container_type(container):
    if not type(container) == type:
        container = type(container)
    print(str(container).split("'")[1].capitalize())


def study(containers, timeit_function, parameter):
    for container in containers:
        print_container_type(container)
        print_stats_report(*timeit_function(container, parameter))


# print('Creation')
# containers = (list, set, tuple)
# size = int(1e6)
# study(containers, create, size)
#
# print('Membership')
# containers = (list(range(size)), set(range(size)), tuple(range(size)))
# target = 5000
# study(containers, contains, size)

def cache(callable_):
    def inner(*args, **kwargs):
        cache_filename = kwargs.pop('cache_filename')
        try:
            with open(cache_filename, 'r') as fp:
                results = json.loads(fp.read())

        except FileNotFoundError:

            results = callable_(*args, **kwargs)

            # TODO print some feedback
            with open(cache_filename, 'w') as fp:
                result_str = json.dumps(results)
                fp.write(result_str)

        return results
    return inner


@cache
def get_results_creation(container, start=0, end=int(1e6), step=int(1e4)):

    for i in range(start, end, step):
        create(container, i)


def get_results_contains(container, cache_filename,
                         start=0, end=int(1e6), step=int(1e4)):
    # file based caching
    try:
        with open(cache_filename, 'r') as fp:
            results = json.loads(fp.read())

    except FileNotFoundError:

        target = -1 # we want test to always fail. that way we ensure all
        # values are examined
        results = []
        for i in range(start, end, step):
            values = container(range(i))
            results.append(contains(values, target))


        # TODO print some feedback
        with open(cache_filename, 'w') as fp:
            result_str = json.dumps(results)
            fp.write(result_str)

    return results


def save_graph(results, file_name):
    x = np.arange(0, len(results), 1)
    y = list(map(lambda x: x[1], results))

    fig = plt.figure()
    fig.add_subplot(111)
    plt.plot(x, y)
    plt.savefig(file_name)


from functools import partial

list_create = partial(create, list)
results = get_results_creation(list_create, cache_filename='list_creation.txt')
save_graph(results, 'list_creation.png')

set_create = partial(create, set)
results = get_results_creation(set_create , 'set_creation.txt')
save_graph(results, 'set_creation.png')

set_create = partial(create, tuple)
results = get_results_creation(set_create , 'set_creation.txt')
save_graph(results, 'set_creation.png')

results = get_results_contains(list, 'list_membership.txt')
save_graph(results, 'list_membership.png')

results = get_results_contains(set, 'set_membership.txt')
save_graph(results, 'set_membership.png')

"""
Sample output:
In [12]: %run main.py
Creation

List
best:  0.029847362980945036
mean:  0.04134655749658123
worst: 0.029847362980945036

Set
best:  0.08696803500060923
mean:  0.09387849149934482
worst: 0.08696803500060923

Tuple
best:  0.031665550981415436
mean:  0.04328682199702598
worst: 0.031665550981415436

Membership

List
best:  8.290499681606889e-05
mean:  9.880229481495917e-05
worst: 8.290499681606889e-05

Set
best:  3.479945007711649e-07
mean:  4.6909553930163383e-07
worst: 3.479945007711649e-07

Tuple
best:  8.224099292419851e-05
mean:  0.00010319769789930433
worst: 8.224099292419851e-05
"""
