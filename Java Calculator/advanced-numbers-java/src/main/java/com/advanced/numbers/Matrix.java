package com.advanced.numbers;

import java.util.Arrays;

public final class Matrix {
    private Matrix() {}

    public static double[][] multiply(double[][] a, double[][] b) {
        int n = a.length;
        int m = b[0].length;
        int p = a[0].length;
        if (p != b.length) throw new IllegalArgumentException("Incompatible dimensions");
        double[][] res = new double[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                double s = 0;
                for (int k = 0; k < p; k++) s += a[i][k] * b[k][j];
                res[i][j] = s;
            }
        }
        return res;
    }

    public static double[][] transpose(double[][] a) {
        int n = a.length;
        int m = a[0].length;
        double[][] t = new double[m][n];
        for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) t[j][i] = a[i][j];
        return t;
    }

    public static String toString(double[][] a) {
        StringBuilder sb = new StringBuilder();
        for (double[] row : a) sb.append(Arrays.toString(row)).append('\n');
        return sb.toString();
    }
}
