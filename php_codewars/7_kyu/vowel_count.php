<?php

function getCount($str) {
    $vowels = ["a", "e", "i", "o", "u"];
    $vowelsCount = 0;
    
    foreach(str_split($str) as $letter) {
        if (in_array($letter, $vowels)) {
            $vowelsCount += 1;
        }
    }
    
    return $vowelsCount;
}

echo getCount("abracadabra");

?>