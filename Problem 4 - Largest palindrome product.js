function palindrome() {
	var arr = [];
	for (var i = 999; i > 99; i--) {
		for (var j = 999; j > 99; j--) {
			var mult = (i * j).toString();
		    if  (mult == mult.split('').reverse().join('')) {
		    	arr.push(mult);
		    	// console.log("i " + i + " j " + j);
		    	// console.log(i * j);
		    }
		}
	}
	console.log(Math.max.apply(Math, arr));
}

palindrome();