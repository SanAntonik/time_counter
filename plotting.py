import matplotlib.pyplot as plt
import seaborn as sns


# plot mean, mean+-standart deviation
def mean_std(ax, mean, std):
    ax.axhline(y=mean-std, color='k', linestyle='-')
    ax.axhline(y=mean, color='r', linestyle='-', label="mean")
    ax.axhline(y=mean+std, color='k', linestyle='-', label="mean+-std")


def plot_data(df, mean, std, month):
    ax = sns.barplot(x="Day", y="Total", data=df, hue="Kind", dodge=False)
    mean_std(ax, mean, std)
    plt.title(month)
    plt.legend()
    plt.show()
