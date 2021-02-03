# The MaPyto Project (by *s0rcy_r*)

![GitHub last commit](https://img.shields.io/github/last-commit/s0rcy-r/mapyto?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/s0rcy-r/mapyto?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/s0rcy-r/mapyto?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/s0rcy-r/mapyto?style=for-the-badge)

## Description

**MaPyto:earth_africa:** is a python program that takes multiple addresses as input and shows in output an "*optimized*" route on Google Map (without the maximum of 10 steps allowed by Google).
This program works in Python 3.9 with Django and geopy (+ Nominatim).

### How does it works ?

It works most of the times so don't ask questions ...
Well, in fact the main API sort the addresses step by step taking into account the distance between each place. This methodology doesn't work each time, but based on my multiple tests, it came out that 80% of the results are correct,
18% only have a misplaced address and only 2% are incorrect.

## Installation
Only one thing to do :
```pip install -r requirements.txt```

## Usage

### Django usage
```
cd mapyto
python runserver.py <ip>:<port>
```

*example :*
```
cd mapyto
python runserver.py 0.0.0.0:8080
```

### API usage
For more informations about the API, go see the full documentation in the API folder.

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