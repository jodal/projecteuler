/*
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

From https://projecteuler.net/problem=30
*/

use std;
import vec::{foldl, map};

fn main() {
    std::io::println(#fmt("%d", problem30(5u)));
}

#[test]
fn test_problem30() {
    assert problem30(4u) == 19316;
}

fn problem30(power: uint) -> int {
    let sum: int = 0;
    int::range(1, upper_limit(power)) { |i|
        if sum_of_powers_of_digits_equal_number(i, power) {
            sum += i;
        }
    }
    sum
}

#[test]
fn test_upper_limit() {
    assert upper_limit(3u) >= 407;
    assert upper_limit(4u) >= 9474;
    assert upper_limit(5u) >= 194979;
}

fn upper_limit(power: uint) -> int {
    // FIXME This formula is just crap taken out of thin air
    int::pow(9, power) * (power as int)
}

#[test]
fn test_sum_of_powers_of_digits_equal_number() {
    assert !sum_of_powers_of_digits_equal_number(1, 4u);
    assert sum_of_powers_of_digits_equal_number(1634, 4u);
    assert !sum_of_powers_of_digits_equal_number(1635, 4u);
    assert sum_of_powers_of_digits_equal_number(8208, 4u);
    assert sum_of_powers_of_digits_equal_number(9474, 4u);
}

fn sum_of_powers_of_digits_equal_number(n: int, power: uint) -> bool {
    let ps = power_of_digits(n, power);
    if vec::len(ps) == 1u { ret false }
    sum(ps) == n
}

#[test]
fn test_power_of_digits() {
    assert power_of_digits(1634, 4u) == [1, 1296, 81, 256];
}

fn power_of_digits(n: int, power: uint) -> [int] {
    map(map(str::to_chars(int::to_str(n, 10u)), int_from_char),
        {|d| int::pow(d as int, power)})
}

#[test]
fn test_int_from_char() {
    assert int_from_char('0') == 0;
    assert int_from_char('1') == 1;
    assert int_from_char('2') == 2;
}

fn int_from_char(&&c: char) -> int {
    char::to_digit(c) as int
}

#[test]
fn test_sum() {
    assert sum([]) == 0;
    assert sum([1]) == 1;
    assert sum([2]) == 2;
    assert sum([1, 2, 3]) == 6;
    assert sum([1, 2, -3]) == 0;
}

fn sum(xs: [int]) -> int {
    foldl(0, xs, {|z, x| z + x})
}
