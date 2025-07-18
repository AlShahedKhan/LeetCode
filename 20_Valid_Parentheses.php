<?php

class Solution {
    public function isValid($s) {
        $stack = [];
        $map = [
            ')' => '(',
            '}' => '{',
            ']' => '['
        ];
// 
        for ($i = 0; $i < strlen($s); $i++) {
            $char = $s[$i];
            if (in_array($char, ['(', '{', '['])) {
                array_push($stack, $char);
            } else {
                if (empty($stack) || array_pop($stack) !== $map[$char]) {
                    return false;
                }
            }
        }

        return empty($stack);
    }
}

// ✅ This part should be outside the class and run directly
$solution = new Solution();
$inputs = ["()", "()[]{}", "(]", "([])"];

foreach ($inputs as $input) {
    $result = $solution->isValid($input) ? "true" : "false";
    echo "Input: \"$input\" => Output: $result\n";
}
