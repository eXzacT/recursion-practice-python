<?php

require __DIR__ . '/../../src/TriangleSum.php';

$test_cases = [
    [[1, 2, 3, 4, 5], [[1, 2, 3, 4, 5], [3, 5, 7, 9], [8, 12, 16], [20, 28], [48]]],
    [[0, 1], [[0, 1], [1]]],
    [[0, 5, 9], [[0, 5, 9], [5, 14], [19]]],
];

$functions = [
    'triangle_sum',
    'triangle_sum_rec',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('creates a triangle of sums', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);