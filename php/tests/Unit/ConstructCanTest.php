<?php

require __DIR__ . '/../../src/ConstructCan.php';

$test_cases = [
    [["enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]], true],
    [["eeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeeee"]], false]
];

$functions = [
    'construct_can_dp' => 'construct_can_dp',
    'construct_can_dp_v2' => 'construct_can_dp_v2',
    'construct_can_rec' => 'construct_can_rec',
    'construct_can_rec_v2' => 'construct_can_rec_v2',
    'construct_can_rec_v3' => 'construct_can_rec_v3',
    'construct_can_rec_memo' => 'construct_can_rec_memo',
];

it('returns whether a given string can be constructed from a given word bank', function ($input, $expected) use ($functions) {
    [$target, $word_bank] = $input;
    foreach ($functions as $func_name => $func) {
        $start_time = microtime(true);
        expect($func($target, $word_bank))->toBe($expected);
        $end_time = microtime(true);
        echo "Execution time of '{$func_name}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);
