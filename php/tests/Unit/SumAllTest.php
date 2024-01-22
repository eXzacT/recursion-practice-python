<?php

require __DIR__ . '/../../src/SumAll.php';

$test_cases = [
    [[0, [2, 4, 3]], [[]]],
    [[5, [1, 2, 3]], [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [2, 3]]],
    [[9, [10, 12, 13]], null],
    [[15, [10, 9, 3, 2, 1]], [[10, 3, 2], [10, 3, 1, 1], [10, 2, 2, 1], [10, 2, 1, 1, 1], [10, 1, 1, 1, 1, 1], [9, 3, 3], [9, 3, 2, 1], [9, 3, 1, 1, 1], [9, 2, 2, 2], [9, 2, 2, 1, 1], [9, 2, 1, 1, 1, 1], [9, 1, 1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [3, 3, 3, 3, 2, 1], [3, 3, 3, 3, 1, 1, 1], [3, 3, 3, 2, 2, 2], [3, 3, 3, 2, 2, 1, 1], [3, 3, 3, 2, 1, 1, 1, 1], [3, 3, 3, 1, 1, 1, 1, 1, 1], [3, 3, 2, 2, 2, 2, 1], [3, 3, 2, 2, 2, 1, 1, 1], [3, 3, 2, 2, 1, 1, 1, 1, 1], [3, 3, 2, 1, 1, 1, 1, 1, 1, 1], [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 2, 2, 2, 2, 2, 2], [3, 2, 2, 2, 2, 2, 1, 1], [3, 2, 2, 2, 2, 1, 1, 1, 1], [3, 2, 2, 2, 1, 1, 1, 1, 1, 1], [3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 1], [2, 2, 2, 2, 2, 2, 1, 1, 1], [2, 2, 2, 2, 2, 1, 1, 1, 1, 1], [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]],
];

$functions = [
    // Works but different order, I could make all of them do lexicographic order but there's no point
    //'sum_all_dp', 
    'sum_all_rec',
    'sum_all_memo',
    'sum_all_rec_v2',
    'sum_all_memo_v2',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks all the ways to sum up to a given number using numbers from a given array', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    echo "Input " . json_encode($input), "\n";
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($total, $arr);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);