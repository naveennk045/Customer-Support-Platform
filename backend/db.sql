-- Create database
CREATE DATABASE demo_app;
USE demo_app;

-- Users table for login/signup
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Twilio credentials table
CREATE TABLE twilio_credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_sid VARCHAR(255) UNIQUE NOT NULL,
    auth_token VARCHAR(255) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    enable_whatsapp BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Database credentials table
CREATE TABLE db_credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    db_type VARCHAR(50) NOT NULL,
    db_host VARCHAR(255) NOT NULL,
    db_port VARCHAR(10) NOT NULL,
    db_name VARCHAR(255) NOT NULL,
    db_username VARCHAR(255) NOT NULL,
    db_password VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Chatbot settings table
CREATE TABLE chatbot_settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chatbot_name VARCHAR(255) NOT NULL,
    chatbot_greeting TEXT NOT NULL,
    chatbot_theme VARCHAR(50) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);