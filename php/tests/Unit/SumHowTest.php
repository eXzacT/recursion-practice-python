<?php

require __DIR__ . '/../../src/SumHow.php';

$test_cases = [
    [[0, [7, 14, 28]], []],
    [[9, [5, 5]], null],
    [[10, [5, 5]], [5, 5]],
    [[300, [21, 5, 9, 12, 30]], [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 5, 5, 5, 12]],
    [[33, [1, 4]], array_fill(0, 33, 1)]
];

$functions = [
    'sum_how_rec',
    'sum_how_memo',
    'sum_how_rec_v2',
    'sum_how_memo_v2',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks how to sum up to given number using numbers from the array', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($total, $arr);
        expect($actual)->toBe($expected, "Failed test for function {$func}:");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);

$test_cases = [
    [[0, [7, 14, 28]], []],
    [[9, [5, 5]], null],
    [[10, [5, 5]], [5, 5]],
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks how to sum up to given number using numbers from the array using dp', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    $start_time = microtime(true);
    $actual = sum_how_dp($total, $arr);
    expect($actual)->toBe($expected, "Failed test for function 'sum_how_dp':");
    $end_time = microtime(true);
    echo "Execution time of 'sum_how_dp': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
})->with($test_cases);