from PyGMO import *
from _analysis import analysis
from my_module import my_problem
from numpy import *
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

prob=problem.himmelblau()
anal=analysis(prob)
anal.sample(1000)
anal.get_local_extrema()
anal.cluster_local_extrema()
anal.plot_local_cluster_pcp(together=True)
anal.plot_local_cluster_pcp(together=False)