<?php

function binary_search(array $arr, int $needle): int
{
    if (empty($arr))
        return -1;

    $lo = 0;
    $hi = count($arr);

    while ($lo <= $hi) {
        $mid = $lo + floor(($hi - $lo) / 2);
        if ($arr[$mid] == $needle) {
            return $mid;
        }
        if ($needle < $arr[$mid]) {
            $hi = $mid - 1;
        } else {
            $lo = $mid + 1;
        }
    }
    return -1;
}


function binary_search_rec(array $arr, int $needle): int
{
    if (empty($arr))
        return -1;

    $helper = function (int $lo, int $hi) use ($arr, $needle, &$helper): int {
        if ($lo > $hi) {
            return -1;
        }

        $mid = $lo + floor(($hi - $lo) / 2);
        if ($arr[$mid] == $needle) {
            return $mid;
        }
        if ($needle < $arr[$mid]) {
            return $helper($lo, $mid - 1);
        }
        return $helper($mid + 1, $hi);
    };

    return $helper(0, count($arr));
}
