package com.calculator;

import com.calculator.core.Calculator;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {
    @Test
    public void basicArithmetic() {
        assertEquals(7.0, Calculator.evaluate("1+2*3"), 1e-9);
        assertEquals(9.0, Calculator.evaluate("(1+2)*3"), 1e-9);
    }

    @Test
    public void functionsAndPow() {
        assertEquals(9.0, Calculator.evaluate("3^2"), 1e-9);
        assertEquals(Math.sin(1.0), Calculator.evaluate("sin(1)"), 1e-9);
    }

    @Test
    public void factorialAndUnary() {
        assertEquals(6.0, Calculator.evaluate("3!"), 1e-9);
        assertEquals(-5.0, Calculator.evaluate("-5"), 1e-9);
        assertEquals(5.0, Calculator.evaluate("- -5"), 1e-9);
    }
}
