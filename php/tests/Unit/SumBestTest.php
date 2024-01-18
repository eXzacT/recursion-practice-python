<?php

require __DIR__ . '/../../src/SumBest.php';

$test_cases = [
    [[35, [1, 2, 3]], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]],
    //[[100, [60, 40, 30, 20, 1, 2, 3, 4, 5]], [40, 60]], wrong order for dp [60,40] doesn't really matter
    [[30, [5, 7, 10, 20]], [20, 10]],
    //[[0, [1, 2, 3]], []],
    [[51, []], null],
];

$functions = [
    'sum_best_dp',
    //'sum_best_rec', Slow
    'sum_best_memo',
    'sum_best_rec_v2',
    'sum_best_rec_v2_early',
    'sum_best_memo_v2',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks what\'s the best way to sum up to given number using numbers from the array', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($total, $arr);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);