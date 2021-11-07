import threading
import urllib.request, urllib.parse, urllib.error
import time

# results - lista zawierająca liczbę wszystkich znaków podanych stron url
results = []

class thread(threading.Thread):
    def __init__(self, urls):
        super().__init__()
        self.urls = urls
        
    def run(self):
        self.urls = urls

        for u in urls:
            url_open = urllib.request.urlopen(u)
            results.append(len(url_open.read()))



#urls_num - liczba adresów url
#urls - lista adresów url
urls_num = 5
urls = []

# pobierz dane od użytkownika i zapisz je w liście
for i in range(urls_num):  
    url = input("Podaj URL %d: " % (i+1))
    urls.append(url)

# dodatkowy wątek liczący znaki stron
aux_thread = thread(urls)

print("Rozpoczęto pobieranie.")
aux_thread.start()

while aux_thread.is_alive():
    print("Oczekiwanie na zakończenie pobierania...")
    time.sleep(1)

print("Zakończono pobieranie")

#wypisz dane użytkownikowi
for i in range(len(urls)):
    print(f"Liczba znaków dla {urls[i]}: {results[i]}")
