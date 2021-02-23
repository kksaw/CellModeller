import random
from CellModeller.Regulation.ModuleRegulator import ModuleRegulator
from CellModeller.Biophysics.BacterialModels.CLBacterium import CLBacterium
from CellModeller.GUI import Renderers
import numpy
from math import *

cell_lens = 3.0
cell_growr = 2.0
gridsize = 100
dist = 20
rad = 5.0

def setup(sim):
    # Set biophysics, signalling, and regulation models
    biophys = CLBacterium(sim, jitter_z=True, gamma = 20, max_planes=5, max_cells=500000)
    biophys.addPlane((0,0,0),(0,0,1),1.0) #base plane
    biophys.addPlane((gridsize/2,0,0),(-1,0,0), 1.0)
    biophys.addPlane((-gridsize/2,0,0),(1,0,0), 1.0)
    biophys.addPlane((0,gridsize/2,0),(0,-1,0), 1.0)
    biophys.addPlane((0,-gridsize/2,0),(0,1,0), 1.0)

    # use this file for reg too
    regul = ModuleRegulator(sim, sim.moduleName)	
    # Only biophys and regulation
    sim.init(biophys, regul, None, None)
 
    # Specify the initial cell and its location in the simulation
    sim.addPillars(dist, gridsize, rad)
    sim.addLawn(gridsize, cell_lens, 1.1)
    
    # Add some objects to draw the models
    therenderer = Renderers.GLBacteriumRenderer(sim)
    sim.addRenderer(therenderer)
    sim.pickleSteps = 20

def init(cell):
    # Specify mean and distribution of initial cell size
    cell.targetVol = cell_lens + random.uniform(0.0,0.5)
    # Specify growth rate of cells
    cell.growthRate = cell_growr
    cell.color = (0.0,1.0,0.0)

def update(cells):
    #Iterate through each cell and flag cells that reach target size for division
    for (id, cell) in cells.iteritems():
        if cell.volume > cell.targetVol:
            cell.divideFlag = True

def divide(parent, d1, d2):
    # Specify target cell size that triggers cell division
    d1.targetVol = cell_lens + random.uniform(0.0,0.5)
    d2.targetVol = cell_lens + random.uniform(0.0,0.5)

