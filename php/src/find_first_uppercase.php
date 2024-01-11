<?php


function find_first_uppercase(string $s): int
{
    for ($i = 0; $i < strlen($s); $i++) {
        if (ctype_upper($s[$i])) {
            return $i;
        }
    }
    return -1;
}

function find_first_uppercase_ascii(string $s): int
{
    for ($i = 0; $i < strlen($s); $i++) {
        if (ord($s[$i]) >= 65 && ord($s[$i]) <= 90) {
            return $i;
        }
    }
    return -1;
}


function find_first_uppercase_rec(string $s, int $idx = 0): int
{
    if ($idx == strlen($s)) {
        return -1;
    }
    return ctype_upper($s[$idx]) ? $idx : find_first_uppercase_rec($s, $idx + 1);
}