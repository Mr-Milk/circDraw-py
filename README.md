# circDraw

A python package for circDraw visualization



## Installation

```shell
pip3 install circDraw

# install dependencies
pip3 install numpy
pip3 install matplotlib
pip3 install colour
```

- Python3
- Matplotlib
- Numpy
- Colour



## Usage

```python
from circDraw import circDraw

 # initiate a circDraw instance
cd = circDraw()

# set color of circ_on_chr (optional)
cd.set_palette(["#5CA0F2", "#FF881D", '#e30067', '#924900','#ab9c00','#ccd0d2', '#075800', '#5e0094',])

# set color of modifications (optional)
mod_palette = {'m6a': '#E98B2A',
               'm5c': '#E16B8C',
               'm1a': '#64363C',
               'pu': '#ffa12c',
               '2ome': '#1a6f00',
               'mre': '#6D2E5B',
               'rbp': "#2B5F75",
               'orf': '#516E41'}
cd.set_mod_palette(mod_palette)

# draw backsplicing site on chromosome region
cd.circ_on_chr('Your file')

# draw modifications on circRNA
cd.mod_on_circ('Your file')
```

<img src='circDraw.png' width='85%'>

<img src='hsa_circ_0001.png' width='65%'>

### API

#####circ_on_chr

```python
circDraw.circ_on_chr(file, title='circDraw', dpi=300, save='png', show=True, size=(10, 5))
```

- File:
  
  - Only supported 'csv'
    
  - | Start | End  | Type | Name | Color (Optional) |
    | ----- | ---- | ---- | ---- | ---------------- |
    |       |      |      |      |                  |
  
  - Start < End
  
  - Type: **circ**, **exon**, **intron**, **gene**
  
  - Color: RGB, RGBA, hex, or [supported color names](https://matplotlib.org/examples/color/named_colors.html).
  
- Title: The title of the plot

- Save: file format you wish to save as, **PNG**, **PDF**, **JPEG**, etc.

- Show: Bool, wheather to show the plot after rendering.

- Size: (Length, Width) the size of the plot.

#####mod_on_circ

```python
circDraw.mod_on_circ(self, file, dpi=100, save='png', show=True, size=(7, 7), sep_mod=False)
```

- File:

  - Only supported 'csv'

  - | Start | End  | Type | Name | Color (Optional) |
    | ----- | ---- | ---- | ---- | ---------------- |
    |       |      |      |      |                  |

  - Start < End

  - Type: **circ**, **exon**, **intron**, and modifications type

    - Modifications type: **m6A**, **m1A**, **m5C**, **pU**, **2OMe**, **MRE**, **RBP**, **ORF**

  - Color: RGB, RGBA, hex, or [supported color names](https://matplotlib.org/examples/color/named_colors.html).

- Save: file format you wish to save as, **PNG**, **PDF**, **JPEG**, etc.

- Show: Bool, wheather to show the plot after rendering.

- Size: (Length, Width) the size of the plot.

- sep_mod: Bool, prevent the modifications from overlapping if set **True**.

##### set_palette

```python
circDraw.set_palette(palette)
```

A list of colors, the length of the list must bigger than 5.

##### set_mod_palette

```python
circDraw.set_mod_palette(palette)
```

A dictionary of colors match with the modification. You can change any one of the modification colors.

