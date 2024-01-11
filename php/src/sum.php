<?php

function sum(int $n): int
{
    $res = 0;
    for ($i = 1; $i <= $n; $i++) {
        $res += $i;
    }
    return $res;
}

function sum_reduce(int $n): int
{
    return array_reduce(range(0, $n), fn($carry, $curr) => $carry + $curr, initial: 0);
}

function sum_gauss(int $n): int
{
    return $n * ($n + 1) / 2;
}

function sum_rec(int $n): int
{
    return $n ? $n + sum_rec($n - 1) : 0;
}

function sum_tail_rec(int $n, int $acc = 0): int
{
    return $n ? sum_tail_rec($n - 1, $acc + $n) : $acc;
}
