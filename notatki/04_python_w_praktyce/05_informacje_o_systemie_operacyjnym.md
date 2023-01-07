### Informacje o systemie operacyjnym
Moduł `os` w bibliotece standardowej umożliwia uzyskiwanie informacji o systemie operacyjnym oraz manipulowanie plikami i folderami.

Przykładowo, możemy uzyskać nazwę aktualnie używanego systemu operacyjnego za pomocą `os.name`:

```python
import os
print(os.name)
```

#### Informacje o użytkownikach
Aby uzyskać informacje o użytkownikach systemu oraz grupach, możemy skorzystać z modułu `pwd`:

```python
import pwd

# Pobierz informacje o użytkowniku
user_info = pwd.getpwuid(os.getuid())
print(f"Nazwa użytkownika: {user_info.pw_name}")
print(f" ID użytkownika: {user_info.pw_uid}")
print(f" ID grupy: {user_info.pw_gid}")
print(f" Katalog domowy: {user_info.pw_dir}")

# Pobierz informacje o grupie
group_info = pwd.getgrgid(user_info.pw_gid)
print(f" Nazwa grupy: {group_info.gr_name}")
print(f" ID grupy: {group_info.gr_gid}")
print(f" Lista użytkowników w grupie: {group_info.gr_mem}")
```

#### Dyski
Aby uzyskać informacje o dostępnych dyskach oraz wolnym miejscu na nich, możemy skorzystać z modułu `os.statvfs`:

```python
import os

# Pobierz informacje o dysku
disk_info = os.statvfs("/")
print(f" Całkowita pojemność dysku: {disk_info.f_frsize * disk_info.f_blocks:,} bajtów")
print(f" Wolne miejsce na dysku: {disk_info.f_frsize * disk_info.f_bfree:,} bajtów")
```

#### Informacje o procesorze
Moduł <code>os</code> z biblioteki standardowej zawiera funkcję <code>cpu_count()</code>, która zwraca liczbę rdzeni procesora. Możemy również uzyskać informacje o mocy obliczeniowej procesora za pomocą modułu <code>psutil</code>. Poniższy przykład pokazuje, jak wyświetlić liczbę rdzeni oraz moc obliczeniową procesora:

```python
import os
import psutil

# Liczba rdzeni procesora
print(f"Liczba rdzeni procesora: {os.cpu_count()}")

# Moc obliczeniowa procesora
print(f"Moc obliczeniowa procesora: {psutil.cpu_freq().max} MHz")
```

#### Zmienne środowiskowe
Moduł <code>os</code> zawiera również funkcję <code>environ</code>, która zwraca słownik zawierający wszystkie zmienne środowiskowe. Możemy odczytać wartość konkretnej zmiennej środowiskowej, używając notacji słownikowej. Poniższy przykład pokazuje, jak wyświetlić zmienną środowiskową o nazwie SHELL:

```python
import os

# Wyświetl zmienną środowiskową SHELL
print(f"Zmienna środowiskowa SHELL: {os.environ['SHELL']}")
```

Aby zmienić zmienną środowiskową, można użyć funkcji `os.environ.update()`. Przykładowo, aby ustawić zmienną środowiskową o nazwie `VAR` na wartość value, można użyć następującego kodu:

```python
import os

os.environ.update({'VAR': 'value'})
```

Uwaga: zmiany zmiennych środowiskowych zachodzą tylko w obrębie bieżącego procesu. Po zakończeniu działania skryptu zmiany te nie będą widoczne dla innych procesów. Aby zmiany zmiennych środowiskowych zostały zapisane dla całego systemu, należy je zapisać w odpowiednim pliku konfiguracyjnym (np. `/etc/environment` lub `/etc/bash.bashrc` w systemie Linux).
