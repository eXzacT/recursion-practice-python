<?php

require __DIR__ . '/../../src/DigitsSum.php';

$test_cases = [
    [23959, 28],
    [0, 0],
    [10, 1],
];

$functions = [
    'digits_sum_string',
    'digits_sum_modulo',
    'digits_sum_reduce',
    'digits_sum_rec',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('sums digits of a number', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);