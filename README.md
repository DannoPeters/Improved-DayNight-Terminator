# Improved-DayNight-Terminator
A day night terminator with atmospheric corrections (using NRLMSISE-00 2001 model of the atmosphere ported to python by Joshua Milas) and earth shape corrections (spheroidal)

Must install:

python3: 
numpy: pip install numpy
dateutil: pip install python-dateutil
NRLMSIS-00: pip install msise00
	If you recieve a fragmentation error such as "Fix your #egg=msise00 fragments" update the pip setup tool wheel using:
	pip install --upgrade pip setuptools wheel

Note if Pyhton 3 is NOT the default onyour system, you may need to run pyhton3 -m pip install ... otherwise dependencies will only be installed for your default python. Alternatively, if you are ready to amke the switch to pyhton 3, you can change your system default

