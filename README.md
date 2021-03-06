# Unsupervised dimension reduction on a sequence of covariance matrices

Python code for dimension reduction in papaer: Analyzing Dynamical Brain Functional Connectivity As Trajectories on Space of Covariance Matrices, IEEE Transactions on Medical Imaging, TMI.2019.2931708. 

link: https://arxiv.org/abs/1904.05449

The propsed unsupervised dimension reduction method can bring a sequence of n by n symmetric and positive-definite matrices to arbitrary lower dimensions (m by m, m < n), while preserving the relevant distances between the original matrices as much as possible. The matrices in the resulting sequence in lower dimension have the symmetric and positive-definite structure preserved. Following are two examples from the paper:

Pairwised distances between simulated covariance matrices with n = 100 (a) and after reducing dimensions to m = 20 (b), 10 (c) and 5 (d):
![Dimension reduction of simulated covariance matrices](https://github.com/dzld00/unsupervised-cov-sequence-dim-reduction/blob/master/images/sim1.png)

Visualization of brain functional connectivities using precision matrices estimated by reconstructed SPDMs from different dimensions:
![Reconstructed connectivities](https://github.com/dzld00/unsupervised-cov-sequence-dim-reduction/blob/master/images/sim2.png)

In the paper, n was set to 100 in simulations in comparison with the amount of brain ROIs. However, the proposed method is still useful when n is much larger. 

# Dependency
Pymanopt: python package for optimization on manifolds. See https://pymanopt.github.io/ for details.

Install: pip install --user pymanopt

# Usage
The input matrix is a 4d ndarray with shape (n,n,T,L), where the dimension of covariance matrices is n by n, T is the number of matrices in a sequence, and L is the number of covariance sequences. The resulting ndarray has shape (m,m,T,L), where m < n.

For dimension reduction: python main.py --covseqs_dir xx --m xx

covseqs_dir: file location of original sequences; m: target lower dimension

The default solver in the code is Trustregion, while user can use other solvers for fun. In Pymanopt package, user can define the stopping criteria for the task, by changing maxtime, maxiter, mingradnorm, minstepsize and maxcostevals in solver.py. Usually using a small maxiter and a fixed random seed are enough for getting meaningful results.

For distance calculation between covariance matrices, please see cov_dist.py.






