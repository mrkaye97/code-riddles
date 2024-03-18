# code-riddles

An exercise for a talk at work on optimizing number crunching code. Inspired by the [One Billion Row Challenge](https://www.morling.dev/blog/one-billion-row-challenge/), which got popular on HackerNews in early 2024.

## Introduction

The objective of this exercise is to take a text file like this:

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. John's;15.2
Cracow;12.6
...
```

And get the mean, minimum, and maximum temperature per station, and output it like this (alphabetically ordered):

```
{Abha=5.0/18.0/27.4, Abidjan=15.7/26.0/34.1, Abéché=12.1/29.4/35.6, Accra=14.7/26.4/33.1, Addis Ababa=2.1/16.0/24.3, Adelaide=4.1/17.3/29.7, ...}
```

## Instructions

First, you'll need to generate the data. I'd recommend cloning this repo, then:

1. Create a virtual environment:

```bash
pyenv virtualenv 3.10.9 code-riddles
pyenv local code-riddles
```

2. Install deps into the venv:

```bash
pip install -r requirements.txt
```

Feel free to add dependencies as you need them.

3. Generate the data!

```bash
`python3 src/generate_data.py 100_000_000`
```

4. Profile your code! I've pre-installed [memray](https://github.com/bloomberg/memray), a memory profiler, but feel free to use any tools you like
