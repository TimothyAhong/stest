__author__ = 'Tim'
import matplotlib.pyplot as plt


def plot_volume_comparison(headers, volume_comparison_rows):
    x = range(len(volume_comparison_rows))
    for index, header_name in enumerate(headers):
        #TODO this is sketchy way of making sure that we dont have the mode (_standing) going to the plot
        if header_name != 'mode':
            volume_column = [
                volume_row[index] for volume_row in volume_comparison_rows
            ]
            plt.plot(x,volume_column, label=header_name)
    plt.show()

