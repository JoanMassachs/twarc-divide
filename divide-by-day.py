import json

import click
from tqdm import tqdm
from twarc import ensure_flattened


@click.command()
@click.option('--count-lines', '-c', is_flag=True, default=False)
@click.option('--lines', '-l', default=None)
@click.option('--granularity', '-g', default='day')
@click.argument('infile')
@click.argument('outdir')
def main(count_lines, lines, granularity, infile, outdir):
    indices = {
        'year': 4,
        'month': 7,
        'day': 10,
        'hour': 13,
        'minute': 16,
        'second': 19
    }
    index = indices[granularity]

    if count_lines:
        with open(infile) as f:
            lines = sum(1 for line in f)
    elif lines is not None:
        lines = int(lines)

    with open(infile) as infile:
        for line in tqdm(infile, total=lines):
            for t in ensure_flattened(json.loads(line)):
                date = t['created_at'][:index]
                with open(outdir + date + '.jsonl', 'a') as out:
                    out.write(json.dumps(t) + '\n')


if __name__ == '__main__':
    main()
