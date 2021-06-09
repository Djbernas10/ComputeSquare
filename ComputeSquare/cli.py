from ComputeSquare import *

import click

@click.command()
@click.option("-n",'--num', type= int, help='specificy a number', required=True)

def main(num):
    """The main function for this script."""

    result = square(num)
    print(f"The square of {num} is {result}")

if __name__ == '__main__':
    main()