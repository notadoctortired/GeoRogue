# GeoRogue

A 2D game built using Python's Pygame module. It is a battling simulator using basic geometric shapes as the characters. The inspiration comes primarily from Pokemon and Geometry Dash.

The user is prompted with a choice between a square "Geo" or a circle "Geo". 

Square Geos are given 1.25x extra health, boosting their total health to 125, whereas Circle Geos are provided a 1.2x attack boost. Squares are more likely to get physical moves and frozen status moves. Circles are more likely to get magic moves and burning status moves. (Move types are explained below)

Each of them has a set list of moves that they may be given once the battle begins. The move types are:

 - Physical, of which circles are weak to
 - Magic, of which squares are weak to
 - Status, which (depending on the move) have a chance to inflict a type of status, including:
   - Paralysis, which has a 50% chance to prevent a move for 3-5 turns
   - Burning, which takes 3% of the total health away for 3-5 turns
   - Frozen, which prevents moves for 1-3 turns

Ranges for status (special) moves are calculated using python's random module, specifically randrange.

Weaknesses apply a 1.15x damage boost to an attack.