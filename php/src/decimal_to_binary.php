<?php

function decimal_to_binary(int $number): string
{
    if ($number == 0)
        return "0";

    $bin = "";
    while ($number) {
        $digit = $number % 2;
        $number = intdiv($number, 2);
        $bin = $digit . $bin;
    }
    return $bin;
}

function decimal_to_binary_rec(int $number): string
{
    if ($number == 0)
        return "0";

    $helper = function (int $number) use (&$helper) {
        return $number ? $number % 2 . $helper(intdiv($number, 2)) : '';
    };

    return $helper($number);
}

function decimal_to_binary_tail_rec(int $number): string
{
    if ($number == 0)
        return "0";

    $helper = function (int $number, string $acc = '') use (&$helper) {
        return $number ? $helper(intdiv($number, 2), $acc . $number % 2) : $acc;
    };

    return $helper($number);
}