#simple python script to benchmark your cpu

import timeit

bmark_script='"|".join(str(i) for i in range(99999))'
print("Running CPU Benchmark.... ")
print("Please wait until the test ends...")

raw_score=round(timeit.timeit(bmark_script, number=1000), 0)
if raw_score>201:raw_score=201
elif raw_score<1:raw_score=1

scoring_criteria={}
scores=[i for i in range (1,201)];c=0
for i in range(200,0,-1):
    scoring_criteria[scores[c]]=i; c+=1

print(scoring_criteria)
pc_score=scoring_criteria[raw_score]
print(f"Your pc scored {pc_score/2} points out of 100 ! ")
