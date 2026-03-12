import mysql.connector
from password_utils import get_decrypted_password

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="hospital"
    )
    return conn