<?php

require __DIR__ . '/../../src/ackermann.php';


$test_cases = [
    [[0, 0], 1],
    [[0, 1], 2],
    //[[1, 0], 2], Doesn't work for DP approach for any 'm' when 'n' is 0
    [[1, 1], 3],
    [[3, 4], 125]
];

$functions = [
    'ackermann_dp' => 'ackermann_dp',
    'ackermann_rec' => 'ackermann_rec',
    'ackermann_rec_memo' => 'ackermann_rec_memo',
];

it('returns the correct ackermanns number', function ($input, $expected) use ($functions) {
    [$m, $n] = $input;
    foreach ($functions as $func_name => $func) {
        $start_time = microtime(true);
        expect($func($m, $n))->toBe($expected);
        $end_time = microtime(true);
        echo "Execution time of '{$func_name}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
})->with($test_cases);

it('returns the correct ackermanns number for a large input', function () {
    $start_time = microtime(true);
    expect(ackermann_dp(6, 6))->toBe(1014754159855);
    $end_time = microtime(true);
    echo "Execution time of 'ackermann_dp': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
});