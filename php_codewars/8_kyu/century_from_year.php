<?php

function centuryFromYear($year) {
    if ($year % 100 == 0) {
        return $year / 100;
    } else {
        return (($year - $year % 100) / 100) + 1;
    }
    // OR
    // return ceil($year / 100);
}

echo centuryFromYear(1705) . "\n";
echo centuryFromYear(1900) . "\n";
echo centuryFromYear(1601) . "\n";
echo centuryFromYear(1612) . "\n";
echo centuryFromYear(2000) . "\n";

?>