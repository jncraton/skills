## readme.md

````markdown
# Primes

This lab introduces C++ programming through the task of generating the first 100 prime numbers.

## Learning Outcomes

After completing this experience, learners will be able to:

1. Use modern C++ features including `<println>` for output
2. Implement loops and conditional logic
3. Work with vectors and basic algorithms
4. Write and run automated tests

## Usage

The code includes a number of embedded tests that can be run using:

```
make test
```

The output should show the first 100 prime numbers and the results of the automated tests.

## Tasks

1. Implement `is_prime`
2. Implement `get_primes`
3. Implement `main` to print the results

## Resources

- [std::vector](https://en.cppreference.com/cpp/container/vector)
- [std::println](https://en.cppreference.com/cpp/io/basic_ostream/println)

````

## makefile

````makefile
all: test

primes: primes.cpp
	g++ -std=c++23 $< -Wall -O2 -o $@

test: primes
	./primes

clean:
	rm -f primes
````