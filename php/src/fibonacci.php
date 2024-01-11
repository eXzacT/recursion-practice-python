<?php

function fib(int $n): int
{
    $prev = 0;
    $curr = 1;

    if ($n == $prev)
        return $prev;
    if ($n == $curr)
        return $curr;

    for ($i = 2; $i <= $n; $i++) {
        [$prev, $curr] = [$curr, $prev + $curr];
    }
    return $curr;
}

function fib_dp(int $n): int
{
    if ($n == 0)
        return 0;

    $dp = array_fill(0, $n, null);
    $dp[0] = 0;
    $dp[1] = 1;

    for ($i = 2; $i <= $n; $i++) {
        $dp[$i] = $dp[$i - 1] + $dp[$i - 2];
    }

    return $dp[$n];
}

function fib_rec(int $n): int
{
    if ($n <= 1)
        return $n;
    return fib_rec($n - 1) + fib_rec($n - 2);
}

function fib_rec_v2(int $n, int $curr = 0, int $nxt = 1): int
{
    if ($n == 0)
        return $curr;
    return fib_rec_v2($n - 1, curr: $nxt, nxt: $curr + $nxt);
}