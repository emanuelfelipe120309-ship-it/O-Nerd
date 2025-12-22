package com.advanced.numbers;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

public class StatisticsTest {
    @Test
    public void testMeanVariance() {
        var nums = Arrays.asList(1.0, 2.0, 3.0, 4.0);
        assertEquals(2.5, Statistics.mean(nums), 1e-9);
        assertEquals(1.25, Statistics.variancePopulation(nums), 1e-9);
    }
}
