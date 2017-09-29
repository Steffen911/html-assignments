densities = [ scipy.stats.gaussian_kde(X[:,j])
    for j in range(D) ]
xs = np.linspace(0,np.max(X),200)
for j in range(D):
    plt.plot(xs, densities[j](xs), label=j)
plt.legend(ncol=5)