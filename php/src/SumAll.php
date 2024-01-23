<?php


function sum_all_dp(int $target, array $nums): array|null
{
    $dp = array_fill(0, $target + 1, null);
    $dp[0] = [[]];
    for ($i = 1; $i <= $target; $i++) {
        foreach ($nums as $num) {
            if ($i - $num >= 0) {
                // To construct number 'i' we can use all the combinations to construct i-num, by adding that num
                foreach ($dp[$i - $num] as $subarr) {
                    // This check ensures we don't get all the permutations
                    if (empty($subarr) || $num <= $subarr[0]) {
                        $subarr = [$num, ...$subarr];
                        $dp[$i][] = $subarr;
                    }
                }
            }
        }
    }
    return $dp[$target];
}


function sum_all_rec(int $target, array $nums): array|null
{
    $combinations = [];
    $helper = function (int $remainder, int $last_used = 0, array $comb = []) use ($nums, &$helper, &$combinations): void {
        if ($remainder < 0 or $last_used == count($nums))
            return;
        if ($remainder == 0) {
            $combinations[] = $comb;
            return;
        }

        $helper($remainder - $nums[$last_used], $last_used, [...$comb, $nums[$last_used]]);
        $helper($remainder, $last_used + 1, $comb);
    };
    $helper($target);
    return count($combinations) ? $combinations : null;
}


function sum_all_memo(int $target, array $nums): array|null
{
    $memo = [];
    $helper = function (int $remainder, int $last_used = 0) use ($nums, &$helper, &$memo_hits, &$memo): array|null {
        $key = serialize([$last_used, $remainder]);
        if (array_key_exists($key, $memo))
            return $memo[$key];
        if ($remainder < 0 or $last_used == count($nums))
            return null;
        if ($remainder == 0)
            return [[]];

        $new_combs = null;

        $combs = $helper($remainder - $nums[$last_used], $last_used);
        if ($combs !== null) {
            foreach ($combs as $comb) {
                $comb = [$nums[$last_used], ...$comb];
                $new_combs[] = $comb;
            }
        }

        $combs = $helper($remainder, $last_used + 1);
        if ($combs !== null) {
            foreach ($combs as $comb) {
                $new_combs[] = $comb;
            }
        }

        $memo[$key] = $new_combs;
        return $new_combs;
    };

    return $helper($target);
}

function sum_all_rec_v2(int $target, array $nums): array|null
{
    $helper = function (int $remainder, int $last_used = 0) use ($nums, &$helper): array|null {
        if ($remainder == 0)
            return [[]];
        if ($remainder < 0)
            return null;

        $new_combs = null;
        for ($i = $last_used; $i < count($nums); $i++) {
            $combs = $helper($remainder - $nums[$i], $i);
            if ($combs !== null) {
                foreach ($combs as $comb) {
                    $comb = [$nums[$i], ...$comb];
                    $new_combs[] = $comb;
                }
            }
        }
        return $new_combs;
    };
    return $helper($target);
}

function sum_all_memo_v2(int $target, array $nums): array|null
{
    $memo = [];
    $helper = function (int $remainder, int $last_used = 0) use ($nums, &$helper, &$memo): array|null {
        $key = serialize([$remainder, $last_used]);
        if (array_key_exists($key, $memo)) {
            return $memo[$key];
        }
        if ($remainder == 0)
            return [[]];
        if ($remainder < 0)
            return null;

        $new_combs = null;
        for ($i = $last_used; $i < count($nums); $i++) {
            $combs = $helper($remainder - $nums[$i], $i);
            if ($combs !== null) {
                foreach ($combs as $comb) {
                    $comb = [$nums[$i], ...$comb];
                    $new_combs[] = $comb;
                }
            }
        }

        $memo[$key] = $new_combs;
        return $new_combs;
    };
    return $helper($target);
}