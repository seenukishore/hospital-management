from cryptography.fernet import Fernet

class fakestr(str):
    def __str__(self):
        return "***********"
    def __repr__(self):
        return "***********"

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return fakestr(decrypted)

def get_decrypted_password():
    encrypted_password = b'gAAAAABpskitlexDXr_bxMPC8q7sU-AJuk1nBj8ut0WhyPHG0OIMlOi7069b0xCXXxFknghb-L6gT6v3TYB9_8h4RKBo4GkUiw=='
    return decrypt_password(encrypted_password)

if __name__ == "__main__":
    pwd = get_decrypted_password()
    print(f"Actual password: {str.__str__(pwd)}")