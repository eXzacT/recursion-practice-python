<?php


function ackermann_dp(int $m, int $n): int
{
    $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    for ($i = 0; $i <= $m; $i++) {
        for ($j = 0; $j <= $n; $j++) {
            if ($i == 0) # Base case 1: A(0, n) = n+1
                $dp[0][$j] = $j + 1;
            else if ($j == 0) # Base case 2: A(m, 0) = A(m-1, 1)
                $dp[$i][0] = $dp[$i - 1][1];
            else {
                $row = $i - 1;
                $col = $dp[$i][$j - 1];  # A(m, n-1) INNER recursive call
                if ($row == 0)  # Same as base case 1, since we subtracted 1 and got 0
                    $res = $col + 1;
                # Recursive case: A(m, n) = A(m-1, INNER recursive call result)
                else if ($col <= $n)  # Can fetch the value from the table
                    $res = $dp[$i - 1][$col];
                else  # Compute it using a formula because the value is not in the table
                    $res = ($col - $n) * ($row) + $dp[$row][$n];

                $dp[$i][$j] = $res;
            }
        }
    }

    return $dp[$m][$n];
}

function ackermann_rec(int $m, int $n): int
{
    if ($m == 0)
        return $n + 1;
    if ($n == 0)
        return ackermann_rec($m - 1, 1);
    return ackermann_rec($m - 1, ackermann_rec($m, $n - 1));
}

function ackermann_rec_memo(int $m, int $n): int
{
    $memo = [];
    $helper = function (int $m, int $n) use ($memo, &$helper): int {
        $key = serialize([$m, $n]);
        if (isset($memo[$key])) {
            return $memo[$key];
        }
        if ($m == 0)
            return $n + 1;
        if ($n == 0)
            return $helper($m - 1, 1);

        $memo[$key] = $helper($m - 1, $helper($m, $n - 1));
        return $memo[$key];
    };

    return $helper($m, $n);
}