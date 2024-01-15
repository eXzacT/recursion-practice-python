<?php

function sum_count_dp(int $target, array $arr): int
{
    $dp = array_fill(0, $target + 1, 0);
    $dp[0] = 1;
    foreach ($arr as $num) {
        // Increment ways to get to 'i' by ways to get to i-num, because we can add num and get to 'i'
        for ($i = $num; $i <= $target; $i++)
            $dp[$i] += $dp[$i - $num];
    }

    return $dp[$target];
}

function sum_count_rec(int $target, array $arr): int
{
    $helper = function (int $sum_so_far, int $last_used_idx = 0) use (&$helper, $arr): int {
        if ($sum_so_far < 0)
            return 0;
        if ($sum_so_far == 0)
            return 1;

        $count = 0;
        // Start from last used so we don't get permutations
        for ($i = $last_used_idx; $i < count($arr); $i++)
            $count += $helper($sum_so_far - $arr[$i], $i);

        return $count;
    };
    return $helper($target);
}

function sum_count_memo(int $target, array $arr): int
{
    $memo = [];
    $memo_hits = 0;
    $helper = function (int $sum_so_far, int $last_used_idx = 0) use (&$helper, &$memo, &$memo_hits, $arr): int {
        $key = serialize([$sum_so_far, $last_used_idx]);
        if (isset($memo[$key])) {
            $memo_hits++;
            return $memo[$key];
        }
        if ($sum_so_far < 0)
            return 0;
        if ($sum_so_far == 0)
            return 1;

        $count = 0;
        // Start from last used so we don't get permutations
        for ($i = $last_used_idx; $i < count($arr); $i++)
            $count += $helper($sum_so_far - $arr[$i], $i);

        $memo[$key] = $count;
        return $count;
    };
    $res = $helper($target);
    //echo "Memo hits:$memo_hits", "\n";
    return $res;
}

function sum_count_rec_v2(int $target, array $arr): int
{
    $helper = function (int $sum_so_far, int $idx = 0) use (&$helper, $arr): int {
        if ($sum_so_far < 0 || $idx == count($arr))
            return 0;
        if ($sum_so_far == 0)
            return 1;

        return $helper($sum_so_far - $arr[$idx], $idx) + $helper($sum_so_far, $idx + 1);
    };
    return $helper($target);
}


function sum_count_memo_v2(int $target, array $arr): int
{
    $memo = [];
    $memo_hits = 0;
    $helper = function (int $sum_so_far, int $idx = 0) use (&$helper, &$memo, &$memo_hits, $arr): int {
        $key = serialize([$sum_so_far, $idx]);
        if (isset($memo[$key])) {
            $memo_hits++;
            return $memo[$key];
        }
        if ($sum_so_far < 0 || $idx == count($arr))
            return 0;
        if ($sum_so_far == 0)
            return 1;

        $memo[$key] = $helper($sum_so_far - $arr[$idx], $idx) + $helper($sum_so_far, $idx + 1);
        return $memo[$key];
    };

    $res = $helper($target);
    //echo "Memo hits:$memo_hits", "\n";
    return $res;
}