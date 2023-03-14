import typer
import random
from model import Quote
from database import add_row, get_quotes

app = typer.Typer()


def print_line(line):
    text, auth = line
    print(f"{text} - {auth}")


@app.command()
def add(author: str):
    """
    Add a new quote by AUTHOR. Enter the quote at a prompt
    """
    q_text = input("Enter the quote: ")
    to_add = Quote(q_text, author)
    add_row(to_add)
    print(f"Added quote by {author} to database!")


@app.command()
def display_all():
    """
    Display all quotes currently in the database
    """
    quotes_list = get_quotes()
    for quote in quotes_list:
        print_line(quote)


@app.command()
def display_random():
    """
    Display a random quote from the database
    """
    quotes_list = get_quotes()
    selection = random.choice(quotes_list)
    print_line(selection)


if __name__ == "__main__":
    app()
