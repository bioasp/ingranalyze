# Copyright (c) 2012, Sven Thiele <sthiele78@gmail.com>
#
# This file is part of ingranalyze.
#
# ingranalyze is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ingranalyze is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ingranalyze.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
import os

#some pretty printers for predictions, minimal inconsistent cores, etc

def print_predictions(predictions) :
    #predictions.sort()
    predictions = sorted(predictions, key=lambda p: str(p.arg(0)))
    exp = ''
    for p in predictions:
        if p.pred() == "vlabel" :
           if exp!=str(p.arg(0)) :
              print 'Experiment '+str(p.arg(0))+':'
              exp=str(p.arg(0))
           if p.arg(2)== "-1": print('   '+str(p.arg(1))+ ' = - ')
           if p.arg(2)== "1" : print('   '+str(p.arg(1))+ ' = + ')
           if p.arg(2)== "0" : print('   '+str(p.arg(1))+ ' = nc ')
        if p.pred() == "elabel" :
           if p.arg(2) == "-1" : print '   '+str(p.arg(0))+' -> '+str(p.arg(1))+' -'
           if p.arg(2) == "1"  : print '   '+str(p.arg(0))+' -> '+str(p.arg(1))+' +'
                  
def print_mic(mic, net, obs):
  
    nodes = []
    edges = []
    for node in mic: nodes.append(str(node.arg(1)))
    
    predecessors = []
    for e in net:
       if e.pred() == "obs_elabel" :
          #print str(e)
          #print str(e.arg(0)),str(e.arg(1)),str(e.arg(2))
          if str(e.arg(1)) in nodes : 
            predecessors.append(str(e.arg(0)))
            if str(e.arg(2)) == "1" : edges.append( str(e.arg(0))+ " -> " + str(e.arg(1))+ " +")
            if str(e.arg(2)) == "-1" : edges.append(str(e.arg(0))+ " -> " + str(e.arg(1))+ " -")
         #TODO ? edges
    for edge in edges: print('   '+edge)
    for o in obs:
       if o.pred() == "obs_vlabel" :  
          if str(o.arg(1)) in nodes :
              if str(o.arg(2))=="1" :  print '   '+str(o.arg(1))+ " = +"
              if str(o.arg(2))=="-1" :  print '   '+str(o.arg(1))+ " = -"
          if str(o.arg(1)) in predecessors :
              if str(o.arg(2))=="1" :  print '   '+str(o.arg(1))+ " = +"
              if str(o.arg(2))=="-1" :  print '   '+str(o.arg(1))+ " = -"
    

def clean_up() :
  if os.path.isfile("parser.out"): os.remove("parser.out")
  if os.path.isfile("asp_py_lextab.py"): os.remove("asp_py_lextab.py")
  if os.path.isfile("asp_py_lextab.pyc"): os.remove("asp_py_lextab.pyc")
  if os.path.isfile("asp_py_parsetab.py"): os.remove("asp_py_parsetab.py")
  if os.path.isfile("asp_py_parsetab.pyc"): os.remove("asp_py_parsetab.pyc") 
  if os.path.isfile("graph_parser_lextab.py"): os.remove("graph_parser_lextab.py")
  if os.path.isfile("graph_parser_lextab.pyc"): os.remove("graph_parser_lextab.pyc")  
  if os.path.isfile("graph_parser_parsetab.py"): os.remove("graph_parser_parsetab.py")
  if os.path.isfile("graph_parser_parsetab.pyc"): os.remove("graph_parser_parsetab.pyc")

def m_quit() :  
  clean_up()
  quit()