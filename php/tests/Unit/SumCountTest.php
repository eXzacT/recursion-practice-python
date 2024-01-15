<?php

require __DIR__ . '/../../src/SumCount.php';

$test_cases = [
    [[200, [7, 14, 28]], 0],
    [[0, [7, 14, 28]], 1],
    [[56, [7, 2, 28]], 9],
    [[9, [5, 5]], 0],
];

$functions = [
    'sum_count_dp',
    'sum_count_rec',
    'sum_count_memo',
    'sum_count_rec_v2',
    'sum_count_memo_v2',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks in how many different ways to sum up to a given number with numbers from the array', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($total, $arr);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }

    echo "\n";
})->with($test_cases);