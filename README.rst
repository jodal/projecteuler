My Project Euler solutions
==========================

This is my solutions for some of the
`Project Euler <http://projecteuler.net/>`_ problems. My focus here is first
playing with programming languages, and second playing with algorithms.

All solutions include the problem description and test cases.

The Python solutions include silent asserts that will blow up if anything is
wrong, and prints the final solution::

    $ python problem001.py
    233168

The Rust solutions can be compiled either for running tests or for solving the
problem::

    $ rustc --test problem030.rs && ./problem030

    running 6 tests
    test test_int_from_char ... ok
    test test_power_of_digits ... ok
    test test_problem30 ... ok
    test test_sum ... ok
    test test_sum_of_powers_of_digits_equal_number ... ok
    test test_upper_limit ... ok

    result: ok. 6 passed; 0 failed; 0 ignored

    $ rustc problem030.rs && ./problem030
    443839
