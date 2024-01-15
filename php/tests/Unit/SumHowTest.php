<?php

require __DIR__ . '/../../src/SumHow.php';

$test_cases = [
    [[200, [7, 14, 28]], false],
    [[0, [7, 14, 28]], [0]],
    [[56, [7, 2, 28]], [7, 7, 7, 7, 7, 7, 7, 7]],
    [[9, [5, 5]], false],
];

$functions = [
    'sum_how_dp',
    'sum_how_rec',
    'sum_how_memo',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('checks if it\'s possible to sum up to given number with numbers from the array', function ($input, $expected) use ($functions) {
    [$total, $arr] = $input;
    foreach ($functions as $func) {
        $start_time = microtime(true);
        try {
            expect($func($total, $arr))->toBe($expected);
        } catch (\Throwable) {
            // Not sure if pest provides a way to see which function failed exactly, that's why I'm wrapping this
            throw new Exception("Test failed for function '{$func}' with result '{$func($input)}' expected '{$expected}'");
        }
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);