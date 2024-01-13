<?php

function array_mean(array $arr): int
{
    return array_sum($arr) / count($arr);
}

function array_mean_iter(array $arr): int
{
    $sum = 0;
    foreach ($arr as $num) {
        $sum += $num;
    }
    return $sum / count($arr);
}

function array_mean_rec(array $arr): int
{
    $helper = function (int $idx = 0) use ($arr, &$helper): int {
        return $idx == count($arr) ? 0 : $arr[$idx] + $helper($idx + 1);
    };
    return $helper() / count($arr);
}

function array_mean_tail_rec(array $arr): int
{
    $helper = function (int $idx = 0, int $acc = 0) use ($arr, &$helper): int {
        return $idx == count($arr) ? $acc / count($arr) : $helper($idx + 1, $acc + $arr[$idx]);
    };
    return $helper();
}