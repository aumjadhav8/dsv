from bokeh.plotting import figure, show, output_file
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
output_file("line.html")
p = figure(title="Bokeh Line Graph with Annotations - Garvit Saraf USN: 1BI21CS185", x_axis_label='X', y_axis_label='Y')
p.line(x, y, legend_label="Temp.", line_width=2)
p.circle(x, y, size=10, color="navy", alpha=0.5)
for i, (xi, yi) in enumerate(zip(x, y)):
    p.text(xi, yi, text=[f"Point {i+1}"], text_color="red", text_align="center")
show(p)