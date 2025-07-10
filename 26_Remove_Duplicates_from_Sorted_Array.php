<?php

class Solution {

    /**
     * Removes duplicates from a sorted array in-place.
     * @param Integer[] $nums
     * @return Integer The number of unique elements
     */
    function removeDuplicates(&$nums) {
        if (count($nums) == 0) return 0;

        $index = 1;

        for ($i = 1; $i < count($nums); $i++) {
            if ($nums[$i] != $nums[$i - 1]) {
                $nums[$index] = $nums[$i];
                $index++;
            }
        }

        return $index;
    }
}

// ======== TEST CODE =========
$nums = [1, 1, 2, 2, 3, 4, 4];
$solution = new Solution();
$length = $solution->removeDuplicates($nums);

echo "✅ Total Unique Elements: $length\n";
echo "✅ Modified Array: ";
for ($i = 0; $i < $length; $i++) {
    echo $nums[$i] . " ";
}
// 
echo "\n";
