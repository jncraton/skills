all: test

primes: primes.cpp
	g++ -std=c++23 $< -Wall -O2 -o $@

test: primes
	./primes

format:
	clang-format -style google -i *.cpp

clean:
	rm -f primes