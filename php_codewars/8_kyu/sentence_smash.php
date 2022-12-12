<?php

function smash($words) {
    return implode(" ", $words);
}

// found something odd:
// function smash(array $words): string {
//     return eval(base64_decode('
//                cmV0dXJuIGltc     GxvZGUoJyAnL
//             CAkd29yZHMpOyAvLyDRhCDRi9Cy0YTRgtGI
//           0LLQvNCz0YTRiNGC0LLRhNC80YjQstCz0LzRhNG
//             G0LLQvNCz0YjRhtGE0LLQs9C80YjRhtGE0L
//               LQs9C80YjRidGE0YbQs9Cy0YjRidC8
//                 0YTRhtGL0LPQstGJ0LPRhNGJ0L
//                   zQstCz0YTRhtCy0LzRhtGE
//                     0YnQstC80YTQstC80Y
//                       TQstCz0LzRhNGG
//                         0YLQstC80L
//                           PRiNGG
//                             0=
//   '));
//   }

echo smash(["hello", "world"]) . "\n";
echo smash(["hello"]) . "\n";

?>