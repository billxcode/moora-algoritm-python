from bokeh.plotting import show, output_file, figure

output_file("line.html")
p = figure()
p.line([1,2,3,4,5], [6,5,7,3,2], line_width=2)
show(p)
