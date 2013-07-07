function diff() {
	var num = 100;

	var answer = SquareOfSum(num) - SumOfSquares(num);
	console.log(answer);
}

function SumOfSquares(num) {
	var result = 0;
	for (var i = 1; i <= num; i++) {
		result += i * i;
	}
	console.log(result);
	return result;
}

function SquareOfSum(num) {
	var result = 0;
	for (var i = 1; i <= num; i++) {
		result += i;
	}

	result *= result;
	console.log(result);
	return result;
}

diff();