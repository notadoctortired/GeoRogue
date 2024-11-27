# GeoRogue

A 2D game built using Python's Pygame module. The premise of the game is to battle 2D geometric shapes called Geos, with the goal of winning against your opponent by depleating their health before they depleat yours. The user is prompted with a choice between a square "Geo" or a circle "Geo". Square Geos are given 1.25x extra health, boosting their total health to 125, whereas Circle Geos are provided a 1.2x attack boost.

There are two types of move:
 - Physical, of which circles are weak to
 - Magic, of which squares are weak to

Weaknesses apply a 1.15x damage boost to an attack.

To run the game (through the scripts, functioning executable coming soon) you require the following:
 - Python 3.12 or above installed
 - Pygame installed
  - Windows - pip install pygame
  - Linux (Debian-based) - sudo apt-get install python3-pygame
  - Linux (Arch-based) - sudo pacman -S python-pygame
  - Linux (Fedora-based) - sudo dnf install python-pygame
  - Mac - xcode-select --install, then do pip3 install pygame

Once you have done so, simply run main.py in scripts and enjoy!