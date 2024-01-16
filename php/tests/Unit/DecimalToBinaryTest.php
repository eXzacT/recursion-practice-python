<?php

require __DIR__ . '/../../src/DecimalToBinary.php';

$test_cases = [
    [5, "101"],
    [7, "111"],
    [0, "0"],
];

$functions = [
    'decimal_to_binary',
    'decimal_to_binary_rec',
    'decimal_to_binary_tail_rec',
];

it('returns a binary representation of a given number', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);