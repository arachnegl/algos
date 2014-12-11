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

default_timer = time.perf_counter  # process_time

def timeit(callable_, runs=10):
    def inner(*args, **kwargs):
        times = []
        for i in range(runs):
            start = default_timer()
            result = callable_(*args, **kwargs)
            end = default_timer()
            took = end - start
            times.append(took)
        avg = statistics.mean(times)
        best = min(times)
        worst = min(times)
        return result, best, avg, worst
    return inner


@timeit
def create(container, count):
    return container(range(count))


@timeit
def contains(container, obj):
    return obj in container


size = int(1e6)

print('Creation\n')
containers = (list, set, tuple)
for container in containers:
    result, best, avg, worst = create(container, size)
    container_name = str(container).split("'")[1].capitalize()
    tmpl = "{}:\nbest:  {}\nmean:  {}\nworst: {}\n"
    msg = tmpl.format(container_name, best, avg, worst)
    print(msg)

"""
Outputs:

Creation

List:
best:  0.029161999999999466
mean:  0.042134799999998765
worst: 0.029161999999999466

Set:
best:  0.08680100000000124
mean:  0.09330260000000265
worst: 0.08680100000000124

Tuple:
best:  0.03296100000000024
mean:  0.0433002000000009
worst: 0.03296100000000024sults

Which compares with:

In [61]: %timeit list(range(int(1e6)))
10 loops, best of 3: 41.9 ms per loop

In [62]: %timeit set(range(int(1e6)))
10 loops, best of 3: 92.6 ms per loop

In [63]: %timeit tuple(range(int(1e6)))
10 loops, best of 3: 43.2 ms per loop
"""

print('Membership\n')
containers = (list(range(size)), {x for x in range(size)}, tuple(range(size)))
target = 5000
for container in containers:
    result, best, avg, worst = contains(container, target)
    container_name = str(type(container)).split("'")[1].capitalize()
    tmpl = "{}:\nbest:  {}\nmean:  {}\nworst: {}\n"
    msg = tmpl.format(container_name, best, avg, worst)
    print(msg)
