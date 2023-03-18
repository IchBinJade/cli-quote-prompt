# CLI Quote Prompt DB
A simple Python CLI application to allow entry, and display, of quotes stored in a local database.

## Description
This CLI app allows users to add their quotes to a database and either retrieve all entries to display or have the app return a random quote.

## Getting Started

### Dependencies
The following packages are required:

* click==8.1.3
* typer==0.7.0

### Installing
Clone this repository to your local machine:

`git clone https://github.com/ichbinjade/cli-quote-prompt`

You can then install the dependencies using the requirements.txt file.

### Executing Program

#### Add a Quote
```
~/cli-quote-prompt$ python quotecli.py add "Author"
Enter the quote:
```

#### Display All Quotes
`python quotecli.py display-all`

#### Display Random Quote
`python quotecli.py display-random`

## Help
```
Usage: quotecli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  add             Add a new quote by AUTHOR.
  display-all     Display all quotes currently in the database
  display-random  Display a random quote from the database
```

## Version History
0.2 - Fix Issue [#1](https://github.com/IchBinJade/cli-quote-prompt/issues/1) where database required manual initialisation

0.1 - Original Version

## License
[MIT](https://choosealicense.com/licenses/mit/)
