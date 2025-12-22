package com.advanced.numbers;

import java.util.DoubleSummaryStatistics;
import java.util.List;

public final class Statistics {
    private Statistics() {}

    public static double mean(List<? extends Number> nums) {
        return nums.stream().mapToDouble(Number::doubleValue).average().orElse(Double.NaN);
    }

    public static double variancePopulation(List<? extends Number> nums) {
        double mean = mean(nums);
        return nums.stream().mapToDouble(Number::doubleValue)
                .map(d -> (d - mean) * (d - mean)).average().orElse(Double.NaN);
    }

    public static double varianceSample(List<? extends Number> nums) {
        int n = nums.size();
        if (n < 2) return Double.NaN;
        double mean = mean(nums);
        return nums.stream().mapToDouble(Number::doubleValue)
                .map(d -> (d - mean) * (d - mean)).sum() / (n - 1);
    }

    public static DoubleSummaryStatistics summary(List<? extends Number> nums) {
        return nums.stream().mapToDouble(Number::doubleValue).collect(DoubleSummaryStatistics::new,
                DoubleSummaryStatistics::accept, DoubleSummaryStatistics::combine);
    }
}
