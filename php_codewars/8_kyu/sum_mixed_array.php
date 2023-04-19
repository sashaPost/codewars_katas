<?php

function sum_mix($a) {
    $sum = 0;
    foreach($a as $item) {
        $sum += intval($item);
    }
    return $sum;
}

echo sum_mix([9, 3, '7', '3']);

?>