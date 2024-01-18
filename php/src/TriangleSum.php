<?php

/**
 * @param int[]$nums
 * @return int[][]
 */
function triangle_sum(array $nums): array
{
    $triangle = [$nums];
    while (count($nums) > 1) {
        $temp = [];
        for ($i = 0; $i < count($nums) - 1; $i++) {
            $curr = $nums[$i] + $nums[$i + 1];
            $temp[] = $curr;
        }
        $triangle[] = $temp;
        $nums = $temp;
    }
    return $triangle;
}

/**
 * @param int[]$nums
 * @return int[][]
 */
function triangle_sum_rec(array $nums): array
{
    $triangle = [$nums];
    $helper = function (array $nums) use (&$triangle, &$helper) {
        if (count($nums) == 1)
            return $triangle;

        $row = [];
        for ($i = 0; $i < count($nums) - 1; $i++) {
            $row[] = $nums[$i] + $nums[$i + 1];
        }
        $triangle[] = $row;
        return $helper($row);
    };

    $helper($nums);
    return $triangle;
}