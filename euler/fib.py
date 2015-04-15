import cProfile, pstats, io

_cache = {1: 1, 2: 2, }
def fib_c(n):
    ''' cached '''
    if n in _cache:
        return _cache[n]
    else:
        prev1 = fib_c(n - 1)
        _cache[n - 1] = prev1
        prev2 = fib_c(n - 2)
        _cache[n - 2] = prev2
        _cache[n] = prev1 + prev2
        return _cache[n]

def fib_n(n):
    ''' naive '''
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_n(n - 1) + fib_n(n - 2)

def fib_acc(n):
    n1 = 1
    n2 = 2
    if n == 1:
        return n1
    elif n == 2:
        return n2
    total = 2
    count = 2
    #print('n - 2 = {} n - 1 = {}'.format(n1, n2))
    while count <= n - 1:
        new = n1 + n2
        if new % 2 == 0:
            total = total + new
        n1 = n2
        n2 = new
        count += 1
        #print('n - 2 = {} n - 1 = {}'.format(n1, n2))
    return n2, total

def main():

    for fib_func in [fib_c, fib_acc, fib_n]:
        pr = cProfile.Profile()
        pr.enable()

        result = fib_func(20)
        print(u'Got: {}'.format(result))

        pr.disable()
        s = io.StringIO()
        sortby = u'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

if __name__ == '__main__':
    main()
