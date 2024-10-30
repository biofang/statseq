
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typer
from pathlib import Path
from enum import Enum
from typing import List

from statseq.fareader import Reader
from statseq.fastat import FaStat

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
app = typer.Typer(context_settings=CONTEXT_SETTINGS, add_completion=False)

__version__ = "0.1.2"

class Attrs(str,Enum):
    id = "id",
    seq = "seq",
    seq_len = "seq_len",
    gc_content = "gc_content"

def parse_values(value: str) -> List[str]:
    '''
    Preprocess parameters
    '''
    value_lst = [v.strip() for v in value.split(',')]
    for val in value_lst:
        if val not in  [item.value for item in Attrs]:
            raise TypeError(f"{val} is not find!")
    return value_lst

@app.command(no_args_is_help=True,help="Fasta Sequence Stat Function")
def stat(
    filepath: Path = typer.Option(...,"--filepath","-f", help="Input fasta file path."),
    summary : bool = typer.Option(True,
                                  "--summary/--no-summary","-s/-no-s",help="Output fasta summary stat info.")
):
    fa_stat = FaStat(filepath)
    if summary:
        print(fa_stat.summary)

@app.command(no_args_is_help=True,help="Fasta Reader Function")
def reader(
    filepath: Path = typer.Option(...,"--filepath","-f", help="Input fasta file path."),
    # attrs : List[Attrs] = typer.Option(["id","seq"],"--attrs","-a", help="Input fasta file path."),
    attrs : str = typer.Option(",".join([i.value for i in Attrs]),"--attrs","-a",help="Input one or more values, separated by commas",callback=parse_values),
):
    header = "\t".join(attrs)
    print(header)
    with Reader(filepath) as parser:
        for record in parser:
            ele_list = []
            for attr in attrs:
                if hasattr(record,attr):
                    ele_list.append(getattr(record, attr))
                else:
                    raise TypeError(f"The record objecthas no {attr} attribute")
            ele_info = "\t".join(map(str,ele_list))
            print(ele_info)

@app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
        version: bool = typer.Option(False, '--version', '-v', help='Show version informatio.'),
):
    if version:
        typer.echo(f'demoseq version: {__version__}')
        raise typer.Exit()

if __name__ == "__main__":
    app()

