# 🚀 Secure Drone Delivery System

## 📌 Overview

This project simulates a secure drone delivery system using modern cybersecurity and automation techniques.

It includes:

* AES-256 encryption for secure communication
* SHA-256 hashing for data integrity
* OTP-based authentication for delivery verification
* Real-time attack simulation (GPS spoofing, signal jamming)

The system demonstrates how AI-driven automation and security can be applied to real-world logistics and delivery systems.

---

## 🛡️ Architecture

This project implements a **three-layer security architecture** to protect the entire delivery lifecycle:

### 🔹 Layer 1: Drone Security

* AES-256 encrypted drone-to-server communication
* Encrypted telemetry (location, battery)
* Anti-spoofing protection

### 🔹 Layer 2: Delivery Channel Security

* Cryptographically secure package IDs
* SHA-256 hashed OTP storage
* Encrypted real-time position updates
* Complete audit logging

### 🔹 Layer 3: Customer Verification

* 6-digit OTP authentication
* Maximum 3 attempts before lockdown
* Tamper detection and alert system
* Secure delivery confirmation

---

## ⚙️ Features

* AES-256 (Fernet) encryption for all communications
* Secure OTP-based authentication
* Drone flight simulation with encrypted updates
* GPS spoofing detection and prevention
* Signal jamming detection with fallback handling
* Tamper detection with instant alerts
* Flask-based REST API
* CLI-based simulation environment
* Automated API testing system

---

## 📊 Results

* 100% attack prevention achieved in simulation
* <50 ms encryption latency
* ~30.6 seconds average delivery time

---

## 🚀 Quick Start

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run system

```bash
python drone_delivery_system.py
```

### Run tests

```bash
python test_api.py
```

---

## 🧪 Testing

Run the system and test API endpoints:

```bash
# Terminal 1
python drone_delivery_system.py

# Terminal 2
python test_api.py
```

All tests should pass ✅

---

## 💡 What This Project Demonstrates

* Secure system design using encryption and authentication
* Real-time attack simulation and detection
* Integration of APIs and automation workflows
* Application of AI-driven thinking to real-world problems


