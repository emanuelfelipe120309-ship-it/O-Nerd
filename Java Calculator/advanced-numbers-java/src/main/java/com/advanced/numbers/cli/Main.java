package com.advanced.numbers.cli;

import com.advanced.numbers.NumberToolkit;
import com.advanced.numbers.Statistics;
import com.advanced.numbers.Matrix;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Advanced Numbers CLI\nType 'help' for commands.");
        while (true) {
            System.out.print("> ");
            String line = sc.nextLine().trim();
            if (line.isEmpty()) continue;
            if (line.equalsIgnoreCase("exit")) break;
            if (line.equalsIgnoreCase("help")) {
                System.out.println("Commands: gcd a b | lcm a b | fact n | primes n | mean nums | var nums | matmul r c ... | exit");
                continue;
            }
            try {
                if (line.startsWith("gcd ")) {
                    String[] p = line.split(" ");
                    long a = Long.parseLong(p[1]);
                    long b = Long.parseLong(p[2]);
                    System.out.println(NumberToolkit.gcd(a, b));
                } else if (line.startsWith("lcm ")) {
                    String[] p = line.split(" ");
                    long a = Long.parseLong(p[1]);
                    long b = Long.parseLong(p[2]);
                    System.out.println(NumberToolkit.lcm(a, b));
                } else if (line.startsWith("fact ")) {
                    int n = Integer.parseInt(line.split(" ")[1]);
                    BigInteger f = NumberToolkit.factorial(n);
                    System.out.println(f.toString());
                } else if (line.startsWith("primes ")) {
                    int n = Integer.parseInt(line.split(" ")[1]);
                    System.out.println(NumberToolkit.primeSieve(n));
                } else if (line.startsWith("mean ")) {
                    List<Double> nums = Arrays.stream(line.substring(5).split(","))
                            .map(String::trim).map(Double::parseDouble).collect(Collectors.toList());
                    System.out.println(Statistics.mean(nums));
                } else if (line.startsWith("var ")) {
                    List<Double> nums = Arrays.stream(line.substring(4).split(","))
                            .map(String::trim).map(Double::parseDouble).collect(Collectors.toList());
                    System.out.println("pop=" + Statistics.variancePopulation(nums) + " sample=" + Statistics.varianceSample(nums));
                } else if (line.startsWith("matmul ")) {
                    System.out.println("Matrix multiply demo: multiplying 2x3 by 3x2");
                    double[][] a = {{1,2,3},{4,5,6}};
                    double[][] b = {{7,8},{9,10},{11,12}};
                    System.out.println(Matrix.toString(Matrix.multiply(a,b)));
                } else {
                    System.out.println("Unknown command. Type 'help'.");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
        System.out.println("Bye");
    }
}
