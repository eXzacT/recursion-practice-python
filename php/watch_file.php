#!/usr/bin/env php
<?php

# Check if an argument is provided
if ($argc < 2) {
    echo "Usage: just watch <filename>\n";
    exit(1);
}

# Get the current modification time of the file
$filename = $argv[1] . ".php";
$full_path = getcwd() . DIRECTORY_SEPARATOR . 'src' . DIRECTORY_SEPARATOR . $filename;
if (file_exists($full_path)) {
    echo "Watching file $filename\n\n";
    $current_mod_time = filemtime($full_path);
} else {
    echo "The file $filename does not exist\n";
    exit(1);
}

while (true) {
    clearstatcache(); # Clear cached results of filemtime
    # If the modification time has changed, run the command
    if ($current_mod_time != filemtime($full_path)) {
        $current_mod_time = filemtime($full_path);
        $output = null;
        $retval = null;
        $filename = explode('_', $filename)[0];
        exec("vendor\bin\pest --colors=always --filter={$filename}", $output, $retval);
        echo implode("\n", $output);
    }
    # Wait for a while before checking again
    sleep(1);
}
