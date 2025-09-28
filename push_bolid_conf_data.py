import zipfile
from pathlib import Path
from datetime import datetime
import subprocess

# Пути
bolid_path = Path("..\Bolid")
repo_path = Path("")
repo_path.mkdir(exist_ok=True)
zip_file = repo_path / "ConfData.zip"

print (bolid_path)
print (repo_path)
print (zip_file)

# Создание архива
with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for folder in bolid_path.iterdir():
        if folder.is_dir():
            # Список TXT файлов только из папки первого уровня
            txt_files = [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() == ".txt"]
            if txt_files:
                # Самый новый файл
                newest_file = max(txt_files, key=lambda f: f.stat().st_mtime)
                rel_path = Path(folder.name) / newest_file.name
                zipf.write(newest_file, rel_path)


# Git: добавляем архив
subprocess.run(["git", "add", "."], check=True)

# Проверка изменений
status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
if status.stdout.strip():
    # Если есть изменения — делаем коммит и пуш
    branch_name = "master"
    current_date = datetime.now().strftime("%Y-%m-%d")
    subprocess.run(["git", "commit", "-m", current_date], check=True)
    subprocess.run(["git", "push", "origin", branch_name], check=True)
    print(f"ВЫПОЛНЕНО!!!")
else:
    print("Нет изменений для коммита. Пуш не выполнен.")

input("Нажмите Enter для выхода...")