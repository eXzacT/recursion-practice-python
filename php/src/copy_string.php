<?php

function copy_string(string $s): string
{
    $new_str = "";
    for ($i = 0; $i < strlen($s); $i++) {
        $new_str .= $s[$i];
    }
    return $new_str;
}

function copy_string_rec(string $s): string
{
    $helper = function (int $idx = 0) use ($s, &$helper): string {
        if ($idx == strlen($s))
            return "";
        return $s[$idx] . $helper($idx + 1);
    };

    return $helper();
}

function copy_string_tail_rec(string $s): string
{
    $helper = function (int $idx = 0, string $acc = "") use ($s, &$helper): string {
        if ($idx == strlen($s))
            return $acc;
        return $helper($idx + 1, $acc . $s[$idx]);
    };

    return $helper();
}