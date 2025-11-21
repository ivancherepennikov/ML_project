from parse_photo import parse_photo
from resize_symbols import resize_symbols
from network_fit_and_score import final

input_photo = 'numbers.jpeg'

def main(input_photo):
    parse_photo(input_photo)
    resize_symbols()
    return(final())