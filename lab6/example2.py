books = ["ulysses", "animal farm", "brave new world", "ender's game"]

book_dict = {}
for book in books :
  key = book
  value1 = len(book)
  value2 = len(set(book))
  value = (value1, value2)
  book_dict.update( {key:value} )
      
for book in book_dict.keys() :
  print(book, "->", value)
  

