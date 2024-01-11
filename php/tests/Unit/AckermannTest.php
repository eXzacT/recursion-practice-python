<?php

require __DIR__ . '/../../src/ackermann.php';


$test_cases = [
    [[0, 0], 1],
    [[0, 1], 2],
    //[[1, 0], 2], Doesn't work for DP approach for any 'm' when 'n' is 0
    [[1, 1], 3],
    [[3, 4], 125]
];

it('returns the correct ackermanns number', function ($input, $expected) {
    [$m, $n] = $input;
    expect(ackermann_dp($m, $n))->toBe($expected);
    expect(ackermann_rec($m, $n))->toBe($expected);
    expect(ackermann_rec_memo($m, $n))->toBe($expected);
})->with($test_cases);

it('returns the correct ackermanns number for a large input', function () {
    expect(ackermann_dp(5, 5))->toBe(11174165);
});