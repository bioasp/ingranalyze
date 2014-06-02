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
import tempfile
from pyasp.asp import *

root = __file__.rsplit('/', 1)[0]

guess_inputs_prg = root + '/encodings/pm_guess_inputs.gringo'

consistency_prg = root + '/encodings/pm_consistency.gringo'
prediction_prg = root + '/encodings/pm_prediction.gringo'
explanation_prg = root + '/encodings/explanation.gringo'
mic_prg = root + '/encodings/pm_mic.gringo'
dyn_mic_prg = root + '/encodings/dynamic_diagnosis.gringo'
reduction_prg = root + '/encodings/reduction.lp'

repair_options_prg =     root + '/encodings/compute_repair_options.gringo'
repair_core_prg =        root + '/encodings/repair_core.gringo'
prediction_core_prg =    root + '/encodings/prediction_core.gringo'
repair_cardinality_prg = root + '/encodings/repair_cardinality.gringo'
repair_subset_prg  =     root + '/encodings/repair_subset.gringo'

def is_consistent(instance):
    '''
    [is_consistent(instance)] returns [True] if there exists a consistent extension
    to the system described by the TermSet object [instance].
    '''
    return get_consistent_labelings(instance,1) != []
    

def get_consistent_labelings(instance,nmodels=0,exclude=[]):
    '''
    [consistent_labelings(instance,nmodels,exclude)] returns a list containing
    [nmodels] TermSet objects representing consistent extensions of the system
    described by the TermSet [instance]. The list [exclude] should contain TermSet objects
    representing (maybe partial) solutions that are to be avoided. If [nmodels] equals [0]
    then the list contain all feasible models.
    '''
    #inputs = get_reductions(instance)
    inst = instance.to_file()
    prg = [ consistency_prg, inst, exclude_sol(exclude) ]
    co= str(nmodels)
    solver = GringoClasp(clasp_options=co)
    models = solver.run(prg)
    os.unlink(inst)
    os.unlink(prg[2])
    return models
   
    
#def get_minimal_inconsistent_cores(instance,nmodels=0,exclude=[]):
    #'''
    #[compute_mic(instance,nmodels,exclude)] returns a list containing
    #[nmodels] TermSet objects representing subset minimal inconsistent cores of the system
    #described by the TermSet [instance]. The list [exclude] should contain TermSet objects
    #representing (maybe partial) solutions that are to be avoided. If [nmodels] equals [0]
    #then the list contain all feasible models.
    #'''
    #inputs = get_reductions(instance)
    #prg = [ mic_prg, inputs.to_file(), instance.to_file(), exclude_sol(exclude) ] 
    #options=' --heuristic=Vmtf'
    #solver = GringoClaspD(options)
    #models = solver.run(prg,nmodels)
    #os.unlink(prg[1])
    #os.unlink(prg[2])
    #os.unlink(prg[3])
    #return models[0]

def get_minimal_inconsistent_cores(instance,nmodels=0,exclude=[]):
    '''
    [compute_mic(instance,nmodels,exclude)] returns a list containing
    [nmodels] TermSet objects representing subset minimal inconsistent cores of the system
    described by the TermSet [instance]. The list [exclude] should contain TermSet objects
    representing (maybe partial) solutions that are to be avoided. If [nmodels] equals [0]
    then the list contain all feasible models.
    '''
    inputs = get_reductions(instance)
    prg = [ dyn_mic_prg, inputs.to_file(), instance.to_file(), exclude_sol(exclude) ] 
    options='--heuristic=Vmtf '+str(nmodels)
    solver = GringoClasp(clasp_options=options)
    models = solver.run(prg, collapseTerms=True, collapseAtoms=False)
    os.unlink(prg[1])
    os.unlink(prg[2])
    os.unlink(prg[3])
    return models

def guess_inputs(instance):
    prg = [ guess_inputs_prg, instance.to_file() ]
    solver = GringoClasp()
    models = solver.run(prg, collapseTerms=True, collapseAtoms=False)
    os.unlink(prg[1])
    assert(len(models) == 1)
    return models[0]

def get_reductions(instance):
    prg = [ reduction_prg, instance.to_file() ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[1])
    assert(len(models) == 1)
    return models[0]


def get_repair_options_flip_obs(instance):
    repair_mode = String2TermSet('repair_v')
    instance2 = instance.union(repair_mode)
    prg = [ instance2.to_file(), repair_options_prg ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[0])    
    return models[0]
    

def get_repair_options_flip_edge(instance):
    repair_mode = String2TermSet('repair_e')
    instance2 = instance.union(repair_mode)
    prg = [ instance2.to_file(), repair_options_prg ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[0])    
    return models[0]

def get_repair_options_make_node_input(instance):
    repair_mode = String2TermSet('repair_g')
    instance2 = instance.union(repair_mode)
    prg = [ instance2.to_file(), repair_options_prg ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[0])    
    return models[0]
    
      
def get_repair_options_make_obs_input(instance):
    repair_mode = String2TermSet('repair_i')
    instance2 = instance.union(repair_mode)
    prg = [ instance2.to_file(), repair_options_prg ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[0])    
    return models[0]
    
def get_repair_options_add_edges(instance):
    repair_mode = String2TermSet('repair_a')
    instance2 = instance.union(repair_mode)
    prg = [ instance2.to_file(), repair_options_prg ]
    solver = GringoClasp()
    models = solver.run(prg)
    os.unlink(prg[0])    
    return models[0]


def get_minimum_of_repairs(instance,repair_options,exclude=[]):
    #inputs = get_reductions(instance)
    #instance2 = instance.union(inputs)
    inst = instance.to_file()
    repops = repair_options.to_file()
    prg = [ inst, repops, exclude_sol(exclude), repair_core_prg, repair_cardinality_prg ]

    solver = GringoClasp()
    optimum = solver.run(prg)
    os.unlink(inst)
    os.unlink(repops)
    os.unlink(prg[2]) 
    return optimum[0]


def get_minimal_repair_sets(instance, repair_options ,optimum,nmodels=0,exclude=[]):
    #inputs = get_reductions(instance)
    #instance2 = instance.union(inputs)
    inst = instance.to_file()
    repops = repair_options.to_file()
    prg = [ inst, repops, exclude_sol(exclude), repair_core_prg, repair_cardinality_prg ]

    options='--project --opt-mode=optN '+str(nmodels)
    solver = GringoClasp(clasp_options=options)
    models = solver.run(prg, collapseTerms=True, collapseAtoms=False)
    os.unlink(inst)
    os.unlink(repops)
    os.unlink(prg[2])
    return models
    
     
def get_predictions_under_minimal_repair(instance, repair_options, optimum):
    '''
    Computes the set of signs on edges/vertices that can be cautiously
    derived from [instance], minus those that are a direct consequence
    of obs_[ev]label predicates
    '''
    #inputs = get_reductions(instance)
    #instance2 = instance.union(inputs)
    inst = instance.to_file()
    repops = repair_options.to_file()    
    prg = [ inst, repops, prediction_core_prg, repair_cardinality_prg ]

    options='--project --enum-mode cautious --opt-mode=optN --opt-bound='+str(optimum)
    solver = GringoClasp(clasp_options=options)
    models = solver.run(prg, collapseTerms=True, collapseAtoms=False)
    os.unlink(inst)
    os.unlink(repops)
    return whatsnew(instance,models[0])


def cut_obs_(s):
    return str(s)[4:]

def whatsnew(instance,pred):
    '''
    [whatsnew(instance,pred)] is a TermSet equal to [pred] where all predicates
    vlabel and elabel which have a corresponding obs_vlabel and obs_elabel in
    [instance] have been deleted. This function is meant to see which of the invariants
    are not a direct consequence of the observations.
    '''
    accu = TermSet(pred)
    for t in instance:

        if t.pred() == 'obs_vlabel':
            [_,e,v,s] = t.explode()
            accu.discard(Term('vlabel',[e,v,s]))
        elif t.p('obs_elabel'):
            [_,j,i,s] = t.explode()
            accu.discard(Term('elabel',[j,i,s]))
    return accu


def get_predictions_under_consistency(instance):
    '''
    Computes the set of signs on edges/vertices that can be cautiously
    derived from [instance], minus those that are a direct consequence
    of obs_[ev]label predicates
    '''
    #inputs = get_reductions(instance)
    inst = instance.to_file()
    prg = [ prediction_prg, inst, exclude_sol([]) ]
    solver = GringoClasp(clasp_options='--project --enum-mode cautious')
    models = solver.run(prg, collapseTerms=True, collapseAtoms=False)
    os.unlink(inst)
    os.unlink(prg[2])
    return whatsnew(instance,models[0])
    