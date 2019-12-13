import sys
import re
def clean(file_name):
    """
    Input: text file
    Output: cleaned from unwanted characters
    """
    with open(file_name, 'r') as file :
        words = file.read().lower()
        words = re.sub(r"[-()\"#/@;:<>{}=~|.?,]", "",words)
        # print(words)
        return words

if __name__ == '__main__':
    words_list = clean(sys.argv[1])
