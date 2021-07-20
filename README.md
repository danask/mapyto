# MaPyto | by s0rcy_r『魔女』

![MaPyto Logo](https://github.com/s0rcy-r/mapyto/blob/main/Logo.PNG?raw=true)

![GitHub last commit](https://img.shields.io/github/last-commit/s0rcy-r/mapyto?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/s0rcy-r/mapyto?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/s0rcy-r/mapyto?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/s0rcy-r/mapyto?style=for-the-badge)
![Python version](https://img.shields.io/badge/Python-v3.9-red?style=for-the-badge)
![Project version](https://img.shields.io/badge/Project%20version-v1.0.0-orange?style=for-the-badge)

## Description

**MaPyto:earth_africa:** is a python program that takes multiple addresses as input and shows in output an "*optimized*" route on Google Map (without the maximum of 10 steps allowed by Google).
This program works with Python 3.9, Django and geopy (+ Nominatim).

### How does it works ?

It works most of the times so don't ask questions ...
Well, in fact the main API sort the addresses step by step taking into account the distance between each place. This methodology doesn't work each time, but based on my multiple tests, it came out that 80% of the results are correct,
18% only have one misplaced address and only 2% are totally incorrect.

## Installation
Only one thing to do :
```pip install -r requirements.txt```

## Usage

### Django usage

```
cd mapyto
python runserver.py
```

### API usage
For more information about the API, go see the (light) documentation in the API folder.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Social

![Twitter Follow](https://img.shields.io/twitter/follow/s0rcy_r?style=social)
![GitHub followers](https://img.shields.io/github/followers/s0rcy-r?label=Follow%20me&style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/s0rcy-r/mapyto?style=social)
