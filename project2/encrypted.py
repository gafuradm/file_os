import os
from cryptography.fernet import Fernet as Fn


def encrypt():
    folder_path = "data/decrypted_reports"
    encrypted_folder_path = "data/encrypted_reports"
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не существует")
        return
    if not os.path.exists(encrypted_folder_path):
        os.makedirs(encrypted_folder_path)
    files = os.listdir(folder_path)
    key = Fn.generate_key()
    fernet_key = Fn(key)
    for file_name in files:
        if "c" not in file_name.lower():
            source_file_path = os.path.join(folder_path, file_name)
            try:
                with open(source_file_path, "rb") as file:
                    data = file.read()
                encrypted_data = fernet_key.encrypt(data)
                encrypted_file_path = os.path.join(encrypted_folder_path, file_name)
                with open(encrypted_file_path, "wb") as file:
                    file.write(encrypted_data)
            except Exception as e:
                print(f"Возникла ошибка при шифровании файла {file_name}: {e}")
        else:
            print(f"Файл {file_name} содержит букву c")
