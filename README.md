# Ewald
A script to obtain most favored configurations at various ionic concentrations of a cathode material.

## Requirements

1.Pymatgen ( https://pymatgen.org )
2.Pandas
3.Numpy
 
## Usage

python ewald.py {cif file name} { working ion with its oxidation state}

## Example

python ewald.py Na6MnO4.cif Na+  

## Output

One is expected to obtain a configuration file ( POSCAR ) for each composition of the working ion. For example -  5LiCoO2 ( a supercell made of 5 unit cells of LiCoO2 ) is expected to give 6 configurations (CoO2, Li0.2CoO2, Li0.4CoO2, Li0.6CoO2, Li0.8CoO2, LiCoO2 ) where each configuration is obtained by doing Ewald summation on all possible permutations of substructures and choosing the substructure which has the least energy.  Mind that above 26 working ions in the structure is pushing it (at least from initial tests). This is a good starting point to obtain stable intermediate configurations during delithiation. Also, a csv file is produced containing relevant energy values per formula unit. Find a sample output above.


