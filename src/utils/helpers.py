
import matplotlib.pyplot as plt

def plot_series(df, columns=['Close']):
    df[columns].plot(figsize=(10,5))
    plt.show()
