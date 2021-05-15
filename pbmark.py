# Simple python script to benchmark your cpu

import timeit # timeit measures execution time of given code snippet(s)

"""
so basically our benchmarking script tries to do 0|1|2|3|4|5|6|7|8..... upto
99998 
"""

bmark_script='"|".join(str(i) for i in range(99999))'


print("Running CPU Benchmark.... ")
print("Please wait until the test ends...")

"""
The raw_score of the cpu is time taken by it to iterate the benchmarking script
1000 times in a row
"""

raw_score=round(timeit.timeit(bmark_script, number=1000), 0)

if raw_score>300:raw_score=300
elif raw_score<1:raw_score=1

"""
The criteria is self-explanatory
any pc taking 1 second or less would score 100
and any pc taking 300 seconds or more would score 1
"""
scoring_criteria={}
scores=[i for i in range (1,301)];c=0
for i in range(300,0,-1):
    scoring_criteria[scores[c]]=i; c+=1


pc_score=scoring_criteria[raw_score]
print(f"\nYour pc scored {round(pc_score/3,2)} points out of 100 ! ")

