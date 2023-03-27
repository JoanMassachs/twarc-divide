import json
import os

import click
from tqdm import tqdm
from twarc import ensure_flattened


@click.command()
@click.option('--granularity', '-g', default='day', show_default=True)
@click.argument('infile', type=click.File('r'))
@click.argument('outdir', type=click.Path(exists=False))
def main(granularity, infile, outdir):
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
