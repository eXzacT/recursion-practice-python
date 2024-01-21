<?php

function hanoi_rec(int $n): array
{
    $moves = [];
    $move = function (int $disk, int $source, int $dest) use (&$moves): void {
        $moves[] = "Moving disk $disk from rod $source to rod $dest";
    };

    $helper = function (int $n, int $source, int $aux, int $dest) use ($move, &$helper): void {
        if ($n == 1) {
            $move($n, $source, $dest);
            return;
        }

        $helper($n - 1, $source, $dest, $aux);
        $move($n, $source, $dest);
        $helper($n - 1, $aux, $source, $dest);
    };

    $helper($n, 1, 2, 3);
    return $moves;
}

function hanoi_rec_v2(int $n): array
{
    $moves = [];
    $move = function (int $disk, int $source, int $dest) use (&$moves): void {
        $moves[] = "Moving disk $disk from rod $source to rod $dest";
    };
    $helper = function (int $n, int $source, int $dest) use ($move, &$helper): void {
        if ($n == 1) {
            $move($n, $source, $dest);
            return;
        }
        $aux = 6 - $source - $dest;
        $helper($n - 1, $source, $aux);
        $move($n, $source, $dest);
        $helper($n - 1, $aux, $dest);
    };

    $helper($n, 1, 3);
    return $moves;
}