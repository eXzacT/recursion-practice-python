<?php

require __DIR__ . '/../../src/decimal_to_binary.php';

$test_cases = [
    [5, "101"],
    [7, "111"],
    [0, "0"],
];

it('returns a binary representation of a given number', function ($number, $expected) {
    expect(decimal_to_binary($number))->toBe($expected);
    expect(decimal_to_binary_rec($number))->toBe($expected);
    expect(decimal_to_binary_tail_rec($number))->toBe($expected);
})->with($test_cases);