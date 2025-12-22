package com.calculator;

import com.calculator.core.Calculator;
import com.calculator.ui.SwingCalculator;

public class Main {
    public static void main(String[] args) {
        if (args.length == 0) {
            javax.swing.SwingUtilities.invokeLater(() -> new SwingCalculator().show());
            return;
        }
        String expr = String.join(" ", args);
        try {
            double result = Calculator.evaluate(expr);
            System.out.println(result);
        } catch (Exception e) {
            System.err.println("Erro ao avaliar expressão: " + e.getMessage());
        }
    }
}
