# 🏥 Hospital Management System

## 📌 About
A Python + MySQL based Hospital Management System that securely manages patients, appointments, and billing with encrypted database credentials. Supports both Terminal and GUI versions.

## 🛠️ Technologies Used
- Python 3
- MySQL Connector
- Cryptography (Fernet)
- Tkinter (GUI)

## 📁 Project Structure
| File | Description |
|------|-------------|
| `main.py` | Terminal version entry point |
| `main_gui.py` | GUI version entry point |
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
- ✅ Terminal Version
- ✅ GUI Version (Tkinter)

## 🔒 Security
- `secret.key` is never uploaded to GitHub
- Password is encrypted using Fernet encryption
- Password is always masked when printed

## ▶️ How to Run
1. Clone the repository
2. Install dependencies:
```
   pip install mysql-connector-python cryptography
```
3. Run `encrypt_once.py` to generate key & encrypted password
4. Update encrypted password in `password_utils.py`
5. Terminal version: `python main.py`
6. GUI version: `python main_gui.py`