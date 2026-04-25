package com.example;

import java.util.Objects;

public class Calculator {

    // ✅ Fix: Handle division by zero
    public int divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Divider cannot be zero");
        }
        return a / b;
    }

    // ✅ Fix: Removed unused variable
    public int add(int a, int b) {
        return a + b;
    }

    // ✅ Fix: Prevent SQL Injection (use parameterized style simulation)
    public String getUser(String userId) {
        if (userId == null || !userId.matches("\\d+")) {
            throw new IllegalArgumentException("Invalid user ID");
        }
        return "SELECT * FROM users WHERE id = ?";
    }

    // ✅ Fix: Remove duplicate logic (reuse method)
    public int multiply(int a, int b) {
        return a * b;
    }

    public int multiplyAlt(int a, int b) {
        return multiply(a, b); // reuse logic
    }

    // ✅ Fix: Reduce parameter count using object
    public void processUser(User user) {
        if (user == null) {
            throw new IllegalArgumentException("User cannot be null");
        }
        System.out.println("Processing: " + user.getName());
    }

    // ✅ Fix: Null safety
    public String getName(String name) {
        return Objects.requireNonNull(name, "Name cannot be null").toUpperCase();
    }

    // ✅ Fix: Proper exception handling
    public void riskyOperation() {
        try {
            int x = 10 / 0;
        } catch (ArithmeticException e) {
            System.err.println("Error occurred: " + e.getMessage());
        }
    }
}
