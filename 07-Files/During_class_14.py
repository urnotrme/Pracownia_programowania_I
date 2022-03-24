import json
book={
    "name":"Love Yourself",
    "author":"Olivia Held",
    "pages":287,
    "genre":"romance"
    
    }

with open("favourite.json", "w") as file:
    json.dump(book, file, indent=4)
    
