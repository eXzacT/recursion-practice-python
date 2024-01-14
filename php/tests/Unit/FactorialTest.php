<?php
require __DIR__ . '/../../src/Factorial.php';

$test_cases = [
    [5, 120],
    [0, 1],
    [1, 1],
    [3, 6],
];

it('returns a factorial for given number', function ($n, $expected) {
    expect(factorial($n))->toBe($expected);
    expect(factorial_reduce($n))->toBe($expected);
    expect(factorial_rec($n))->toBe($expected);
    expect(factorial_tail_rec($n))->toBe($expected);
})->with($test_cases);
