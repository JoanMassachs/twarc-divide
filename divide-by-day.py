import json
import os

import click
from twarc.decorators2 import FileSizeProgressBar
from twarc.expansions import ensure_flattened


@click.command()
@click.option(
    '--granularity',
    '-g',
    type=click.Choice(
        ['year', 'month', 'day', 'hour', 'minute', 'second'],
        case_sensitive=False
    ),
    default='day',
    show_default=True,
    help='Granularity of temporal windows'
)
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outdir', type=click.Path(exists=False))
def main(granularity, infile, outdir):
    '''
    Divides the input file in an output file for each temporal window.
    Each output file contains the tweets published in its temporal window.
    Output files are saved in the output directory,
    and their names are the dates of the temporal windows.
    If an output file already exists, new output is appended to the old one.
    '''
    indices = {
        'year': 4,
        'month': 7,
        'day': 10,
        'hour': 13,
        'minute': 16,
        'second': 19
    }
    index = indices[granularity]

    with FileSizeProgressBar(infile, None) as progress:
        for line in infile:
            for t in ensure_flattened(json.loads(line)):
                date = t['created_at'][:index]
                with open(os.path.join(outdir, date + '.jsonl'), 'a') as out:
                    out.write(json.dumps(t) + '\n')
            progress.update(len(line))


if __name__ == '__main__':
    main()
