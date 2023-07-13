# twarc-divide

*twarc-divide* adds a new `divide` [twarc] command that
lets you divide collected twitter data by date or a custom temporal window.

## Install

To install you will need to:

```
pip3 install twarc-divide
```

## Use

First you will need to collect some data with [twarc]:
```
twarc2 search politics tweets.jsonl
```

Then you can divide them by day:
```
mkdir days/
twarc2 divide tweets.jsonl days/
```
This will create in the directory `days/` an output file for each day
whose name will be the date.
If the output file already exists, it will append the output to it.

You can also change the granularity of the temporal windows used:
```
mkdir hours/
twarc2 divide --granularity hour tweets.jsonl hours/
```

[twarc]: https://github.com/docnow/twarc
