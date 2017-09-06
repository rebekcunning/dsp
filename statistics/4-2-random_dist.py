import numpy as np
import pandas as pd
import thinkstats2
import thinkplot

sample = np.random.random(1000)
sample_pmf = thinkstats2.Pmf(sample, label='pmf')
sample_cdf = thinkstats2.Cdf(sample, label='cdf')

thinkplot.Cdf(sample_cdf)
thinkplot.Show(xlabel='percentile rank', ylabel='CDF')

thinkplot.Pmf(sample_pmf)
thinkplot.Show(xlabel='number', ylabel='PMF')
