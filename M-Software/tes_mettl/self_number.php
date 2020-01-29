<?php
function generateSelfNumber($n) {
	$arr = [];
	$arrExclude = [];

	for ($i=0; $i<$n; $i++) {

		$sumOfSplit = array_sum(str_split($i));
		$sumTotal = $i+$sumOfSplit;

		array_push($arrExclude, $sumTotal);

		if (!in_array($i, $arrExclude)) {
			array_push($arr, $i);
		}
	}

	return $arr;
}

echo array_sum(generateSelfNumber(5000));

?>