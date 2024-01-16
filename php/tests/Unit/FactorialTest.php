<?php
require __DIR__ . '/../../src/Factorial.php';

$test_cases = [
    [5, 120],
    [0, 1],
    [1, 1],
    [3, 6],
];

$functions = [
    'factorial',
    'factorial_reduce',
    'factorial_rec',
    'factorial_tail_rec',
];

it('returns a factorial for given number', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);
