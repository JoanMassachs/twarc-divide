import json
import os

import click
from tqdm import tqdm
from twarc import ensure_flattened


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

    with tqdm(total=os.stat(infile.name).st_size, unit='B') as progress:
        for line in infile:
            for t in ensure_flattened(json.loads(line)):
                date = t['created_at'][:index]
                with open(outdir + date + '.jsonl', 'a') as out:
                    out.write(json.dumps(t) + '\n')
            progress.update(len(line))


if __name__ == '__main__':
    main()
