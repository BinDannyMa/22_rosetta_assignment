import os
import sys 


f_sum = open("README", "w")

os.mkdir("runs")
i = 0
while(i < 10):
  job_str = """#!/bin/bash                                                             
#SBATCH -t 12:00:00
#SBATCH -o out.txt
cd $WORK/rosetta/runs/"""+str(i)
  
  job_str += """\nAbinitioRelax.default.linuxgccrelease -in:file:native ../../1l2y.pdb -in:file:frag3 ../../aa1l2yA03_05.200_v1_3 -in:file:frag9 ../../aa1l2yA09_05.200_v1_3 -out:nstruct 100 -out:file:silent 1l2y_silent.out"""
  
  os.mkdir("runs/" + str(i))
  
  job_path = "runs/" + str(i) + "/" + str(i) + ".sh"
  f = open(job_path, "w")
  f.write(job_str)
  f.close()
  
  f_sum.write("sbatch " + job_path + "\n")
  
  i += 1
  
f_sum.close()
