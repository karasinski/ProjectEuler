function Fibonacci() {
	var fib = [1, 1];

	while (fib[fib.length-1] < 4000000) {
		fib.push((fib[fib.length-1] + fib[fib.length-2]))
	}
	fib.pop();

	// console.log("One: " + fib[fib.length-2] + ", Two: " + fib[fib.length-1]);
	// console.log(fib);

	var sum = 0;
	for (var i = 0; i < fib.length; i++) {
		if (fib[i] % 2 == 0) sum += fib[i];
		console.log(fib[i]);
	}

	console.log(sum);
}

Fibonacci();