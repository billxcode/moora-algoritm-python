from bokeh.plotting import show, output_file, figure, save
from bokeh.models import HoverTool

NAME = input('Tuliskan nama file preferensi :')

NAME_FILE = "result/preferensi_"+NAME+"_RESULT.txt"
RESULT_ARRAY = []
INDEX_ARRAY = []
with open(NAME_FILE, 'r') as file:
    index = 0
    for rows in file:
        index +=1
        INDEX_ARRAY.append(index)
        rows = rows.split("\n")
        for row in rows:
            if row!='':
                RESULT_ARRAY.append(float(row).real)

output_file("graph/graph_"+NAME+".html")

disp = figure(plot_width=1000)
disp.vbar(x=INDEX_ARRAY, width=0.5, bottom=0, top=RESULT_ARRAY, color="#74ADD1")
# disp.line(INDEX_ARRAY, RESULT_ARRAY, line_width=2, color="#DE2D26")
# disp.inverted_triangle(x=INDEX_ARRAY, y=RESULT_ARRAY, size=8, color="#DE2D26")

save(disp)
 