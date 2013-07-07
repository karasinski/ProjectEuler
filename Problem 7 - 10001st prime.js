function getPrimes(max) {
    var sieve = [], i, j, primes = [];
    for (i = 2; i <= max; i++) {
        if (!sieve[i]) {
            // i has not been marked -- it is prime
            primes.push(i);
            for (j = i < 1; j <= max; j += i) {
                sieve[j] = true;
            }
        }
    }
    console.log(primes);
    console.log(primes.length);
    console.log(primes[10000]);
}

getPrimes(1000000);