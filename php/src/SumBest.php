<?php

function sum_best_dp(int $target, array $nums): array|null
{
    $dp = array_fill(0, $target + 1, null);
    $dp[0] = [];
    for ($i = 0; $i <= $target; $i++) {
        if ($dp[$i] !== null) {
            foreach ($nums as $num) {
                if ($i + $num <= $target) {
                    if ($dp[$i + $num] === null or (count($dp[$i]) + 1) < count($dp[$i + $num]))
                        $dp[$i + $num] = [$num, ...$dp[$i]];
                }
            }
        }
    }
    return $dp[$target];
}

function sum_best_rec(int $target, array $nums): array|null
{
    $helper = function (int $remainder) use ($nums, &$helper): array|null {
        if ($remainder < 0)
            return null;
        if ($remainder == 0)
            return [];

        $best = null;
        foreach ($nums as $num) {
            if (($res = $helper($remainder - $num)) !== null) {
                $combination = [...$res, $num];
                if ($best === null or count($combination) < count($best))
                    $best = $combination;
            }
        }

        return $best;
    };
    return $helper($target);
}


function sum_best_memo(int $target, array $nums): array|null
{
    $memo = [0 => []];
    $helper = function (int $remainder) use ($nums, &$memo, &$helper): array|null {
        if ($remainder < 0)
            return null;
        if (array_key_exists($remainder, $memo))
            return $memo[$remainder];

        $best = null;
        foreach ($nums as $num) {
            if (($res = $helper($remainder - $num)) !== null) {
                $combination = [...$res, $num];
                if ($best === null or count($combination) < count($best))
                    $best = $combination;
            }
        }
        $memo[$remainder] = $best;
        return $best;
    };
    return $helper($target);
}

function sum_best_rec_v2(int $target, array $nums): array|null
{
    $best = null;
    $helper = function (int $remainder, array $combination = [], int $idx = 0) use ($nums, &$best, &$helper) {
        if ($remainder < 0 or $idx == count($nums))
            return null;
        if ($remainder == 0)
            return $combination;
        $with = $helper($remainder - $nums[$idx], [$nums[$idx], ...$combination], $idx);
        if ($with !== null && ($best === null || count($with) < count($best))) {
            $best = $with;
        }

        $helper($remainder, $combination, $idx + 1);
    };

    $helper($target);
    return $best;
}

function sum_best_rec_v2_early(int $target, array $nums): array|null
{
    $best = null;
    $helper = function (int $remainder, array $combination = [], int $idx = 0) use ($nums, &$best, &$helper) {
        if ($remainder < 0 or $idx == count($nums))
            return null;
        if ($remainder == 0)
            return $combination;

        // Early return as soon as we go above best combination in length
        if ($best !== null and count($combination) > count($best))
            return null;

        $with = $helper($remainder - $nums[$idx], [$nums[$idx], ...$combination], $idx);
        if ($with !== null && ($best === null || count($with) < count($best))) {
            $best = $with;
        }

        $helper($remainder, $combination, $idx + 1);
    };

    $helper($target);
    return $best;
}

function sum_best_memo_v2(int $target, array $nums): array|null
{
    $memo = [0 => []];
    $helper = function (int $remainder, int $idx = 0) use ($nums, &$memo, &$helper): array|null {
        if ($remainder < 0 or $idx == count($nums))
            return null;
        if (array_key_exists($remainder, $memo))
            return $memo[$remainder];

        $with = $helper($remainder - $nums[$idx], 0);
        if ($with !== null)
            $with[] = $nums[$idx];

        $without = $helper($remainder, $idx + 1);

        // Pick the shortest combination so far
        if ($with === null or ($without !== null and count($without) < count($with)))
            $memo[$remainder] = $without;
        else
            $memo[$remainder] = $with;

        return $memo[$remainder];
    };

    return $helper($target);
}