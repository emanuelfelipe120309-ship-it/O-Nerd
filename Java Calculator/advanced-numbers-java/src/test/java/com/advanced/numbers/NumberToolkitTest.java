package com.advanced.numbers;

import org.junit.jupiter.api.Test;

import java.math.BigInteger;

import static org.junit.jupiter.api.Assertions.*;

public class NumberToolkitTest {
    @Test
    public void testGcdLcm() {
        assertEquals(6, NumberToolkit.gcd(54, 24));
        assertEquals(216, NumberToolkit.lcm(72, 24));
    }

    @Test
    public void testFactorial() {
        assertEquals(BigInteger.valueOf(120), NumberToolkit.factorial(5));
    }

    @Test
    public void testPrimes() {
        assertEquals(4, NumberToolkit.primeSieve(10).size());
    }
}
