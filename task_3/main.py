import sys
import re
import collections


#Создание списка с именами ключей для дольнейшего использования 
KEY_LIST = ["date", "time", "level", "massage"]


#Парсинг строк, содержащих логи
def parse_log_line(line: str) -> dict:
    #Создание паттерна для раздиления всех логов на элементы для словаря
    pattern = r"(\d{4}\-\d{2}\-\d{2})\s(\d{2}\:\d{2}\:\d{2})\s(\w*)\s(.*)"
    #Раздиление строки
    match = re.search(pattern, line)
    if match:
        #Создание словаря где ключ это элемент списка KEY_LIST а значение это элемент объекта Match
        result = {key: match.group(value) for key, value in zip(KEY_LIST,range(1,5))}
        return result
    else:
        return None

#Загрузка логов из файла 
def load_logs(file_path: str) -> list:
    #Открытие файла для чтения из него логов
    with open(file_path, 'r') as fh:
        #Создание списка словарей, где будут сохраняться логи
        lines = [parse_log_line(line) for line in fh.readlines()]
        fh.close()
        return lines


#Фильтр всех логов в файле для поиска всех логов с одним уромнем
def filter_logs_by_level(logs: list, level: str) -> list:
    #Создание списка состоящего из наеденых в списке логов, которые соответствуют необходимому уровню
    return list(filter(lambda info_dict: info_dict['level'] == level.upper(), logs))


#Подсчет логов с определенным уровнем
def count_logs_by_level(logs: list) -> dict:
    #Создание словаря в котором ключ это уровень, а значение это количество посторений этого уровня в списке всех логов с помощью класса Counter
    return dict(collections.Counter(log['level'] for log in logs))

#Вывод результатов подсчета логов с определенным уровнем 
def display_log_counts(counts: dict):
    #Создание списка ключей
    keys_of_logs = list(counts.keys())
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    #вывод всех уровней логов и количества этих уровней
    for level in keys_of_logs:
        print(level, " "*(15 - len(level)),"|", counts[level])


def main():
    try:
        path = sys.argv[1]
        list_of_logs = load_logs(path)
        if not list_of_logs:
            print("There are no logs in the file.")
        else:
            display_log_counts(count_logs_by_level(list_of_logs))
            if len(sys.argv) == 3:
                print(f"\nДеталі логів для рівня {sys.argv[2].upper()}:")
                for log in filter_logs_by_level(list_of_logs, sys.argv[2]):
                    print(f"{log["date"]} {log['time']} - {log['massage']}")
    except IndexError:
        #Если пользователь не укозал путь к файлу то программа выведет:"Please write path to log file as argument"
        print("Please write path to log file as argument")
    except FileNotFoundError:
        # Если файл не найден  то программа выводит "The file is corrupted or cannot be read"
        print("File not found")
    except UnicodeDecodeError:
        # Если файл поврежден то программа  выводит "The file is corrupted or cannot be read"
        print("The file is corrupted or cannot be read")



if __name__ == "__main__":
    main()