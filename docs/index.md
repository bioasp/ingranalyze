---
layout: index
title: ingranalyze
tagline: Influence graph analysis, consistency check, diagnosis, repair and prediction
---

### Sign Consistency on Influence Graphs - Diagnosis, Repair, Prediction 

For many biological systems knowledge bases are available that describe the interaction of its components usually in terms of causal networks and influence graphs.
In particular signed **influence graphs** where edges indicate either positive or negative effect of one node upon another.
Building upon a notion of consistency between biochemical/genetic regulations and high-throughput profiles of cell activity. We present an approach to check the consistency of large-scale data sets, provide explanations for inconsistencies by determining minimal representations of conflicts. In practice, this can be used to identify unreliable data or to indicate missing reactions. Further, we address the problem of repairing networks and corresponding yet often discrepant measurements in order to re-establish their mutual consistency and predict unobserved variations even under inconsistency. 

### Installation 

You can install ingranalyze by running:

	$ pip install --user ingranalyze

On Linux the executable script can then be found in ``~/.local/bin``

and on Mac OS the script is under ``/Users/YOURUSERNAME/Library/Python/3.6/bin``.

### Usage

Typical usage is:
	
	$ ingranalyze.py --mics --repair 5 networkfile observationfile


For more options you can ask for help as follows:
	
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



### Samples

Sample files for yeast are available here::
      [yeast_guelzim.net]( http://bioasp.github.io/downloads/samples/yeastdata/yeast_guelzim.net) [yeast_snf2.obs](http://bioasp.github.io/downloads/samples/yeastdata/yeast_snf2.obs)


### Related publications

* *Detecting Inconsistencies in Large Biological Networks with Answer Set Programming.* (2011). Theory and Practice of Logic Programming. [DOI](http://dx.doi.org/10.1007/978-3-540-89982-2_19)

* *Repair and Prediction (under Inconsistency) in Large Biological Networks with Answer Set Programming.* (2010). 12th International Conference on the Principles of Knowledge Representation and Reasoning.[DOI](http://aaai.org/ocs/index.php/KR/KR2010/paper/view/1334/1660)


### FAQ
**Q**: I don't have pip. How can I install pip without admin rights?

**A**: You can install pip without admin rights.

1. Download [getpip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py).

		$ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py

2. Install pip locally. 

		$ python get-pip.py --user

3. You can install using your local pip.

**Q**: I don't have pip. How can I install ingranalyze without pip?

**A**:  You can install ingranalyze without pip if you take care of the dependencies yourself.

1. Download [pyasp-1.3.3](https://pypi.python.org/pypi/pyasp/1.3.3). 
 
		$ wget https://pypi.python.org/packages/source/p/pyasp/pyasp-1.3.3.tar.gz

2. Extract and install pyasp. 

		$ gzip -d pyasp-1.3.3.tar.gz
		$ tar -xvf pyasp-1.3.3.tar
		$ cd pyasp-1.3.3
		$ python setup.py install --user

3. Download [ingranalyze-1.5.3](https://pypi.python.org/pypi/ingranalyze/1.5.3). 

		$ wget https://pypi.python.org/packages/source/i/ingranalyze/ingranalyze-1.5.3.tar.gz
 
4. Extract and install ingranalyze.

		$ gzip -d ingranalyze-1.5.3.tar.gz
		$ tar -xvf ingranalyze-1.5.3.tar
		$ cd ingranalyze-1.5.3
		$ python setup.py install --user
	

   The executable script can then be found in ``~/.local/bin`` on Linux and in ``/Users/YOURUSERNAME/Library/Python/2.7/bin``on Mac OS.
