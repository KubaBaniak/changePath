import os
import platform

file_path = '/home/kuba/change_path_dir/test.py'
# Tu podaj scieżkę '/home/kuba/change_path_dir/testowo

def prepare_path_linux(path):
    elements = [element for element in file_path.split('/') if element]
    print(elements)
    username_windows = input('Input your linux username account')
    elements[0] = 'home'
    elements[1] = username_windows
    path = f'{os.sep}{os.sep.join(elements)}'
    print(path)
    return path

def prepare_path_windows(path):
    elements = [element for element in file_path.split('/') if element]
    username_windows = input('Input your windows username account: ')
    elements[0] = 'Users'
    elements[1] = username_windows
    start_path = os.sep.join([elements[0], elements[1]])
    current_dir = f'C:{os.sep}{start_path}'

    for x in elements[2:]:
        if x in os.listdir(current_dir):
            current_dir = os.path.join(current_dir, x)
        else:
            if '.' in x:
                with open(current_dir + os.sep + elements[-1], 'w') as f:
                    pass
            else:
                current_dir = os.path.join(current_dir, x)
                os.mkdir(current_dir)

    path = current_dir
    return path

system = platform.system()
if system == 'Linux':
    path = prepare_path_linux(file_path)
elif system == 'Windows':
    path = prepare_path_windows(file_path)

print('Jeżeli do tej pory działa, to zobaczysz poniżej ścieżkę :)')
print(path)

print('Użyj ścieżki aby sprawdzić czy zadziała.')

#Przykłady użycia ścieżki pliku w programie (nie o wszystkich mówiliśmy, jak czegoś nie #rozumiecie to nie przejmujcie się tym :) wybierzcie tą którą rozumiecie, ew. #poczytajcie więcej w dokumentacji - starczy 1):
#os.remove()
#os.system(polecenie_ze_sciezka)
#open().read()
#subprocess.Popen()
#sys.path
#pd.read_csv(path)
# etc.
