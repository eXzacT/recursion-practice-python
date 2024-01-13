#!/usr/bin/env php
<?php

if ($argc < 2) {
    echo "Usage: just create <filename>\n";
    exit(1);
}

$filename = $argv[1];
$rootDir = getcwd();
$srcDir = $rootDir . DIRECTORY_SEPARATOR . 'src';
$templateDir = $srcDir . DIRECTORY_SEPARATOR . 'template';
$testDir = $rootDir . DIRECTORY_SEPARATOR . 'Tests' . DIRECTORY_SEPARATOR . 'Unit';

// Get template contents
$srcTemplateFilename = $templateDir . DIRECTORY_SEPARATOR . "Source.php";
$srcTemplateContents = file_get_contents($srcTemplateFilename);
$testTemplateFilename = $templateDir . DIRECTORY_SEPARATOR . "Test.php";
$testTemplateContents = file_get_contents($testTemplateFilename);

// Create the source file and write template content
$srcFile = $srcDir . DIRECTORY_SEPARATOR . $filename . ".php";
$handle = fopen($srcFile, 'w');
fwrite($handle, $srcTemplateContents);
fclose($handle);

// Create the test file, replace $filename string and write the new content
$testFile = $testDir . DIRECTORY_SEPARATOR . $filename . "Test.php";
$handle = fopen($testFile, 'w');
$newContent = str_replace('$filename', $filename, $testTemplateContents);
fwrite($handle, $newContent);
fclose($handle);

echo "File $filename and its corresponding test created successfully from template src/template\n";
