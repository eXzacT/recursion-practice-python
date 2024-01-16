<?php

require __DIR__ . '/../../src/BinarySearch.php';

$test_cases = [
    [[[2, 3, 4, 10, 40], 15], -1],
    [[[2, 3, 4, 10, 40], 40], 4],
    [[[2, 3, 4, 10, 40], 2], 0],
    [[[2, 3, 4, 10, 40], 10], 3],
    [[[], 15], -1],
];

$functions = [
    'binary_search',
    'binary_search_rec',
];

it('returns the index if a number was found in the array', function ($input, $expected) use ($functions) {
    [$arr, $needle] = $input;
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($arr, $needle);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);