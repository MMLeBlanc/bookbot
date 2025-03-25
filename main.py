import sys
from stats import count_words, count_letters, order_dict 

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
        print('----------- Word Count ----------')
        count_words(book_text)
        print('--------- Character Count -------')
        for dictionary in order_dict(count_letters(book_text)):
            print(f'{dictionary['char']}: {dictionary['count']}')
        

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    get_book_text(file_path)
    print('============= END ===============')

if __name__=="__main__":
    main()
