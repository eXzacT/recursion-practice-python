<?php

require __DIR__ . '/../../src/FindFirstUppercase.php';

$test_cases = [
    ["testcaseE", 8],
    ["nouppercase", -1],
    ["", -1]
];

$functions = [
    'find_first_uppercase',
    'find_first_uppercase_ascii',
    'find_first_uppercase_rec',
];


it('finds first uppercase letter', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}: expected {$expected}, but got {$actual}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);