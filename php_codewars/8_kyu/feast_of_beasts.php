<?php

function feast($beast, $dish){
//   return $beast[0] . " " . $beast[-1] . "\n";
    if ($beast[0] == $dish[0] and $beast[-1] == $dish[-1]) {
        return true;
    } else {
        return false;
    }
}

echo feast("great blue heron", "garlic naan");
echo feast("chickadee", "chocolate cake");
echo feast("brown bear", "bear claw");

?>