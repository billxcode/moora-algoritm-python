from bokeh.plotting import show, output_file, figure, save
from bokeh.models import HoverTool

NAME_FILE = "result/preferensi.txt"
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
                print(row)
                RESULT_ARRAY.append(float(row).real)

print(RESULT_ARRAY)
print(INDEX_ARRAY)

output_file("result.html")

disp = figure(plot_width=1000)
disp.vbar(x=INDEX_ARRAY, width=0.5, bottom=0, top=RESULT_ARRAY, color="#74ADD1")

save(disp)
 