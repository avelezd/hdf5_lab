import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def plot_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()


if __name__ == "__main__":
    # viridis = cm.get_cmap('viridis', 8)
    # print(viridis)
    # breakpoint()
    # cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
    
    ltcolors = ['#ffffff']
    for colhex in range(0,254):
        
        hexstr = hex(colhex).replace('0x','')
        
        if len(hexstr) == 1:
            hexstr = '0%s'%hexstr
        
        rgbstr = '#%s0000'%hexstr
        ltcolors.append(rgbstr)

    # print(ltcolors)
    # cmap = ListedColormap(["#550011", "#882211", "#005599", "#775566"])
    cmap = ListedColormap(ltcolors)
    plot_examples([cmap])
