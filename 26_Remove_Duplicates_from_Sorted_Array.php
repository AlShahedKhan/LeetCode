<?php

class Solution {
    function removeDuplicates(&$nums){
        if (count($nums) == 0 ) {
            return 0;
        }

        $index = 1;

        for ($i=0; $i < count($nums); $i++) { 
            echo "$index";
        }
    }
}

$nums = [1, 1, 2];
$solution = new Solution();
$length = $solution->removeDuplicates($nums);