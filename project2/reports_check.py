import os


def reports():
    folder_path = "data/decrypted_reports"
    if not os.path.exists(folder_path):
        print(f"Папка {folder_path} не существует")
        return
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                prefix = content.lower().replace("вра", "дру")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(prefix)
                    file.write("\nПроверено!")
            except Exception as e:
                print(f"Возникла ошибка при модификации файла {file_name}: {e}")
        else:
            print(f"{file_name} является папкой")
