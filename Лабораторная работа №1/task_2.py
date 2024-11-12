disk_size_mb = 1.44  # объём дискеты в Мб
pages_per_book = 100  # страниц в книге
lines_per_page = 50  # строк на странице
chars_per_line = 25  # символов в строке
bytes_per_char = 4  # байт на символ

chars_per_page = lines_per_page * chars_per_line
total_chars_per_book = chars_per_page * pages_per_book
book_size_bytes = total_chars_per_book * bytes_per_char

disk_size_bytes = disk_size_mb * 1024 * 1024

books_on_disk = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", books_on_disk)
