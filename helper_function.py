from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


def get_basic_info(df):
    print(f'The dataframe has {len(df)} rows and {len(df.columns)} columns. Its columns and data types are:\n{df.dtypes}.')
    print(f"Here's a hint at what's to come: {df.head()}")


def set_type(df, column):
    var = input(f"How would you like to reset {column}'s column?")
    df[column] = df[column].astype(var)


def my_fmt(x, total):
    return '{:.1f}% ({:.0f})'.format(x, total*x/100)


def show_pie_chart(df, column, my_fmt):
    purchases = df[column]
    v_counts = purchases.value_counts()
    total = len(purchases)

    fig = plt.figure(facecolor='black')
    plt.pie(v_counts, labels=v_counts.index, autopct=lambda x: my_fmt(x, total), shadow=True)
    plt.suptitle('Overall Count of Products Sold', color='white')
    plt.title('Product Sold More Than Once?', fontsize=10, color='white')
    # plt.gca().axis('equal')
    # plt.gca().set_xticklabels([], color='white')
    # plt.gca().set_yticklabels([], color='white')
    plt.show()

    # plt.pie(v_counts, labels=v_counts.index, autopct = lambda x: my_fmt(x, total), shadow=True)

    # plt.suptitle('Overall Count of Products Sold')
    # plt.title('Product Sold More Than Once?', fontsize=10)
    # plt.set_facecolor('white')
    # plt.tick_params(axis='x', colors='white')
    # plt.tick_params(axis='y', colors='white')
    # plt.set_xlabel('Product', color='white')
    # plt.set_ylabel('Count', color='white')
    # plt.title.set_color('white')

    # plt.show()


def count_plot(df, *args):

    """
    args[0] = 'product_category'
    args[1] = 're_buy'
    """

    names = df[args[0]].unique()
    new_data = df[df[args[1]] == True]

    plot_2 = sns.countplot(data = new_data, x = args[0], width = 0.8)
    plot_2.set_xticklabels(names, rotation = 90)
    plot_2.set(xlabel = 'Product', xticklabels = names, ylabel = 'Count', title = 'Count of Products Sold More Than Once')
    plot_2.tick_params(axis='x', colors='white')
    plot_2.tick_params(axis='y', colors='white')
    plot_2.set_xlabel('Product', color='white')
    plot_2.set_ylabel('Count', color='white')
    plot_2.title.set_color('white')
    plot_2.set_facecolor('black')

    plt.show()


def bar_plot(df, *args):

    """
    args[0] = 'product_category'
    args[1] = 're_buy'
    args[2] = 'sales'
    """

    sales_1 = df.groupby([args[0], args[1]])[args[2]].sum().unstack().plot(kind = 'bar')
    sales_1.set_xlabel('Product', color='white')
    sales_1.set_ylabel('Sales', color='white')
    sales_1.set_title('Sales of Products Sold More Than Once', color='white')
    sales_1.tick_params(axis='x', colors='white')
    sales_1.tick_params(axis='y', colors='white')
    sales_1.set_facecolor('black')
    plt.ticklabel_format(axis='y', style='plain')
    plt.legend(loc='upper left', frameon=False)
    plt.show()

    # sales_1.set(xlabel = 'Product', ylabel = 'Sales', title = 'Sales of Products Sold More Than Once')

    # plt.ticklabel_format(axis = 'y', style = 'plain')
    # plt.tick_params(axis='x', colors='white')
    # plt.tick_params(axis='y', colors='white')
    # plt.set_xlabel('Product', color='white')
    # plt.set_ylabel('Count', color='white')
    # plt.title.set_color('white')
    # plt.legend(loc = 'upper left', frameon = False)
    # plt.show()


def bar_plot_comparison(df, *args):

    """
    args[0] = 're_buy'
    args[1] = 'pet_type'
    args[2] = 'product_category
    """

    plot_0_false_cat = df[(df[args[0]] == False) & (df[args[1]] == 'cat')]
    sales_0_plot_cat = plot_0_false_cat.groupby(args[2])[args[0]].count()
    plot_1_true_cat = df[(df[args[0]] == True) & (df[args[1]] == 'cat')]
    sales_1_plot_cat = plot_1_true_cat.groupby(args[2])[args[0]].count()

    df_cat = pd.DataFrame({'False': sales_0_plot_cat, 'True': sales_1_plot_cat}).fillna(0).astype(int)
    fig_cat = df_cat.plot(kind = 'bar', xlabel = 'Product', ylabel = 'Count', title = 'Cat Product Sold More Than Once')
    # fig_cat = df_cat.plot(kind='bar', color='white', edgecolor='white')
    fig_cat.set_facecolor('black')
    fig_cat.set_xlabel('Product', color='white')
    fig_cat.set_ylabel('Count', color='white')
    fig_cat.tick_params(axis='x', colors='white')
    fig_cat.tick_params(axis='y', colors='white')
    fig_cat.set_title('Cat Product Sold More Than Once', color='white')

    plot_0_false_dog = df[(df[args[0]] == False) & (df[args[1]] == 'dog')]
    sales_0_plot_dog = plot_0_false_dog.groupby(args[2])[args[0]].count()
    plot_1_true_dog = df[(df[args[0]] == True) & (df[args[1]] == 'dog')]
    sales_1_plot_dog = plot_1_true_dog.groupby(args[2])[args[0]].count()

    df_dog = pd.DataFrame({'False': sales_0_plot_dog, 'True': sales_1_plot_dog}).fillna(0).astype(int)
    fig_dog = df_dog.plot(kind = 'bar', xlabel = 'Product', ylabel = 'Count', title = 'Dog Product Sold More Than Once')
    fig_dog.set_facecolor('black')
    fig_dog.set_xlabel('Product', color='white')
    fig_dog.set_ylabel('Count', color='white')
    fig_dog.tick_params(axis='x', colors='white')
    fig_dog.tick_params(axis='y', colors='white')
    fig_dog.set_title('Dog Product Sold More Than Once', color='white')

    plot_0_false_fish = df[(df[args[0]] == False) & (df[args[1]] == 'fish')]
    sales_0_plot_fish = plot_0_false_fish.groupby(args[2])[args[0]].count()
    plot_1_true_fish = df[(df[args[0]] == True) & (df[args[1]] == 'fish')]
    sales_1_plot_fish = plot_1_true_fish.groupby(args[2])[args[0]].count()

    df_fish = pd.DataFrame({'False': sales_0_plot_fish, 'True': sales_1_plot_fish}).fillna(0).astype(int)
    fig_fish = df_fish.plot(kind = 'bar', xlabel = 'Product', ylabel = 'Count', title = 'Fish Product Sold More Than Once')
    fig_fish.set_facecolor('black')
    fig_fish.set_xlabel('Product', color='white')
    fig_fish.set_ylabel('Count', color='white')
    fig_fish.tick_params(axis='x', colors='white')
    fig_fish.tick_params(axis='y', colors='white')
    fig_fish.set_title('Fish Product Sold More Than Once', color='white')

    plot_0_false_bird = df[(df[args[0]] == False) & (df[args[1]] == 'bird')]
    sales_0_plot_bird = plot_0_false_bird.groupby(args[2])[args[0]].count()
    plot_1_true_bird = df[(df[args[0]] == True) & (df[args[1]] == 'bird')]
    sales_1_plot_bird = plot_1_true_bird.groupby(args[2])[args[0]].count()

    df_bird = pd.DataFrame({'False': sales_0_plot_bird, 'True': sales_1_plot_bird}).fillna(0).astype(int)
    fig_bird = df_bird.plot(kind = 'bar', xlabel = 'Product', ylabel = 'Count', title = 'Bird Product Sold More Than Once')
    fig_bird.set_facecolor('black')
    fig_bird.set_xlabel('Product', color='white')
    fig_bird.set_ylabel('Count', color='white')
    fig_bird.tick_params(axis='x', colors='white')
    fig_bird.tick_params(axis='y', colors='white')
    fig_bird.set_title('Bird Product Sold More Than Once', color='white')

    plt.show()