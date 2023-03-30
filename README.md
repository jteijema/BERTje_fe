# BERTje feature extractor for ASReview

This repository houses a dutch feature extractor model for ASReview

## Getting started

Click the `Use this template` button and add/modify the algorithms. Install your new classifier with

```bash
pip install .
```

or

```bash
pip install git+https://github.com/JTeijema/BERTje_fe
```

## Usage

The new classifier `bertje` is defined in
[`asreviewcontrib\models\bertje.py`](asreviewcontrib\models\bertje.py) and can be used in a simulation.

```bash
asreview simulate example_data_file.csv -e bertje
```

## License

MIT license
