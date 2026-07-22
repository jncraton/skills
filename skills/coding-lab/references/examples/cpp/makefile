all: test

primes: primes.cpp
	g++ -std=c++23 $< -Wall -O2 -o $@

test: primes
	./primes

clean:
	rm -f primes