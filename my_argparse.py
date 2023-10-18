import argparse

if __name__ == "__main__":
    print('Parser initialized!')
    parser = argparse.ArgumentParser(description='Argument Parser Example')

    # Add arguments to the parser
    parser.add_argument('--l', type=str, default='ua', help='Language (default: ua)')
    parser.add_argument('--c', type=str, default='word', help='Keyword (default: word)')
    parser.add_argument('--m', type=int, default=0, help='Value (default: 0)')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Retrieve values from parsed arguments
    lang = args.l
    keyword = args.c
    value = args.m

    print(f'lang: {lang}, keyword: {keyword}, value: {value}')
