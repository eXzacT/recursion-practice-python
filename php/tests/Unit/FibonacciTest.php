<?php

require __DIR__ . '/../../src/fibonacci.php';

$test_cases = [
    [0, 0],
    [1, 1],
    [10, 55],
];

it('returns a fibonacci number for a given n', function ($n, $expected) {
    expect(fib($n))->toBe($expected);
    expect(fib_dp($n))->toBe($expected);
    expect(fib_rec($n))->toBe($expected);
    expect(fib_rec_v2($n))->toBe($expected);
})->with($test_cases);