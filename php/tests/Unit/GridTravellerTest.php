<?php

require __DIR__ . '/../../src/GridTraveller.php';

$test_cases = [
    [[3, 3], 6],
    [[4, 4], 20],
    [[6, 6], 252],
    [[10, 10], 48620],
];

$functions = [
    'grid_traveller_dp',
    'grid_traveller_dp_v2',
    'grid_traveller_rec',
    'grid_traveller_memo',
    'grid_traveller_rec_v2',
    'grid_traveller_memo_v2',
    'grid_traveller_rec_v3',
    'grid_traveller_memo_v3',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('calculates how many ways you can travel from top right to bottom left in a 2d grid', function ($input, $expected) use ($functions) {
    [$m, $n] = $input;
    echo "For input " . json_encode($input), "\n";
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($m, $n);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);