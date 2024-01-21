<?php

// Given an m*n grid how many ways can you get from top left to bottom right
// You can only go down or right

function grid_traveller_dp(int $m, int $n): int
{
    $dp = array_fill(0, $m, array_fill(0, $n, 0));
    for ($i = 0; $i < $m; $i++) {
        $dp[$i][0] = 1;
    }
    for ($j = 1; $j < $n; $j++) {
        $dp[0][$j] = 1;
    }
    for ($i = 1; $i < $m; $i++) {
        for ($j = 1; $j < $n; $j++) {
            $dp[$i][$j] = $dp[$i - 1][$j] + $dp[$i][$j - 1];
        }
    }

    return $dp[$m - 1][$n - 1];
}

function grid_traveller_dp_v2(int $m, int $n): int
{
    $dp = array_fill(0, $m, array_fill(0, $n, 0));
    $dp[0][0] = 1;
    for ($i = 0; $i < $m; $i++) {
        for ($j = 0; $j < $n; $j++) {
            $current = $dp[$i][$j];
            if ($i + 1 < $m)
                $dp[$i + 1][$j] += $current;
            if ($j + 1 < $n)
                $dp[$i][$j + 1] += $current;
        }
    }

    return $dp[$m - 1][$n - 1];
}

function grid_traveller_rec(int $m, int $n): int
{
    $helper = function (int $m, int $n) use (&$helper): int {
        if ($m == 0 or $n == 0)
            return 0;
        if ($m == 1 and $n == 1)
            return 1;

        return $helper($m - 1, $n) + $helper($m, $n - 1);
    };
    return $helper($m, $n);
}

function grid_traveller_memo(int $m, int $n): int
{
    $memo = [serialize([1, 1]) => 1];
    $helper = function (int $m, int $n) use (&$helper, &$memo): int {
        if ($m == 0 or $n == 0)
            return 0;
        $key = serialize([$m, $n]);
        if (isset($memo[$key]))
            return $memo[$key];

        $memo[$key] = $helper($m - 1, $n) + $helper($m, $n - 1);
        return $memo[$key];
    };
    return $helper($m, $n);
}
function grid_traveller_rec_v2(int $m, int $n): int
{
    $helper = function (int $m, int $n) use (&$helper): int {
        if ($m == 1 and $n == 1)
            return 1;
        $down = $right = 0;
        if ($m > 1)
            $down = $helper($m - 1, $n);
        if ($n > 1)
            $right = $helper($m, $n - 1);

        return $down + $right;
    };
    return $helper($m, $n);
}

function grid_traveller_memo_v2(int $m, int $n): int
{
    $memo = [serialize([1, 1]) => 1];
    $helper = function (int $m, int $n) use (&$helper, &$memo, &$memo_hits): int {
        $key = serialize([$m, $n]);
        if (isset($memo[$key])) {
            return $memo[$key];
        }

        $down = $right = 0;
        if ($m > 1)
            $down = $helper($m - 1, $n);
        if ($n > 1)
            $right = $helper($m, $n - 1);

        $memo[$key] = $down + $right;
        return $memo[$key];
    };
    return $helper($m, $n);
}

function grid_traveller_rec_v3(int $m, int $n): int
{
    $helper = function (int $m, int $n) use (&$helper): int {
        if ($m == 1 and $n == 1)
            return 1;
        if ($m == 1)
            return $helper($m, $n - 1);
        if ($n == 1)
            return $helper($m - 1, $n);

        return $helper($m - 1, $n) + $helper($m, $n - 1);
    };
    return $helper($m, $n);
}

function grid_traveller_memo_v3(int $m, int $n): int
{
    $memo = [serialize([1, 1]) => 1];
    $helper = function (int $m, int $n) use (&$helper, &$memo, &$memo_hits): int {
        $key = serialize([$m, $n]);
        if (isset($memo[$key])) {
            return $memo[$key];
        }
        if ($m == 1)
            return $helper($m, $n - 1);
        if ($n == 1)
            return $helper($m - 1, $n);

        $memo[$key] = $helper($m - 1, $n) + $helper($m, $n - 1);
        return $memo[$key];
    };

    return $helper($m, $n);
}

