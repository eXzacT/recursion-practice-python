<?php

require __DIR__ . '/../../src/Sum.php';

$test_cases = [
    [5, 15],
    [10, 55],
    [0, 0],
];

$functions = [
    'sum',
    'sum_reduce',
    'sum_gauss',
    'sum_rec',
    'sum_tail_rec',
];

it('returns sum for numbers up to and including n', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);