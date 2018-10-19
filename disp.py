from bokeh.plotting import show, output_file, figure

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

disp = figure()
disp.line(INDEX_ARRAY, RESULT_ARRAY, line_width=2)
show(disp)
 