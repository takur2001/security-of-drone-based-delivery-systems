## 🚀 Overview
This project simulates a secure drone delivery system using modern cybersecurity and automation techniques.

It includes:
- AES-256 encryption for secure communication
- SHA-256 hashing for data integrity
- OTP-based authentication for delivery verification
- Real-time attack simulation (GPS spoofing, signal jamming)

The system demonstrates how AI-driven automation and security can be applied to real-world logistics and delivery systems.

# Secure Drone Delivery System

**Team**: Takur Sai Karthik & Satya Sai Kumar  
**Course**: MCS 7033


# Secure Drone Delivery System
A multi-layer security framework designed to protect drone-based delivery systems from attacks such as GPS spoofing, signal jamming, package theft, and unauthorized access.  
This project was developed as part of **MCS 7033 – Collaborative Research Project 2**.

---

## 🛡 Project Overview
Modern drone delivery systems are vulnerable to cyber and physical attacks.  
This project implements a **three-layer security architecture** to secure the entire delivery lifecycle:

### **Layer 1: Drone Security**
- AES-256 encrypted drone-to-server communication  
- Encrypted telemetry (lat/lon/battery)
- Anti-spoofing protection

### **Layer 2: Delivery Channel Security**
- Unique cryptographically secure Package IDs  
- SHA-256 hashed OTP storage  
- Real-time encrypted position updates  
- Complete audit logs for all events  

### **Layer 3: Customer Verification**
- 6-digit OTP authentication  
- Maximum 3 attempts before lockdown  
- Tamper detection and alerting  
- Secure delivery confirmation  

---

## 🚀 Features
- AES-256 (Fernet) encryption for all messages  
- Cryptographically secure OTP generation  
- Drone flight simulation with encrypted updates  
- GPS spoofing simulation and detection  
- Signal jamming detection and fallback  
- Tamper detection with instant alerts  
- Flask REST API with multiple endpoints  
- Full CLI simulation for testing  
- Automated API-based testing suite 

## Quick Start
```bash
# Install
pip install -r requirements.txt

 

# Test
python drone_delivery_system.py test

# Run Server
python drone_delivery_system.py
```

## What It Does

✅ AES-256 encryption  
✅ OTP authentication  
✅ Tamper detection  
✅ GPS spoofing prevention  
✅ 100% attack prevention rate  

## Testing
```bash
# Terminal 1
python drone_delivery_system.py

# Terminal 2
python test_api.py
```

All tests should pass ✅
