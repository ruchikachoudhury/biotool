from Bio.PDB import PDBParser
def parse_pdb_file(file_path):
    parser = PDBParser()
    structure = parser.get_structure("protein",file_path)
    for chain in structure.get_chains():
        for residue in chain.get_residues():
            for atom in residue.get_atoms():
                atom_coord = atom.get_coord()
                atom_name = atom.get_name()
                residue_name = residue.get_resname()
                chain_id = chain.get_id()
                print(f"Chain: {chain_id}, Residue: {residue_name}, Atom: {atom_name}, Coordinates: {atom_coord}")
    return structure
  