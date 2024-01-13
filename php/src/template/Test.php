<?php

require __DIR__ . '/../../src/$filename.php';

$test_cases = [
    [],
    [],
    [],
    [],
];

$functions = [
    'func' => 'func',
    'func_dp' => 'func_dp',
    'func_rec' => 'func_rec',
    'func_memo' => 'func_memo',
    'func_tail_rec' => 'func_tail_rec',
];

it('', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        try {
            expect($func($input))->toBe($expected);
        } catch (\Throwable) {
            // Not sure if pest provides a way to see which function failed exactly, that's why I'm wrapping this
            throw new Exception("Test failed for function '{$func}' with result '{$func($input)}' expected '{$expected}'");
        }
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);