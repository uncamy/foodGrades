import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm as cm
from matplotlib import mlab as ml

# ----------
# Example 1
# ----------

NPOINTS = 1000

np.random.seed(101)
lat = np.random.random(NPOINTS)*8+44
lon = np.random.random(NPOINTS)*100-50
counts = np.random.randint(0, 1000, NPOINTS)

plt.subplot(211)
plt.scatter(lat, lon, c=counts)
plt.colorbar()
plt.subplot(212)
plt.scatter(lat, lon, s=counts)

plt.savefig('scatter_example.png')
plt.show()


# ----------
# Example 2
# ----------

# Generate some test data
x = np.random.randn(8873)
y = np.random.randn(8873)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=(512, 384))
# bins are dimentions of the heatmap
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap, extent=extent)
plt.show()


# ----------
# Example 3
# ----------

data = np.genfromtxt('csv_file', dtype=None, delimiter=',')
M = np.random.rand(209).reshape(11, 19)
M.shape
# returns: (11, 19)
# if the array returned from your call to 'genfromtxt'
# is not 11 x 19,
# then you need to reshape it so that it is,
# use, e.g., 'data.reshape(11, 19)'


fig = plt.figure()
ax1 = fig.add_subplot(111)

# 'gray_r' refers to the particular matplotlib color map
# i chose 'r' just means 'reverse'
# so that '0' is white;
# there are quite a few color maps in matplotlib
# use dir(matplotlib.cm) to get a list of the installed colormaps

# select the color map
cmap = cm.get_cmap('gray_r', 10)

# map the colors/shades to your data
ax1.imshow(M, interpolation="nearest", cmap=cmap)

# plot it
plt.show()


# ----------
# Example 4
# ----------

n = 1e5
x = y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z1 = ml.bivariate_normal(X, Y, 2, 2, 0, 0)
Z2 = ml.bivariate_normal(X, Y, 4, 1, 1, 1)
ZD = Z2 - Z1
x = X.ravel()
y = Y.ravel()
z = ZD.ravel()
gridsize = 30
plt.subplot(111)

# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default)
# then the result is a pure 2D histogram

plt.hexbin(x, y, C=z, gridsize=gridsize, cmap=cm.jet, bins=None)
plt.axis([x.min(), x.max(), y.min(), y.max()])

cb = plt.colorbar()
cb.set_label('mean value')
plt.show()
