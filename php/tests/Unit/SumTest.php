<?php

require __DIR__ . '/../../src/sum.php';

$test_cases = [
    [5, 15],
    [10, 55],
    [0, 0],
];

it('returns a sum of numbers in a given range n', function ($n, $expected) {
    expect(sum($n))->toBe($expected);
    expect(sum_reduce($n))->toBe($expected);
    expect(sum_gauss($n))->toBe($expected);
    expect(sum_rec($n))->toBe($expected);
    expect(sum_tail_rec($n))->toBe($expected);
})->with($test_cases);