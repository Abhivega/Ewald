from pymatgen.transformations.standard_transformations import PartialRemoveSpecieTransformation
import numpy as np
import pandas as pd
import sys
import os
from pymatgen import Structure


filename = sys.argv[1]
ion =sys.argv[2]
file = filename.split('.')[0]
os.mkdir(file)

try:
    print(file+' initiated')
    data=[]
    structure = Structure.from_file(filename)
    structure.add_oxidation_state_by_guess()
    len = structure.composition.as_dict()[ion]

    if len > 26 :
    	print(" WARNING !! .. too many combinations, might take a long time")
    elif len < 3:
    	print('Not enough combinations. Consider converting into a supercell')

    fact = structure.composition.get_reduced_composition_and_factor()[1]
    print(f'The given compound has {fact} formula units.')
    os.chdir(file)

    try:
        print(f"{file} with {len} {ion} has initiated.")
        for i in np.arange(0,len+1,1):
            trans = PartialRemoveSpecieTransformation(ion,i/len)
            substructures = trans.apply_transformation(structure,return_ranked_list=1)   # change this number to get multiple configurations with higher ewrld summation.
            substructures[0]['structure'].to(fmt='poscar', filename=str('POSCAR'+str(int(i))))
            data.append([i,(1-i/len),substructures[0]['energy'],substructures[0]['energy']/fact])  # the last term is the normatised ewrld summation with number of formula units

        df=pd.DataFrame(data,columns=['file','composition','Ewald_energy','Norm ( Ewald_energy / '+str(fact)+')' ])

        df.to_csv(file+'.csv')
        print(f'{file} saved')
    except:
        print(' Operation failed to find possible structures.')
        
except:
    print('Operation failed to recognise oxidation states of the elements. The CIF file should contain oxidation states.')

