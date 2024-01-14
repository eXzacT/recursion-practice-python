<?php

require __DIR__ . '/../../src/Fibonacci.php';

$test_cases = [
    [0, 0],
    [1, 1],
    [10, 55],
    [30, 832040],
];

$functions = [
    'fib' => 'fib',
    'fib_dp' => 'fib_dp',
    'fib_rec' => 'fib_rec',
    'fib_memo' => 'fib_memo',
    'fib_tail_rec' => 'fib_tail_rec',
];

it('returns a fibonacci number for a given n', function ($input, $expected) use ($functions) {
    foreach ($functions as $func_name => $func) {
        $start_time = microtime(true);
        expect($func($input))->toBe($expected);
        $end_time = microtime(true);
        echo "Execution time of '{$func_name}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
})->with($test_cases);