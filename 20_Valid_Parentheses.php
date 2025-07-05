<?php
class Solution {
    public $s = "()"; // ✅ Declare as a class property

    function inValid($s) {
        echo "$s";
        $stack = [];
        $map =[
            ')' => '(',
            '}' => '{',
            ']' => '[',
        ];

       for ($i=0; $i < strlen($s); $i++) { 
         $char = $s[$i];
         if (in_array($char,['(','{','['] )) {
            array_push($stack, $char);
         }else{
            if (empty($stack) || array_pop($stack)
            ) {
            }
         }
       }

       
    }

}
$obj = new Solution();
$obj->inValid($obj->s);

