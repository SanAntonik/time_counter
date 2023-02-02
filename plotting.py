import matplotlib.pyplot as plt
import seaborn as sns


# plot mean, mean+-standart deviation
def mean_std(ax, mean, std):
    ax.axhline(y=mean-std, color='k', linestyle='-')
    ax.axhline(y=mean, color='r', linestyle='-', label="mean")
    ax.axhline(y=mean+std, color='k', linestyle='-', label="mean+-std")


def plot_data(df, mean, std, month):
    # another possible approach for handling day offs is to think
    # that every day with total lower than mean-std is a day off
    colours = {"work": "#4a69bd", "relax": "#f6b93b"}
    ax = sns.barplot(x="Day", y="Total", data=df,
                     hue="DKind", dodge=False, palette=colours)
    mean_std(ax, mean, std)
    plt.title(f"{month} - study time per day")
    ax.set_ylabel("Study Total in Minutes")
    ax.set_xlabel("Day of the Month")
    plt.legend()
    plt.show()
