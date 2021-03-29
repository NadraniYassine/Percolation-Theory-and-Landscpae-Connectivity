# Percolation-Theory-and-Landscpae-Connectivity
## Introduction
The extent to which an ecosystem can be interconnected is a determining factor in the different species survival in fragmented landscapes. Therefore, understanding how ecological connectivity is changing is important in order to maintaining an ecosystem's biodiversity.

Rising sea levels are a major threat to coastal ecosystems and islands biodiversity, the rate of exploitable land will decrease considerably. My work is an attempt to analyze and understand the ecological fragmentation phenomenon and its effects on species migration.
## Major points
• Mathematical model to simulate the ecological fragmentation phenomenon.

• Demonstration and analysis of the phase transition behaviour

• Numerical determination of the percolation threshold

• Verification of the consistency of the results obtained of the theoretical data

### Mathematical approach
The Percolation Theory is one of the theoretical tools used to study and model individuals and populations ability to migrate between the spots (sites) of a given landscape. The landscape is somehow assimilated to a porous environment in which each living species moves more or less easily. In other words, percolation here makes it possible to assess the relationship between the migratory nature of species and the permissiveness of any ecosystem.
### Approximation of the theoretical value of the percolation threshold
By varying the probability p with a step of 0.01, and by doing 40 tests for each probability, I obtain the following curve, which plots the variation of DPM as a function of p.
In fact, it is a sigmoid function that shows the threshold effect around the critical value "pc", which even makes it possible to locate pc around 0.59, that is to say very close to the theoretical threshold value which is 0.5927 for site percolation on L² (cf. Mathematical approach file)
To verify this result, I called a Python function that allows regression with a given function, here a sigmoid, which I have drawn in red on the diagram. You will notice the coincidence of the curves, and also the threshold value, which is the point of inflection of the curve, that is to say 0.589.

### Simulation of the percolation behaviour 
