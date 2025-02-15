from pathlib import Path

def total_salary(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            salaries = []
            for line in lines:
                try:
                    salaries.append(int(line.strip().split(',')[1]))
                except ValueError:
                    print(f'ValueError with line: {line}')
                    continue

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print('File not found')
        return 0, 0

    except Exception as e:
        print(f'{e} with file')
        return 0, 0

total, average = total_salary(r'C:\Users\Patifon\OneDrive\Робочий стіл\My repo\goit-algo-hw-04\salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

