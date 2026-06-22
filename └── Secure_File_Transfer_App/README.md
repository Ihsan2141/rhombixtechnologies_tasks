# Secure File Transfer Application

## Project Overview

This project was developed as part of the Rhombix Technologies Cyber Security Internship.

The objective of this project is to implement a secure file transfer system that ensures confidentiality, integrity, and secure communication between a client and a server using encryption techniques.

---

## Objectives

* Develop a secure file transfer application.
* Implement file encryption before transmission.
* Ensure confidentiality of transferred data.
* Verify file integrity using SHA-256 hashing.
* Maintain audit logs of file transfer activities.

---

## Features

* End-to-End Encryption using Fernet (Cryptography Library)
* Secure Client-Server Communication
* SHA-256 Integrity Verification
* Audit Logging
* Encrypted File Storage
* Sample File Transfer Demonstration

---

## Technologies Used

* Python 3
* Cryptography Library (Fernet)
* Socket Programming
* SHA-256 Hashing
* Kali Linux

---

## Project Structure

```text
Secure_File_Transfer_App/
│
├── README.md
├── requirements.txt
├── client.py
├── server.py
├── crypto_utils.py
├── received_file.enc
│
├── Logs/
│   └── transfer_log.txt
│
├── SampleFiles/
│   └── testfile.txt
│
└── Screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-link>
cd Secure_File_Transfer_App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execution Steps

### Start Server

```bash
python server.py
```

### Run Client

Open another terminal:

```bash
python client.py
```

---

## Security Mechanisms

### Confidentiality

Files are encrypted using Fernet symmetric encryption before transmission.

### Integrity

SHA-256 hashing is used to verify data integrity and detect unauthorized modifications.

### Audit Logging

All file transfer activities are recorded in:

```text
Logs/transfer_log.txt
```

---

## Results

* Secure encrypted file transfer achieved.
* SHA-256 integrity verification implemented.
* Audit logs generated successfully.
* Encrypted file received and stored securely.

---

## Screenshots

* Server Running
* Client Connection
* Integrity Verification
* Encrypted File Transfer
* Audit Logs
* Project Structure

---

## Conclusion

This project successfully demonstrates a Secure File Transfer Application that provides confidentiality, integrity verification, and audit logging. The implementation follows basic cybersecurity principles and satisfies the requirements of the Rhombix Technologies Cyber Security Internship.

---

## Author

Ihsanullah

Rhombix Technologies Cyber Security Internship
