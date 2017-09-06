import thinkstats2
import thinkplot
import pandas as pd
import numpy as np
import nsfg

resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
print("actual pmf ", pmf)
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
                                
    new_pmf.Normalize()
    return new_pmf
bias_pmf = BiasPmf(pmf, 'biased')
print("bias pmf", bias_pmf)
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, bias_pmf])
thinkplot.Show(xlabel='Number of children', ylabel='PMF')
print("actual pmf mean", pmf.Mean())
print("biased pmf mean", bias_pmf.Mean())
