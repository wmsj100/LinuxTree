---
title: 遗失的代码
date: 2016-03-24 12:18:58
tags: [JavaScript]
categories: Dynamic
---
- 范例一：	filter 返回数组中符合条件的值
  <!-- more -->
          // Define a callback function.
      	function CheckIfPrime(value, index, ar) {
      	high = Math.floor(Math.sqrt(value)) + 1;
      	
      	for (var div = 2; div <= high; div++) {
      	if (value % div == 0) {
      	return false;
      	}
      	}
      	return true;
      	}
      	
      	// Create the original array.
      	var numbers = [31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53];
      	
      	// Get the prime numbers that are in the original array. 
      	var primes = numbers.filter(CheckIfPrime);
      	
      	document.write(primes);
      	// Output: 31,37,41,43,47,53

- 范例二：
