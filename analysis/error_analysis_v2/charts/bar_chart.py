import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def generate_bar_chart(legend, values, title, path):

    y_pos = np.arange(len(legend))

    plt.figure(figsize=(20.56, 8.00))

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, legend)
    plt.ylabel('% błędu > 2.0')
    plt.title(title)

    plt.savefig(path)
    plt.close(plt.gcf())
