package com.advanced.numbers;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public final class NumberToolkit {
    private NumberToolkit() {}

    public static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public static long lcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return Math.abs(a / gcd(a, b) * b);
    }

    public static BigInteger factorial(int n) {
        if (n < 0) throw new IllegalArgumentException("n must be >= 0");
        BigInteger res = BigInteger.ONE;
        for (int i = 2; i <= n; i++) res = res.multiply(BigInteger.valueOf(i));
        return res;
    }

    public static List<Integer> primeSieve(int n) {
        if (n < 2) return new ArrayList<>();
        boolean[] sieve = new boolean[n + 1];
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (!sieve[i]) {
                primes.add(i);
                if ((long)i * i <= n) {
                    for (int j = i * i; j <= n; j += i) sieve[j] = true;
                }
            }
        }
        return primes;
    }
}
