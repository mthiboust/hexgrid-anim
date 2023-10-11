# Hexgrid Anim

Playing with hexagonal grids with [Manim](https://github.com/ManimCommunity/manim). 

![Infinite nested hexgrids](https://raw.githubusercontent.com/mthiboust/hexgrid-anim)/docs/infinite_nested_hexgrid_640x360.gif)

# Installation

See [Manim](https://github.com/ManimCommunity/manim) to install Manim.

# Usage

To generate an animation:
```bash
manim -pql ./hexgrid-anim/animation.py CreateInfiniteNestedHexGrid # Low resolution
manim -p ./hexgrid-anim/animation.py CreateInfiniteNestedHexGrid # High resolution
```

# Credits

* [Manim](https://github.com/ManimCommunity/manim)
* Amit Patel for his very useful [guide on hexagonal grids](https://www.redblobgames.com/grids/hexagons/)
