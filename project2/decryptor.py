import os
from cryptography.fernet import Fernet as Fn


def decrypt():
    folder_path = "data/spy_reports"
    folder_decrypted = "data/decrypted_reports"
    if not os.path.exists(folder_decrypted):
        os.makedirs(folder_decrypted)
    with open("data/spy.key", "rb") as key_file:
        key = key_file.read()
    fernet_key = Fn(key)
    days = [f"{i:02d}_10_2023" for i in range(1, 32)]
    for day in days:
        files_with_date = [filename for filename in os.listdir(folder_path) if day in filename]
        if files_with_date:
            print(f"Для {day} найден отчет:")
            for filename in files_with_date:
                source_file_path = os.path.join(folder_path, filename)
                folder_decrypted_file_path = os.path.join(folder_decrypted, filename)
                try:
                    with open(source_file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()
                        decrypted_data = fernet_key.decrypt(encrypted_data)
                    with open(folder_decrypted_file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)

                    print(f"{filename} расшифрован и сохранен как {folder_decrypted_file_path}")
                except Exception as e:
                    print(f"Возникла ошибка при дешифровке файла {filename}: {e}")
        else:
            print(f"Для {day} нет отчета")
