import helper_function as hf
import inspect
import importlib
import pandas as pd


importlib.reload(hf)


funcs = []
def list_functions(): 
    members = inspect.getmembers(hf)
    functions = [m for m in members if inspect.isfunction(m[1])]
    for name, obj in functions:
        funcs.append(name)
    print(funcs)
list_functions()


data = pd.read_csv('pet_sales.csv')
hf.get_basic_info(data)


data['sales'] = data['sales'].replace('[$,]', '', regex=True)
data = data[data['pet_type'].str.contains('cat|dog|fish|bird') == True]
for column in data.columns:
    hf.set_type(data, column)
    # int, str, int, float, str, str, str, int, bool
    

hf.show_pie_chart(data, 're_buy', hf.my_fmt)
hf.count_plot(data, 'product_category', 're_buy')
hf.bar_plot(data, 'product_category', 're_buy', 'sales')
hf.bar_plot_comparison(data, 're_buy', 'pet_type', 'product_category')
