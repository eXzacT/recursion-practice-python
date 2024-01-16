<?php

function sum_how_dp(int $target, array $arr): array|null
{
    $dp = array_fill(0, $target + 1, null);
    $dp[0] = [];
    for ($i = 0; $i <= $target; $i++) {
        if ($dp[$i] !== null) {
            foreach ($arr as $num) {
                if ($i + $num < $target) {
                    $dp[$i + $num] = array_merge($dp[$i], [$num]);
                    continue;
                }
                if ($i + $num == $target) {
                    return array_merge($dp[$i], [$num]);
                }
            }
        }
    }
    return $dp[$target];
}

function sum_how_rec(int $target, array $arr): array|null
{
    $helper = function (int $remainder, int $idx = 0) use ($arr, &$helper): array|null {
        if ($remainder < 0 || $idx == count($arr))
            return null;
        if ($remainder == 0)
            return [];

        $res = $helper($remainder - $arr[$idx], $idx);
        if ($res !== null)
            return array_merge([$arr[$idx]], $res);

        $res = $helper($remainder, $idx + 1);
        if ($res !== null)
            return $res;

        return null;
    };
    return $helper($target);
}

function sum_how_memo(int $target, array $arr): array|null
{
    $memo = [0 => []];
    $helper = function (int $remainder, int $idx = 0) use ($arr, &$memo, &$helper): array|null {
        if ($remainder < 0 || $idx == count($arr))
            return null;
        if (isset($memo[$remainder]))
            return $memo[$remainder];

        $res = $helper($remainder - $arr[$idx], $idx);
        if ($res !== null)
            return array_merge([$arr[$idx]], $res);

        $res = $helper($remainder, $idx + 1);
        if ($res !== null)
            return $res;

        $memo[$remainder] = null;
        return null;
    };
    return $helper($target);
}


function sum_how_rec_v2(int $target, array $arr): array|null
{
    $helper = function (int $remainder) use ($arr, &$helper): array|null {
        if ($remainder < 0)
            return null;
        if ($remainder == 0)
            return [];

        foreach ($arr as $num) {
            if (($res = $helper($remainder - $num)) !== null)
                return array_merge([$num], $res);
        }
        return null;
    };
    return $helper($target);
}

function sum_how_memo_v2(int $target, array $arr): array|null
{
    $memo = [0 => []];

    $helper = function (int $remainder) use ($arr, &$memo, &$helper): array|null {
        if ($remainder < 0) {
            return null;
        }
        if (isset($memo[$remainder])) {
            return $memo[$remainder];
        }

        foreach ($arr as $num) {
            $res = $helper($remainder - $num);
            if ($res !== null) {
                $memo[$remainder] = array_merge([$num], $res);
                return $memo[$remainder];
            }
        }
        $memo[$remainder] = null;
        return null;
    };

    return $helper($target);
}