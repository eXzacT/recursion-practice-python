<?php

require __DIR__ . '/../../src/SumCan.php';

$test_cases = [
    [[200, [7, 14, 28]], false],
    [[0, [7, 14, 28]], true],
    [[56, [7, 2, 28]], true],
    [[9, [5, 5]], false],
];

$functions = [
    'sum_can_dp',
    'sum_can_dp_v2',
    'sum_can_rec',
    'sum_can_memo',
    'sum_can_rec_v2',
    'sum_can_memo_v2',
];

it('checks if it\'s possible to sum up to given number with numbers from the array', function ($input, $expected) use ($functions) {
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