-- Create database
CREATE DATABASE IF NOT EXISTS student_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE student_database;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert default admin with hashed password
INSERT INTO users (username, password) VALUES
('admin', 'pbkdf2:sha256:260000$YJyp6yPkKQ9I85kY$ec7f1c0a0e5b91b8ff0b364b0d7350c9392e0d2c1440dbda84ad0d06190e1c3b');

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100)
);
