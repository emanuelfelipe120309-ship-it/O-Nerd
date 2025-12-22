package com.calculator.history;

import java.util.*;
import java.io.*;
import java.nio.file.*;

public class HistoryManager {
    private final Deque<String> history = new ArrayDeque<>();
    private final int capacity;

    public HistoryManager() { this(100); }
    public HistoryManager(int capacity) { this.capacity = capacity; }

    public void add(String entry) {
        history.addFirst(entry);
        while (history.size() > capacity) history.removeLast();
    }

    public List<String> all() { return new ArrayList<>(history); }

    public Optional<String> last() { return Optional.ofNullable(history.peekFirst()); }

    public void saveToFile(Path path) throws IOException {
        Files.createDirectories(path.getParent());
        try (BufferedWriter w = Files.newBufferedWriter(path)) {
            for (String s : history) w.write(s + "\n");
        }
    }

    public void loadFromFile(Path path) throws IOException {
        if (!Files.exists(path)) return;
        List<String> lines = Files.readAllLines(path);
        history.clear();
        for (int i = lines.size()-1; i >= 0; i--) { // add in reverse to keep newest first
            String l = lines.get(i);
            if (!l.isBlank()) history.addFirst(l);
        }
    }

    public static Path defaultHistoryPath() {
        String home = System.getProperty("user.home");
        return Paths.get(home, ".java-calculator", "history.txt");
    }
}
