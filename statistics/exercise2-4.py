import thinkstats2
import nsfg
import thinkplot
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1, group2):
    print("mean for firsts", group1.mean())
    print("mean for others", group2.mean())
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2)/(n1 + n2)
    d = diff/ math.sqrt(pooled_var)
    return d

print("Cohen's d", CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
