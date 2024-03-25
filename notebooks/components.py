import panel as pn

def create_bounding_box(x_min, x_max, y_min, y_max):
    x_min_text = pn.widgets.TextInput(name='x-min', value=str(x_min), disabled=True)
    x_max_text = pn.widgets.TextInput(name='x-max', value=str(x_max), disabled=True)
    y_min_text = pn.widgets.TextInput(name='y-min', value=str(y_min), disabled=True)
    y_max_text = pn.widgets.TextInput(name='y-max', value=str(y_max), disabled=True)
    return (x_min_text, x_max_text, y_min_text, y_max_text)