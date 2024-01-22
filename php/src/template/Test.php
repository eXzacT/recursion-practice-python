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