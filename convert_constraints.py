# tool for converting enzyme design constraints into regular constraints 

from subprocess import check_output 
import os 
from sys import argv 

run_dir = argv[1] 

# error handling 

if len( argv ) < 2:
  print( 'use: python convert_constraints.py <run directory> (see readme.md)' )
  exit()

if not os.path.isdir( run_dir ): 
  print( 'No such directory:', run_dir ) 
  exit()

if not os.path.isfile( run_dir + 'sub.sh' ):
  print( 'No file `sub.sh` found in run directory', run_dir ) 
  exit() 

# algorithm 

print( 'Running Rosetta (may take a minute or two!)' ) 
os.chdir( run_dir ) 
cmd = [ 'bash', 'sub.sh' ] 
text_out = str( check_output( cmd ) ) 
os.chdir( '..' ) 

print( 'Generating a regular contraint file' ) 
for line in text_out.splitlines():
  line = line[ 37: ] # removes tracer leader 
  if '---' in line or 'constraints' in line: 
    print( '#', line ) # comment out comment lines 
  else:
    print( line ) # output is regular constraint file 
