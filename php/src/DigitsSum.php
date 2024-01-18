<?php

function digits_sum_string(int $num): int
{
    $sum = 0;
    $numstr = (string) $num;
    foreach (str_split($numstr) as $digit) {
        $sum += (int) $digit;
    }
    return $sum;
}

function digits_sum_modulo(int $num): int
{
    $sum = 0;
    while ($num) {
        $digit = $num % 10;
        $sum += $digit;
        $num = intdiv($num, 10);
    }
    return $sum;
}

function digits_sum_reduce(int $num): int
{
    return array_reduce(str_split((string) $num), fn($acc, $digit) => $acc + (int) $digit);
}

function digits_sum_rec(int $num): int
{
    $helper = function (int $num, int $acc = 0) use (&$helper): int {
        return $num ? $helper(intdiv($num, 10), $acc + $num % 10) : $acc;
    };
    return $helper($num);
}