# Unsupervised dimension reduction on a sequence of covariance matrices

Python code for dimension reduction in papaer: Analyzing Dynamical Brain Functional Connectivity As Trajectories on Space of Covariance Matrices, IEEE Transactions on Medical Imaging, TMI.2019.2931708. 

link: https://arxiv.org/abs/1904.05449

The propsed unsupervised dimension reduction method can bring a sequence of symmetric and positive-definite matrices to arbitrary lower dimensions, while preserving the relevant distances between the original matrices as much as possible. The matrices in the resulting sequence in lower dimension have the symmetric and positive-definite structure preserved.


# Prerequisities
Pymanopt: package for optimization on manifolds. See https://pymanopt.github.io/ for details.

Install: pip install --user pymanopt

# Usage
The input matrix is a 4d ndarray with shape (n,n,T,L), where the dimension of covariance matrices is n by n, T is the number of matrices in a sequence, and L is the number of covariance sequences. The resulting ndarray has shape (m,m,T,L), where m < n.

For dimension reduction: python main.py --covseqs_dir xx --m xx

covseqs_dir: file location of original sequences; m: target lower dimension

The default solver in the code is Trustregion, while user can use other solvers for fun. In Pymanopt package, user can define the stopping criteria for the task, by changing maxtime, maxiter, mingradnorm, minstepsize and maxcostevals in solver.py. Usually using a small maxiter and a fixed random seed are enough for getting meaningful results.

For distance calculation between covariance matrices, please see cov_dist.py.






