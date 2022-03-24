import ebook


ebook1 = ebook.Ebook("Girl Online", "Zoe Sugg", 362)
ebook1.book_open()
print(ebook1.title, ebook1.author, ebook1.pages, ebook1.cpage)
ebook1.next_page()
ebook1.next_page()
ebook1.next_page()
ebook1.next_page()
print(ebook1.title, ebook1.author, ebook1.pages, ebook1.cpage)
ebook1.book_close()
ebook1.next_page()


