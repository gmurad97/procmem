import psutil


class ProcMem:
    def __init__(self, read, write, nop):
        pass

    def __str__():
        return "New Object ProcMem"

    def __repr__(self):
        return "class name repr"

    def get_process(self, *, process_name=None, process_id=None):
        processes = tuple(process for process in psutil.process_iter(["name"]))

    # def get_processes_name(self):
    #     return tuple(
    #         process.info["name"] for process in psutil.process_iter(["name"])
    #     )

    # def get_processes_pid(self):
    #     return tuple(
    #         process.info["pid"] for process in psutil.process_iter(["pid"])
    #     )


def main():
    proc = ProcMem()
    print(proc.get_processes_pid())


if __name__ == "__main__":
    main()


# import ctypes
# import ctypes.wintypes
# import psutil

# # Константы доступа
# PROCESS_ALL_ACCESS = 0x1F0FFF

# # Адрес, с которого нужно читать
# address = 0x16B8FB90
# buffer_size = 4  # Размер данных, которые нужно прочитать (например, 4 байта)

# def get_process_id_by_name(process_name):
#     for process in psutil.process_iter(attrs=['pid', 'name']):
#         if process.info['name'].lower() == process_name.lower():
#             print(f"Процесс найден: {process_name} с PID {process.info['pid']}")
#             return process.info['pid']
#     print(f"Процесс {process_name} не найден.")
#     return None

# # Функция для чтения памяти
# def read_process_memory(process_name, address, size):
#     pid = get_process_id_by_name(process_name)
#     if not pid:
#         return None

#     # Открываем процесс
#     process_handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
#     if not process_handle:
#         print("Не удалось открыть процесс. Убедитесь, что вы запускаете скрипт от имени администратора.")
#         return None

#     # Буфер для хранения данных
#     buffer = ctypes.create_string_buffer(size)
#     bytesRead = ctypes.c_size_t()

#     # Чтение памяти
#     if ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, size, ctypes.byref(bytesRead)):
#         ctypes.windll.kernel32.CloseHandle(process_handle)
#         return buffer.raw
#     else:
#         print("Ошибка при чтении памяти.")
#         ctypes.windll.kernel32.CloseHandle(process_handle)
#         return None

# # Используем функцию
# data = read_process_memory("popcapgame1.exe", address, buffer_size)
# if data:
#     # Преобразование байтов в число
#     number = int.from_bytes(data, byteorder='little')  # Измените на 'big' при необходимости
#     print(f"Прочитанные данные (байты): {data}")
#     print(f"Прочитанные данные (число): {number}")
# else:
#     print("Не удалось получить данные из памяти.")
