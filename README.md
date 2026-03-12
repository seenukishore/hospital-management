# 🏥 Hospital Management System

## 📌 About
A Python + MySQL based Hospital Management System that securely manages patients, appointments, and billing with encrypted database credentials.

## 🛠️ Technologies Used
- Python 3
- MySQL Connector
- Cryptography (Fernet)

## 📁 Project Structure
| File | Description |
|------|-------------|
| `main.py` | Main menu & entry point |
| `patients.py` | Patient registration & view |
| `appointments.py` | Book & view appointments |
| `billing.py` | Add & view bills |
| `db_config.py` | MySQL connection setup |
| `password_utils.py` | Encrypted password handler |
| `.gitignore` | Hides secret.key from GitHub |

## ⚙️ Features
- ✅ Patient Registration
- ✅ Appointment Booking
- ✅ Billing System
- ✅ Secure Encrypted Password

## 🔒 Security
- `secret.key` is never uploaded to GitHub
- Password is encrypted using Fernet encryption
- Password is always masked when printed

## ▶️ How to Run
1. Clone the repository
2. Install dependencies: `pip install mysql-connector-python cryptography`
3. Run `encrypt_once.py` to generate key & encrypted password
4. Update encrypted password in `password_utils.py`
5. Run `main.py`