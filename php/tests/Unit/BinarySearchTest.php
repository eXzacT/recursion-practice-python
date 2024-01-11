<?php

require __DIR__ . '/../../src/binary_search.php';

$test_cases = [
    [[[2, 3, 4, 10, 40], 15], -1],
    [[[2, 3, 4, 10, 40], 40], 4],
    [[[2, 3, 4, 10, 40], 2], 0],
    [[[2, 3, 4, 10, 40], 10], 3],
    [[[], 15], -1],
];

it('returns the index if a number was found in the array', function ($input, $expected) {
    [$arr, $needle] = $input;
    expect(binary_search($arr, $needle))->toBe($expected);
    expect(binary_search_rec($arr, $needle))->toBe($expected);
})->with($test_cases);