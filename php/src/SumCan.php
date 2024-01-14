<?php


function sum_can_dp(int $total, array $arr): bool
{
    $dp = array_fill(0, $total + 1, false);
    $dp[0] = true;
    for ($i = 0; $i <= $total; $i++) {
        if ($dp[$i]) {
            foreach ($arr as $num) {
                if (($res = $i + $num) <= $total)
                    $dp[$res] = true;
            }
        }
    }
    return end($dp);
}

function sum_can_dp_v2(int $total, array $arr): bool
{
    $dp = array_fill(0, $total + 1, false);
    $dp[0] = true;
    for ($i = 0; $i <= $total; $i++) {
        if ($dp[$i]) {
            foreach ($arr as $num) {
                $res = $i + $num;
                if ($res == $total)
                    return true;
                if ($res < $total)
                    $dp[$res] = true;
            }
        }
    }
    return end($dp);
}

function sum_can_rec(int $total, array $arr): bool
{
    $helper = function (int $remainder, int $idx = 0) use ($arr, &$helper): bool {
        if ($remainder < 0 || $idx == count($arr))
            return false;
        if ($remainder == 0)
            return true;

        return $helper($remainder - $arr[$idx], $idx) || $helper($remainder, $idx + 1);
    };

    return $helper($total);
}

function sum_can_memo(int $total, array $arr): bool
{
    $memo = [0 => true];
    $memo_hits = 0;

    $helper = function (int $remainder, int $idx = 0) use ($arr, &$memo_hits, &$memo, &$helper): bool {
        if ($remainder < 0 || $idx == count($arr))
            return false;

        if (isset($memo[$remainder])) {
            $memo_hits += 1;
            return $memo[$remainder];
        }

        $memo[$remainder] = $helper($remainder - $arr[$idx], $idx) || $helper($remainder, $idx + 1);
        return $memo[$remainder];
    };

    $res = $helper($total);
    //echo "Memo hits: $memo_hits ";
    return $res;
}

function sum_can_rec_v2(int $total, array $arr): bool
{
    $helper = function (int $remainder) use ($arr, &$helper): bool {
        if ($remainder < 0)
            return false;
        if ($remainder == 0)
            return true;

        foreach ($arr as $num) {
            if ($helper($remainder - $num))
                return true;
        }
        return false;
    };

    return $helper($total);
}

function sum_can_memo_v2(int $total, array $arr): bool
{
    $memo = [0 => true];
    $memo_hits = 0;
    $helper = function (int $remainder) use ($arr, &$memo_hits, &$memo, &$helper): bool {
        static $memo_hits = 0;
        if (isset($memo[$remainder])) {
            $memo_hits += 1;
            return $memo[$remainder];
        }
        if ($remainder < 0)
            return false;
        foreach ($arr as $num) {
            if ($helper($remainder - $num)) {
                return true;
            }
        }
        $memo[$remainder] = false;
        return false;
    };

    $res = $helper($total);
    //echo "Memo hits: $memo_hits ";
    return $res;
}