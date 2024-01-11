<?php

function factorial(int $n): int
{
    $res = 1;
    for ($i = 1; $i <= $n; $i++) {
        $res *= $i;
    }

    return $res;
}

function factorial_reduce(int $n): int
{
    return $n ? array_reduce(range(1, $n), fn($carry, $item) => $carry * $item, 1) : 1;
}

function factorial_rec(int $n): int
{
    return $n <= 1 ? 1 : $n * factorial_rec($n - 1);
}

function factorial_tail_rec(int $n, int $acc = 1): int
{
    return $n <= 1 ? $acc : factorial_tail_rec($n - 1, $acc * $n);
}