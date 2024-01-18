<?php

require __DIR__ . '/../../src/CopyString.php';


$test_cases = [
    ["originalstring", "originalstring"],
    ["", ""],
];

$functions = [
    'copy_string',
    'copy_string_rec',
    'copy_string_tail_rec',
];

it('copies the string', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);