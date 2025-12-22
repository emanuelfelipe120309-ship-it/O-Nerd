package com.calculator.ui;

import com.calculator.core.Calculator;
import com.calculator.history.HistoryManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class SwingCalculator {
    private final JFrame frame = new JFrame("Calculadora Java");
    private final JTextField display = new JTextField();
    private final HistoryManager history = new HistoryManager(200);

    public void show() {
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(420, 500);
        frame.setLayout(new BorderLayout());

        JMenuBar menuBar = new JMenuBar();
        JMenu file = new JMenu("Arquivo");
        JMenuItem saveHist = new JMenuItem("Salvar Histórico");
        JMenuItem loadHist = new JMenuItem("Carregar Histórico");
        JMenuItem exit = new JMenuItem("Sair");
        file.add(saveHist);
        file.add(loadHist);
        file.addSeparator();
        file.add(exit);
        menuBar.add(file);
        frame.setJMenuBar(menuBar);

        saveHist.addActionListener(e -> {
            try {
                history.saveToFile(HistoryManager.defaultHistoryPath());
                JOptionPane.showMessageDialog(frame, "Histórico salvo em: " + HistoryManager.defaultHistoryPath());
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(frame, "Erro ao salvar: " + ex.getMessage());
            }
        });
        loadHist.addActionListener(e -> {
            try {
                history.loadFromFile(HistoryManager.defaultHistoryPath());
                JOptionPane.showMessageDialog(frame, "Histórico carregado (" + history.all().size() + " entradas)");
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(frame, "Erro ao carregar: " + ex.getMessage());
            }
        });
        exit.addActionListener(e -> frame.dispose());

        display.setFont(new Font(Font.MONOSPACED, Font.PLAIN, 20));
        display.setHorizontalAlignment(JTextField.RIGHT);
        frame.add(display, BorderLayout.NORTH);

        display.addActionListener(e -> evalAndShow());
        display.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) evalAndShow();
            }
        });

        JPanel buttons = new JPanel(new GridLayout(6, 4, 4, 4));
        String[] labels = {
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+",
            "(",")","^","!",
            "sin","cos","tan","CLR",
            "CE","<-","pi","e"
        };
        for (String l : labels) buttons.add(button(l));

        frame.add(buttons, BorderLayout.CENTER);

        JPanel bottom = new JPanel(new BorderLayout());
        JButton histBtn = new JButton("Hist");
        histBtn.addActionListener(e -> showHistory());
        bottom.add(histBtn, BorderLayout.WEST);
        frame.add(bottom, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private void showHistory() {
        java.util.List<String> all = history.all();
        if (all.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Histórico vazio.");
            return;
        }
        StringBuilder sb = new StringBuilder();
        for (String h : all) sb.append(h).append("\n");
        JOptionPane.showMessageDialog(frame, sb.toString(), "Histórico", JOptionPane.PLAIN_MESSAGE);
    }

    private JButton button(String label) {
        JButton b = new JButton(label);
        b.addActionListener((ActionEvent e) -> onPress(label));
        return b;
    }

    private void onPress(String label) {
        switch (label) {
            case "=":
                evalAndShow();
                break;
            case "CLR":
                display.setText("");
                break;
            case "CE":
                display.setText("");
                break;
            case "<-":
                String t = display.getText();
                if (!t.isEmpty()) display.setText(t.substring(0, t.length()-1));
                break;
            case "sin", "cos", "tan":
                display.setText(display.getText() + label + "(");
                break;
            case "pi":
                display.setText(display.getText() + "pi");
                break;
            case "e":
                display.setText(display.getText() + "e");
                break;
            default:
                display.setText(display.getText() + label);
        }
    }

    private void evalAndShow() {
        String expr = display.getText();
        try {
            double r = Calculator.evaluate(expr);
            String out = expr + " = " + r;
            history.add(out);
            display.setText(Double.toString(r));
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(frame, "Erro: " + ex.getMessage());
        }
    }
}
