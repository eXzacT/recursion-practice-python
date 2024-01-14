<?php

require __DIR__ . '/../../src/FindFirstUppercase.php';

$test_cases = [
    ["testcaseE", 8],
    ["nouppercase", -1],
    ["", -1]
];


it('finds first uppercase letter', function ($input, $expected) {
    expect(find_first_uppercase($input))->toBe($expected);
    expect(find_first_uppercase_ascii($input))->toBe($expected);
    expect(find_first_uppercase_rec($input))->toBe($expected);
})->with($test_cases);