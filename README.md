# deeplapi: DeepL translation API

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This is a [Flask](https://github.com/pallets/flask) server that provides the DeepL API.
If you simply want to use DeepL API in Python, please visit https://github.com/DeepLcom/deepl-python

## Install

```
$ git clone https://github.com/poyo46/deeplapi
$ cd deeplapi
$ poetry install
```

## Run

```
$ poetry shell
$ export DEEPL_AUTH_KEY=your auth key here
$ python -m deeplapi.server
```

If you want to change the configuration, edit the `config/*.yml`.

## Examples

### Translation

Translate `おはようございます。` into `EN-US`.

```
$ curl 'http://localhost:6174/translation?text=%E3%81%8A%E3%81%AF%E3%82%88%E3%81%86%E3%81%94%E3%81%96%E3%81%84%E3%81%BE%E3%81%99%E3%80%82&target_lang=EN-US'
{
  "detected_source_lang": "JA",
  "text": "Good morning."
}
```

Translate `Beautiful is better than ugly.` into `JA`.

```
$ curl 'http://localhost:6174/translation?text=Beautiful%20is%20better%20than%20ugly.&target_lang=JA'
{
  "detected_source_lang": "EN",
  "text": "醜いより美しい方がいい。"
}
```

You can also specify the source language by setting the parameter `source_lang`.

### Available languages

Requests all available languages.

```
$ curl 'http://localhost:6174/languages'
{
  "source_languages": [
    {
      "code": "BG",
      "name": "Bulgarian"
    },
    {
      "code": "CS",
      "name": "Czech"
    },
    {
      "code": "DA",
      "name": "Danish"
    },
    {
      "code": "DE",
      "name": "German"
    },
    {
      "code": "EL",
      "name": "Greek"
    },
    {
      "code": "EN",
      "name": "English"
    },
    {
      "code": "ES",
      "name": "Spanish"
    },
    {
      "code": "ET",
      "name": "Estonian"
    },
    {
      "code": "FI",
      "name": "Finnish"
    },
    {
      "code": "FR",
      "name": "French"
    },
    {
      "code": "HU",
      "name": "Hungarian"
    },
    {
      "code": "IT",
      "name": "Italian"
    },
    {
      "code": "JA",
      "name": "Japanese"
    },
    {
      "code": "LT",
      "name": "Lithuanian"
    },
    {
      "code": "LV",
      "name": "Latvian"
    },
    {
      "code": "NL",
      "name": "Dutch"
    },
    {
      "code": "PL",
      "name": "Polish"
    },
    {
      "code": "PT",
      "name": "Portuguese"
    },
    {
      "code": "RO",
      "name": "Romanian"
    },
    {
      "code": "RU",
      "name": "Russian"
    },
    {
      "code": "SK",
      "name": "Slovak"
    },
    {
      "code": "SL",
      "name": "Slovenian"
    },
    {
      "code": "SV",
      "name": "Swedish"
    },
    {
      "code": "ZH",
      "name": "Chinese"
    }
  ],
  "target_languages": [
    {
      "code": "BG",
      "name": "Bulgarian"
    },
    {
      "code": "CS",
      "name": "Czech"
    },
    {
      "code": "DA",
      "name": "Danish"
    },
    {
      "code": "DE",
      "name": "German"
    },
    {
      "code": "EL",
      "name": "Greek"
    },
    {
      "code": "EN-GB",
      "name": "English (British)"
    },
    {
      "code": "EN-US",
      "name": "English (American)"
    },
    {
      "code": "ES",
      "name": "Spanish"
    },
    {
      "code": "ET",
      "name": "Estonian"
    },
    {
      "code": "FI",
      "name": "Finnish"
    },
    {
      "code": "FR",
      "name": "French"
    },
    {
      "code": "HU",
      "name": "Hungarian"
    },
    {
      "code": "IT",
      "name": "Italian"
    },
    {
      "code": "JA",
      "name": "Japanese"
    },
    {
      "code": "LT",
      "name": "Lithuanian"
    },
    {
      "code": "LV",
      "name": "Latvian"
    },
    {
      "code": "NL",
      "name": "Dutch"
    },
    {
      "code": "PL",
      "name": "Polish"
    },
    {
      "code": "PT-BR",
      "name": "Portuguese (Brazilian)"
    },
    {
      "code": "PT-PT",
      "name": "Portuguese (European)"
    },
    {
      "code": "RO",
      "name": "Romanian"
    },
    {
      "code": "RU",
      "name": "Russian"
    },
    {
      "code": "SK",
      "name": "Slovak"
    },
    {
      "code": "SL",
      "name": "Slovenian"
    },
    {
      "code": "SV",
      "name": "Swedish"
    },
    {
      "code": "ZH",
      "name": "Chinese"
    }
  ]
}
```

### Usage

Requests the current API usage.

```
$ curl 'http://localhost:6174/usage'
{
  "character": {
    "count": 381,
    "limit": 500000,
    "limit_exceeded": false,
    "valid": true
  },
  "document": {
    "count": null,
    "limit": null,
    "limit_exceeded": false,
    "valid": false
  },
  "team_document": {
    "count": null,
    "limit": null,
    "limit_exceeded": false,
    "valid": false
  }
}
```
