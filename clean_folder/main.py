from pathlib import Path
import shutil
import sys
import clean_folder.file_parser as parser
from clean_folder.normalize import normalize

def handle_images(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_audio(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_video(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path):
    # Створюємо папку для архіву
    target_folder.mkdir(exist_ok=True, parents=True)
    # Створюємо папку куди розпакуємо архів
    # Беремо суфікс у файла і удаляємо replace(filename.suffix, '')
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    # Створюємо папку для архіву з іменем файлу
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')

def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_images(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_images(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_images(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_images(file, folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_audio(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handle_audio(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handle_audio(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handle_audio(file, folder / 'audio' / 'AMR')
    for file in parser.AVI_VIDEO:
        handle_audio(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_audio(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_audio(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_audio(file, folder / 'video' / 'MKV')
    for file in parser.DOC_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'DOC')
    for file in parser.TXT_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'TXT')
    for file in parser.DOCX_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'DOCX')
    for file in parser.PDF_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        handle_audio(file, folder / 'documents' / 'PPTX')
    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    # Виконуємо реверс списку для того щоб видалити всі папки
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

def clean_folder():
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())

# if __name__ == '__main__':
#     clean_folder()
#     if sys.argv[1]:
#         folder_for_scan = Path(sys.argv[1])
#         print(f'Start in folder {folder_for_scan.resolve()}')
#         main(folder_for_scan.resolve())

# TODO: запускаємо:  python3 main.py `назва_папки_для_сортування`