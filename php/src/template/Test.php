<?php

require __DIR__ . '/../../src/$filename.php';

$test_cases = [
    [],
    [],
    [],
    [],
];

$functions = [
    'func_dp',
    'func_rec',
    'func_memo',
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