def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author is None and year is None:
        info = f'"{title}"'
    elif author is None:
        info = f'"{title}" was written in {year}'
    elif year is None:
        info = f'"{title}" was written by {author}'
    else:
        info = f'"{title}" was written by {author} in {year}'
    print(info)
