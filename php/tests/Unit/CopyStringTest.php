<?php

require __DIR__ . '/../../src/copy_string.php';


$test_cases = [
    ["originalstring", "originalstring"],
    ["", ""],
];

it('copies the string', function ($input, $expected) {
    expect(copy_string($input))->toBe($expected);
    expect(copy_string_rec($input))->toBe($expected);
    expect(copy_string_tail_rec($input))->toBe($expected);
})->with($test_cases);