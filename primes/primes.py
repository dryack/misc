# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 14:21:12 2014

@author: dave
"""

#additional prime numbers for testing/play available at
#http://prime-numbers.org/

from timeit import default_timer

# following taken from
# http://python.dzone.com/articles/python-timer-class-context


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = default_timer

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %.4f ms' % self.elapsed


class PrimePlay():
    def __init__(self, num):
        self.number = num

    def isPrime1(self):
        with Timer(verbose=True) as t:
            i = 2
            while i < self.number:
                if self.number % i == 0:
                    return False
                i += 1
            # manually exiting Timer instance in order to obtain t.elapsed;
            # this isn't required, and isn't quite as accurate, but it's
            # an example of how to get around the problem of Timer
            # not exiting until AFTER the return statement.
            t.__exit__()
            print 'took %.4f ' % (t.elapsed)
            return True

    def isPrime2(self):
        with Timer(verbose=True) as t:
            i = 3
            if self.number == 2:
                return True
            if self.number % 2 == 0:
                return False
            while i * i <= self.number:
                if self.number % i == 0:
                    return False
                i += 2
            return True


def main():
    a = PrimePlay(5)
    b = PrimePlay(9)
    c = PrimePlay(7251)
    d = PrimePlay(127363)
    e = PrimePlay(9869403307)
    print a.isPrime1()
    print a.isPrime2()
    print b.isPrime1()
    print b.isPrime2()
    print c.isPrime1()
    print c.isPrime2()
    print d.isPrime1()
    print d.isPrime2()
    #print e.isPrime1()  # elapsed time: 3915196.042577 ms
    #print e.isPrime2()  # elapsed time: 21.939831 ms

if __name__ == '__main__':
    main()
