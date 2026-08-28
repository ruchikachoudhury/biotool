from Bio.PDB import PDBParser
def parse_pdb_file(file_path):
    parser = PDBParser()#assigning a variable to the method
    structure = parser.get_structure("protein",file_path)#file path is given to the method to get the structure
    for chain in structure.get_chains():#method used to loop through the chains present
        for residue in chain.get_residues():#method used to loop through redisues in those chains
            for atom in residue.get_atoms():#method used to loop through atoms present in the residue 
                atom_coord = atom.get_coord()#getting atom co-ordinates
                atom_name = atom.get_name()#getting atom name
                residue_name = residue.get_resname()#get residue name
                chain_id = chain.get_id()#getting chain id
                print(f"Chain: {chain_id}, Residue: {residue_name}, Atom: {atom_name}, Coordinates: {atom_coord}")
    return structure
  
