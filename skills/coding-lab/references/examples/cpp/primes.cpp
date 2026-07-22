#include <print>
#include <vector>
#include <cassert>

/**
 * Checks if a number is prime.
 * 
 * @param n The number to check.
 * @return True if prime, false otherwise.
 */
bool is_prime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

/**
 * Generates the first N prime numbers.
 * 
 * @param n The count of prime numbers to generate.
 * @return A vector containing the first N prime numbers.
 */
std::vector<int> get_primes(int n) {
    std::vector<int> primes;
    int num = 2;
    while (primes.size() < static_cast<size_t>(n)) {
        if (is_prime(num)) {
            primes.push_back(num);
        }
        num++;
    }
    return primes;
}

void run_tests() {
    // Test is_prime
    assert(is_prime(2) == true);
    assert(is_prime(3) == true);
    assert(is_prime(4) == false);
    assert(is_prime(5) == true);
    assert(is_prime(9) == false);
    assert(is_prime(11) == true);
    assert(is_prime(13) == true);
    assert(is_prime(15) == false);
    assert(is_prime(17) == true);
    assert(is_prime(19) == true);

    // Test get_primes
    std::vector<int> primes = get_primes(5);
    assert(primes.size() == 5);
    assert(primes[0] == 2);
    assert(primes[1] == 3);
    assert(primes[2] == 5);
    assert(primes[3] == 7);
    assert(primes[4] == 11);

    std::println("All tests passed!");
}

int main() {
    run_tests();

    std::println("First 100 primes:");
    std::vector<int> primes = get_primes(100);
    for (size_t i = 0; i < primes.size(); ++i) {
        std::println("{}", primes[i]);
        if ((i + 1) % 10 == 0) std::println("");
    }

    return 0;
}
