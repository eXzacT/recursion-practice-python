<?php

function can_construct_dp(string $target, array $word_bank): bool
{
    $dp = array_fill(0, strlen($target) + 1, null);
    $dp[0] = "";
    for ($i = 0; $i <= strlen($target); $i++) {
        if ($dp[$i] !== null) {
            foreach ($word_bank as $word) {
                $new_word = $dp[$i] . $word;
                if ($new_word == $target)
                    return true;
                if (!str_starts_with($target, $new_word))
                    continue;

                $dp[strlen($new_word)] = $new_word;
            }
        }
    }
    return false;
}

function can_construct_dp_v2(string $target, array $word_bank): bool
{
    $dp = array_fill(0, strlen($target) + 1, false);
    $dp[0] = true;
    for ($i = 0; $i <= strlen($target); $i++) {
        if ($dp[$i]) {
            foreach ($word_bank as $word) {
                if ($word == substr($target, $i, strlen($word)))
                    $dp[$i + strlen($word)] = true;
            }
        }
    }
    return end($dp);
}

function can_construct_rec(string $target, array $word_bank): bool
{
    $helper = function (int $idx = 0) use ($target, $word_bank, &$helper) {
        if ($idx == strlen($target))
            return true;
        foreach ($word_bank as $word) {
            if (str_starts_with(substr($target, $idx), $word)) {
                if ($helper($idx + strlen($word))) {
                    return true;
                }
            }
        }
        return false;
    };

    return $helper();
}


function can_construct_rec_v2(string $target, array $word_bank): bool
{
    $helper = function (string $target, int $idx = 0) use ($word_bank, &$helper) {
        if ($idx == count($word_bank))
            return false;
        if ($target == "")
            return true;

        if (str_starts_with($target, $word_bank[$idx]))
            return $helper(ltrim($target, $word_bank[$idx]), 0) || $helper($target, $idx + 1);

        return $helper($target, $idx + 1);
    };

    return $helper($target);
}

function can_construct_rec_v3(string $target, array $word_bank): bool
{
    $helper = function (string $target) use ($word_bank, &$helper) {
        if (empty($target)) {
            return true;
        }
        foreach ($word_bank as $word) {
            if (str_starts_with($target, $word)) {
                if ($helper(ltrim($target, $word))) {
                    return true;
                }
            }
        }
        return false;
    };

    return $helper($target);
}

function can_construct_rec_memo(string $target, array $word_bank): bool
{
    $memo = ["" => true];
    $helper = function (string $target) use ($word_bank, $memo, &$helper) {
        if (isset($memo[$target])) {
            return true;
        }
        foreach ($word_bank as $word) {
            if (str_starts_with($target, $word)) {
                $memo[$target] = $helper(ltrim($target, $word));
                if ($memo[$target]) {
                    return true;
                }
            }
        }
        $memo[$target] = false;
        return false;
    };

    return $helper($target);
}