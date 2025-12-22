package com.calculator.core;

import java.util.*;

public class Calculator {
    public static double evaluate(String expr) {
        List<String> tokens = tokenize(expr);
        List<String> rpn = toRPN(tokens);
        return evalRPN(rpn);
    }

    private static List<String> tokenize(String s) {
        List<String> out = new ArrayList<>();
        s = s.replaceAll("\\s+", "");
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (Character.isDigit(c) || c == '.') {
                int j = i + 1;
                while (j < s.length() && (Character.isDigit(s.charAt(j)) || s.charAt(j) == '.')) j++;
                out.add(s.substring(i, j));
                i = j;
            } else if (Character.isLetter(c)) {
                int j = i + 1;
                while (j < s.length() && Character.isLetter(s.charAt(j))) j++;
                String name = s.substring(i, j).toLowerCase();
                if ("pi".equals(name)) {
                    out.add(Double.toString(Math.PI));
                } else if ("e".equals(name)) {
                    out.add(Double.toString(Math.E));
                } else {
                    out.add(name);
                }
                i = j;
            } else {
                if (c == '-' ) {
                    // determine unary
                    if (out.isEmpty() || isOperator(out.get(out.size() - 1)) || "(".equals(out.get(out.size() - 1))) {
                        out.add("u-");
                        i++;
                        continue;
                    }
                }
                out.add(String.valueOf(c));
                i++;
            }
        }
        return out;
    }

    private static boolean isOperator(String t) {
        return "+".equals(t) || "-".equals(t) || "*".equals(t) || "/".equals(t) || "^".equals(t) || "u-".equals(t) || "!".equals(t);
    }

    private static int prec(String op) {
        return switch (op) {
            case "u-" -> 5;
            case "!" -> 5;
            case "^" -> 4;
            case "*", "/" -> 3;
            case "+", "-" -> 2;
            default -> 0;
        };
    }

    private static boolean rightAssoc(String op) {
        return "^".equals(op) || "u-".equals(op);
    }

    private static List<String> toRPN(List<String> tokens) {
        List<String> output = new ArrayList<>();
        Deque<String> stack = new ArrayDeque<>();
        for (String t : tokens) {
            if (isNumber(t)) {
                output.add(t);
            } else if (isFunction(t)) {
                stack.push(t);
            } else if (isOperator(t)) {
                while (!stack.isEmpty() && (isOperator(stack.peek()) || isFunction(stack.peek()))) {
                    String top = stack.peek();
                    if ((isOperator(top) && ((prec(top) > prec(t)) || (prec(top) == prec(t) && !rightAssoc(t))))) {
                        output.add(stack.pop());
                    } else break;
                }
                stack.push(t);
            } else if ("(".equals(t)) {
                stack.push(t);
            } else if (")".equals(t)) {
                while (!stack.isEmpty() && !"(".equals(stack.peek())) output.add(stack.pop());
                if (stack.isEmpty()) throw new IllegalArgumentException("Mismatched parentheses");
                stack.pop();
                if (!stack.isEmpty() && isFunction(stack.peek())) output.add(stack.pop());
            } else {
                throw new IllegalArgumentException("Token desconhecido: " + t);
            }
        }
        while (!stack.isEmpty()) {
            String s = stack.pop();
            if ("(".equals(s) || ")".equals(s)) throw new IllegalArgumentException("Mismatched parentheses");
            output.add(s);
        }
        return output;
    }

    private static boolean isNumber(String s) {
        if (s == null) return false;
        try {
            Double.parseDouble(s);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private static boolean isFunction(String s) {
        if (s == null) return false;
        switch (s) {
            case "sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log", "ln", "abs", "sinh", "cosh", "tanh", "ceil", "floor":
                return true;
            default:
                return false;
        }
    }

    private static double evalRPN(List<String> rpn) {
        Deque<Double> stack = new ArrayDeque<>();
        for (String t : rpn) {
            if (isNumber(t)) {
                stack.push(Double.parseDouble(t));
            } else if (isFunction(t)) {
                if (stack.isEmpty()) throw new IllegalArgumentException("Operando faltando para função " + t);
                double v = stack.pop();
                stack.push(applyFunction(t, v));
            } else if (isOperator(t)) {
                if ("u-".equals(t)) {
                    if (stack.isEmpty()) throw new IllegalArgumentException("Operando faltando para unário-");
                    stack.push(-stack.pop());
                } else if ("!".equals(t)) {
                    if (stack.isEmpty()) throw new IllegalArgumentException("Operando faltando para !");
                    double v = stack.pop();
                    stack.push((double) factorial((long) v));
                } else {
                    if (stack.size() < 2) throw new IllegalArgumentException("Operandos insuficientes para operador " + t);
                    double b = stack.pop();
                    double a = stack.pop();
                    stack.push(applyOp(t, a, b));
                }
            } else {
                throw new IllegalArgumentException("Token RPN desconhecido: " + t);
            }
        }
        if (stack.size() != 1) throw new IllegalArgumentException("Expressão inválida");
        return stack.pop();
    }

    private static double applyOp(String op, double a, double b) {
        return switch (op) {
            case "+" -> a + b;
            case "-" -> a - b;
            case "*" -> a * b;
            case "/" -> a / b;
            case "^" -> Math.pow(a, b);
            default -> throw new IllegalArgumentException("Operador desconhecido: " + op);
        };
    }

    private static double applyFunction(String f, double v) {
        return switch (f) {
            case "sin" -> Math.sin(v);
            case "cos" -> Math.cos(v);
            case "tan" -> Math.tan(v);
            case "asin" -> Math.asin(v);
            case "acos" -> Math.acos(v);
            case "atan" -> Math.atan(v);
            case "sinh" -> Math.sinh(v);
            case "cosh" -> Math.cosh(v);
            case "tanh" -> Math.tanh(v);
            case "sqrt" -> Math.sqrt(v);
            case "log" -> Math.log10(v);
            case "ln" -> Math.log(v);
            case "abs" -> Math.abs(v);
            case "ceil" -> Math.ceil(v);
            case "floor" -> Math.floor(v);
            default -> throw new IllegalArgumentException("Função desconhecida: " + f);
        };
    }

    private static long factorial(long n) {
        if (n < 0) throw new IllegalArgumentException("Fatorial de número negativo");
        long r = 1;
        for (long i = 2; i <= n; i++) r *= i;
        return r;
    }
}
