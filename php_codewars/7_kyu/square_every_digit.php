<?php

function square_digits($num): int {
    $str = '';
    foreach (str_split((string)$num) as $n) {
      $str .= (string)(intval($n)**2);
    }
    return intval($str);
  }