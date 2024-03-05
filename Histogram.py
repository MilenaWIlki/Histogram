# Plot histogram of a column in the dataset
def plot_histogram(dataset, column):
    dataset[column].plot.hist()
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

# Example usage:
plot_histogram(dataset, 'column_name')
