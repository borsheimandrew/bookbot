def main():
  book_path = "books/frankenstein.txt"
  book_text = get_text(book_path)
  word_count = get_words(book_text)

  chars_dict = get_chars_dict(book_text)
  sorted_list = sort(chars_dict)
  print_report(book_path, word_count, sorted_list)
  

def get_text(book_path):
    with open(book_path) as f:
      return f.read()
    
def get_words(text):
   words = text.split()
   return len(words)

def get_chars_dict(words):
  chars = {}

  for c in words:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1

  return chars

def sort_on(dict):
  return dict["occurances"]

def sort(dict):
  new_list = []
  for k in dict:
    if k.isalpha():
      new_list.append({"char": k, "occurances": dict[k]})
  new_list.sort(reverse=True, key=sort_on)
  return new_list

def print_report(book_path, word_count, sorted_list):
    print(f"--- Begin report of {book_path} ---")      
    print(f"{word_count} words found in the document\n\n")
    
    for c in sorted_list:
      print(f"The {c['char']} character was found {c['occurances']} times")
    print("--- End report ---")


main()