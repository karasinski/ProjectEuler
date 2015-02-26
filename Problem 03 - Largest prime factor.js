function prime() {
	var num = 600851475143;
	var i = 2;
	var divisors = [];

	while (num != 1) {
		if (num % i == 0) {
			divisors.push(i);
			num = num / i;
		}
		i++;
	}

	console.log(divisors);
	console.log(divisors[divisors.length - 1]);
}

prime();