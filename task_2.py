from pathlib import Path

def get_cats_info(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
                cats_info = []
                for line in file:
                    parts = (line.strip().split(','))
                    if len(parts) == 3:  
                        cat_id, name, age = parts
                        cats_info.append({"id": cat_id, "name": name, "age": age})
                    else:
                        print(f'ValueError with line: {line}')
                return cats_info
    except FileNotFoundError:
        print('File not found')
        return None   
    except Exception as e:
        print(f'{e} with file')
        return None

cats_info = get_cats_info(r"C:\Users\Patifon\OneDrive\Робочий стіл\My repo\goit-algo-hw-04\cat_information.txt")
print(cats_info)
