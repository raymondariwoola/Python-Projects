# Image Processing

### Filters and Processes

1. black_and_white
2. black_red_blue_green
3. vignette_effect
4. clarendon_effect
5. greyscale
6. rotate_90_deg
7. rotate_multiples_of_90_deg
8. enlargeXY
9. BW_highContrast
10. lighten
10. darken



## Usage

```python
original = image.Image("image.jpg")

# black_red_blue_green
final = black_red_blue_green(original)

# vignette_effect
final = vignette_effect(original)

# clarendon_effect
final = clarendon_effect(original)

# greyscale
final = greyscale(original)

# rotate_90_deg
final = rotate_90_deg(original)

# rotate_multiples_of_90_deg
final = rotate_multiples_of_90_deg(original, 90)

# enlargeXY
final = enlargeXY(original, 5, 1)
newwin = image.ImageWin(final.getWidth(), final.getHeight())
final.draw(newwin)

# BW_highContrast
final = BW_highContrast(original)

# lighten
final = lighten(original)

# darken
final = darken(original)
```
