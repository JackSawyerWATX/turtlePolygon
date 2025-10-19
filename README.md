# turtlePolygon

A small Python program that uses the standard library `turtle` module to draw repeating polygons and star-like shapes on a black background. The script is intended to be simple and configurable: you can change what shapes are drawn, how many times each shape repeats, and how much the turtle rotates between repeats to produce rosette and spirograph-like patterns.

## How it works

- The program creates a `turtle.Screen()` and sets the background to black for high contrast.
- A `turtle.Turtle()` object does the drawing. The script sets a fast drawing speed and a slightly thicker pen for visibility.
- The main drawing logic is split into two helper functions:
  - `draw_shape(turtle_obj, steps, length, turn_angle=None)` draws a closed shape of `steps` segments. If `turn_angle` is not supplied, the function uses the exterior angle of a regular polygon (360 / steps).
  - `draw_repeats(turtle_obj, steps, length, turn_angle, repeats, rotate_between)` draws the same shape `repeats` times, rotating the turtle by `rotate_between` degrees between each repetition.
- A `shapes` list configures multiple shape patterns (steps, length, turn, repeats, rotate_between). The program cycles through a list of bright colors so the shapes show up on the black background.

## Mathematical relationships in the `shapes` array

Each shape config is a dictionary with these keys:
- `steps`: number of line segments (edges) the shape has. For a regular polygon this equals the number of sides (e.g., 3 = triangle, 5 = pentagon).
- `length`: the forward distance traveled for each segment.
- `turn`: the number of degrees the turtle turns after drawing each segment. If `turn` is omitted or `None`, `draw_shape` uses the polygon exterior angle, which for a regular polygon is:

  $\text{exterior angle} = \frac{360}{\text{steps}}$.

  Using this angle makes the turtle draw a regular polygon where the interior angle is $180 - \frac{360}{\text{steps}}$.

- `repeats`: how many times to draw the same polygon before switching to the next configured shape (or color). Repeating a polygon while rotating the turtle between repeats forms a rosette pattern.
- `rotate_between`: the degrees to rotate the turtle between consecutive repeats of the same polygon. Smaller rotation values create dense circular patterns; larger values space repeated polygons more widely.

Star shapes: to draw star-like shapes you provide a `turn` value that is not the exterior angle of the regular polygon. For example, a classic 5-pointed star is drawn by moving forward and turning 144° each step. Why 144°? A 5-point star connects every 2nd vertex in a regular pentagon; the turning angle becomes:

  $\text{star turn} = 180 - \left(\frac{360}{5} \times 2\right) = 144$ (equivalently you can use 144 directly).

General rule for star-like {n, k} (connect every k-th vertex) shapes:

  $\text{turn} = 180 - \frac{360 \times k}{n}$

Choose `k` co-prime with `n` to get a single continuous star polygon.

## Example `shapes` config (found in the file)

```python
shapes = [
    {"steps": 6, "length": 100, "turn": 75, "repeats": 6, "rotate_between": 50},
    {"steps": 5, "length": 160, "turn": 144, "repeats": 8, "rotate_between": 15},
    {"steps": 3, "length": 140, "turn": None, "repeats": 12, "rotate_between": 10},
]
```

- First entry draws a 6-segment pattern using an explicit 75° turn (not the regular polygon exterior). It repeats 6 times and rotates 50° between repeats.
- Second entry draws a 5-point star (turn 144°) repeated 8 times with a 15° rotation between repeats.
- Third entry draws an equilateral triangle (turn omitted so 360/3 = 120° is used) repeated 12 times with 10° rotation between repeats.

Tweak these numbers to explore new patterns.

## Frameworks / Libraries used

- Python 3.x (the script uses only the standard library)
- `turtle` — part of Python's standard library, provides simple drawing primitives and a GUI window for immediate visual feedback.

No external packages are required.

## How to run (PowerShell on Windows)

1. Make sure you have Python 3 installed and `python` available on your PATH.
2. Open PowerShell and navigate to the project folder (where `turtlePoly.py` is located):

```powershell
cd "C:\Users\jonat\OneDrive\Desktop\turtlePolygon"
```

3. Run the script:

```powershell
python .\turtlePoly.py
```

A new window will open showing the turtle drawing. The program will finish and keep the window open until you close it.

## Tips / Customization

- Change or add entries in the `shapes` list to draw different shapes.
- Adjust `repeats` and `rotate_between` to control how many polygons are drawn per color and how much rotation happens between each polygon.
- To draw a star polygon use the `turn` value computed by the star formula above, or experiment with other angles.
- If the drawing is too slow, increase `t.speed('fastest')` or lower the `length` values.

## License

This project is small demo code — feel free to modify and experiment.

### I love you all! Happy coding!