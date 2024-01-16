<?php

require __DIR__ . '/../../src/ArrayMean.php';

$test_cases = [
    [[5, 9, 10, 25, 1], 10],
    [[0], 0],
    [[192, 123, 77, 8, 0], 80],
];

$functions = [
    'array_mean',
    'array_mean_iter',
    'array_mean_rec',
    'array_mean_tail_rec'
];

it('calculates the mean of an array', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);