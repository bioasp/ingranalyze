Installation
============

You can install ingranalyze by running::

	$ pip install --user ingranalyze

The executable scripts can then be found in ~/.local/bin.


Usage
=====

Typical usage is::

	$ ingranalyze.py --mics --repair 5 networkfile observationfile

For more options you can ask for help as follows::

	$ ingranalyze.py -h 
	usage: ingranalyze.py [-h] [--mics] [--repair {1,2,3,4,5}] [--list_repairs] networkfile observationfile                                                          
  
	positional arguments:                                                                                      
	  networkfile           influence graph in bioquali format                                                 
	  observationfile       observations in bioquali format                                                    
  
	optional arguments:                                                                                        
	  -h, --help            show this help message and exit                                                    
	  --mics                compute minimal inconsistent cores
	  --repair {1,2,3,4,5}  choose repair method: 1 flip observed variations, 2
	                        flip influences, 3 define network nodes as inputs, 4
	                        define network nodes as input in an experiment (use
	                        only in case of multiple experiments), 5 add
	                        influences. default is 3
	  --list_repairs        compute all minimal repair sets


Samples
=======

Sample files for yeast are available here::
      yeast_guelzim.net_ yeast_snf2.obs_

.. _yeast_guelzim.net: http://bioasp.github.io/downloads/samples/yeastdata/yeast_guelzim.net
.. _yeast_snf2.obs: http://bioasp.github.io/downloads/samples/yeastdata/yeast_snf2.obs
