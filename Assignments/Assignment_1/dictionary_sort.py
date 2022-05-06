from tokenize import String
from typing import Dict, List
import json

books = [
  {"name":"BookA", "author": "AuthorA", "publishedYear": 2009},
  {"name":"BookJ", "author": "AuthorJ", "publishedYear": 2000},
  {"name":"BookD", "author": "AuthorD", "publishedYear": 2003},
  {"name":"BookE", "author": "AuthorE", "publishedYear": 2004 },
  {"name":"BookF", "author": "AuthorF", "publishedYear": 2005 },
  {"name":"BookG", "author": "AuthorG", "publishedYear": 2006},
  {"name":"BookB", "author": "AuthorB", "publishedYear": 2001 },
  {"name":"BookH", "author": "AuthorH", "publishedYear": 2007 },
  {"name":"BookC", "author": "AuthorC", "publishedYear": 2002 },
  {"name":"BookI", "author": "AuthorI", "publishedYear": 2008 }
]

def sort_dict_list_save_to_file(dict_list: List, file_name: String):
  sorted_list = sorted(dict_list, key=lambda x: x['publishedYear'])
  list_dump = json.dumps(sorted_list, indent=2)

  with open ((file_name + '.json'), "w+") as book_file_w:
    book_file_w.write(list_dump)

sort_dict_list_save_to_file(books, 'books')