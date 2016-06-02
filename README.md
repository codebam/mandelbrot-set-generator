# Mandelbrot Generator
[https://github.com/codebam/mandelbrot](https://github.com/codebam/mandelbrot)

Written in Python, Licensed under GPLv3

## Things I did to improve speed
- Most of the speed of the program is due to me using built in python complex mathematics which are more efficient.
- Since f(x) = -f(x) it prints both sides of the image at the same time, which makes it twice as fast [[proof](https://www.lucaswillems.com/en/articles/3/mandelbrot-set-symmetry)]
- A formula [here](https://en.wikipedia.org/wiki/Mandelbrot_set#Cardioid_.2F_bulb_checking) is used to prevent the iterations of the second period bulb.
- The display is only updated when necessary since this takes a lot of resources for each pixel. It is done line by line, because doing it all at once only improves speed by a few fractions of a second and isn't worth it.
