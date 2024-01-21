<?php

require __DIR__ . '/../../src/HanoiThree.php';

$test_cases = [
    [
        3,
        [
            "Moving disk 1 from rod 1 to rod 3",
            "Moving disk 2 from rod 1 to rod 2",
            "Moving disk 1 from rod 3 to rod 2",
            "Moving disk 3 from rod 1 to rod 3",
            "Moving disk 1 from rod 2 to rod 1",
            "Moving disk 2 from rod 2 to rod 3",
            "Moving disk 1 from rod 1 to rod 3",
        ]
    ],
    [
        4,
        [
            "Moving disk 1 from rod 1 to rod 2",
            "Moving disk 2 from rod 1 to rod 3",
            "Moving disk 1 from rod 2 to rod 3",
            "Moving disk 3 from rod 1 to rod 2",
            "Moving disk 1 from rod 3 to rod 1",
            "Moving disk 2 from rod 3 to rod 2",
            "Moving disk 1 from rod 1 to rod 2",
            "Moving disk 4 from rod 1 to rod 3",
            "Moving disk 1 from rod 2 to rod 3",
            "Moving disk 2 from rod 2 to rod 1",
            "Moving disk 1 from rod 3 to rod 1",
            "Moving disk 3 from rod 2 to rod 3",
            "Moving disk 1 from rod 1 to rod 2",
            "Moving disk 2 from rod 1 to rod 3",
            "Moving disk 1 from rod 2 to rod 3",
        ]
    ]
];

$functions = [
    'hanoi_rec',
    'hanoi_rec_v2',
];

// First function call is slower for some reason, so whatever is called first will be slowest
it('gives instructions how to solve hanoi tower for given number of disks', function ($input, $expected) use ($functions) {
    foreach ($functions as $func) {
        $start_time = microtime(true);
        $actual = $func($input);
        expect($actual)->toBe($expected, "Failed test for function {$func}");
        $end_time = microtime(true);
        echo "Execution time of '{$func}': " . round(($end_time - $start_time) * 1000, 4) . " ms\n";
    }
    echo "\n";
})->with($test_cases);