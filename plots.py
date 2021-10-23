import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


class Plot():

    def draw_plot(self, x, y):
        data = pd.io.json.read_json('https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json')
        plt.scatter(data[x], data[y])
        plt.savefig('plots/plot_' + x + '_' + y + '.png')
        return Path('plots/plot_' + x + '_' + y + '.png').absolute()


if __name__ == '__main__':
    ex = Plot()
    ex.draw_plot('min', 'mean')
