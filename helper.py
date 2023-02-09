from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import re


def get_basic_info(df):
    
    print(f'The dataframe has {len(df)} rows and {len(df.columns)} columns. Its columns and data types are:\n{df.dtypes}.')
    print(f"Here's a hint at what's to come: {df.head()}")


def data_replace(df, *args):

    """
    args[0] = 'sales'
    """

    df[args[0]] = df[args[0]].apply(lambda x: re.sub('[$,]', '', x))


def data_contains(df, column, *args):

    """
    args[0] = 'cat'
    args[1] = 'dog'
    args[2] = 'fish'
    args[3] = 'bird'
    """

    strings = args[:]
    delimiter = '|'
    result = delimiter.join(strings)
    df = df[df[column].str.contains(result) == True]
    return df


def set_type(df, column):
    
    var = input(f"How would you like to reset {column}'s column type?")
    df[column] = df[column].astype(var)


def my_fmt(x, total):
    
    return '{:.1f}% ({:.0f})'.format(x, total*x/100)


def show_pie_chart(df, column, my_fmt):
    
    count = df[column]
    v_counts = count.value_counts()
    total = len(count)

    fig = plt.figure(facecolor = 'black')
    plt.pie(v_counts, labels=v_counts.index, autopct = lambda x: my_fmt(x, total), shadow = True)
    plt.suptitle('Overall Count of Products Sold', color = 'white')
    plt.title('Product Sold More Than Once?', fontsize = 10, color = 'white')
    plt.show()


def count_plot(df, *args):

    """
    args[0] = 'product_category'
    args[1] = 're_buy'
    args[2] = True
    """

    names = df[args[0]].unique()
    new_data = df[df[args[1]] == args[2]]

    plot = sns.countplot(data = new_data, x = args[0], width = 0.8)
    plot.set_xticklabels(names, rotation = 90)
    plot.set(xlabel = 'Product', xticklabels = names, ylabel = 'Count', title = 'Count of Products Sold More Than Once')
    plot.tick_params(axis = 'x', colors = 'white')
    plot.tick_params(axis = 'y', colors = 'white')
    plot.set_xlabel('Product', color = 'white')
    plot.set_ylabel('Count', color = 'white')
    plot.title.set_color('white')
    plot.set_facecolor('black')

    plt.show()


def bar_plot(df, *args):

    """
    args[0] = 'product_category'
    args[1] = 're_buy'
    args[2] = 'sales'
    """

    plot = df.groupby([args[0], args[1]])[args[2]].sum().unstack().plot(kind = 'bar')
    plot.set_xlabel('Product', color = 'white')
    plot.set_ylabel('Sales', color = 'white')
    plot.set_title('Sales of Products Sold More Than Once', color = 'white')
    plot.tick_params(axis = 'x', colors = 'white')
    plot.tick_params(axis = 'y', colors = 'white')
    plot.set_facecolor('black')
    plt.ticklabel_format(axis = 'y', style = 'plain')
    plt.legend(loc = 'upper left', frameon = True)
    plt.show()


def bar_plot_comparison(df, *args):

    """
    args[0] = 're_buy'
    args[1] = 'pet_type'
    args[2] = 'product_category
    args[3] = 'cat' or 'dog' or 'fish' or 'bird'
    args[4] = 'False'
    args[5] = 'True'
    """

    false = df[(df[args[0]] == args[4]) & (df[args[1]] == args[3])]
    sales_false = false.groupby(args[2])[args[0]].count()
    true = df[(df[args[0]] == args[5]) & (df[args[1]] == args[3])]
    sales_true = true.groupby(args[2])[args[0]].count()

    df_pet = pd.DataFrame({args[4]: sales_false, args[5]: sales_true}).fillna(0).astype(int)
    fig_pet = df_cat.plot(kind = 'bar', xlabel = 'Product', ylabel = 'Count', title = f'{args[3]} Product Sold More Than Once')
    fig_pet.set_facecolor('black')
    fig_pet.set_xlabel('Product', color = 'white')
    fig_pet.set_ylabel('Count', color = 'white')
    fig_pet.tick_params(axis = 'x', colors = 'white')
    fig_pet.tick_params(axis = 'y', colors = 'white')
    fig_pet.set_title(f'{args[3].title()} Product Sold More Than Once', color = 'white')
    plt.legend(loc='upper left', frameon = True)

    plt.show()
