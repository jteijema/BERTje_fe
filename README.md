# BERTje feature extractor for ASReview

This repository houses a dutch feature extractor model for ASReview. It is based on the following model: [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased).

## Getting started

Install the template with:

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
