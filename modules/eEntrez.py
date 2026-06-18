from Bio import Entrez
def fetch_gene_info(gene_id, email, dbtype):
    Entrez.email = email
    handle = Entrez.efetch(db=dbtype, id=gene_id, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    
    if records:
        gene_info = records[0]
        gene_name = gene_info.get("Entrezgene_gene", {}).get("Gene-ref", {}).get("Gene-ref_locus", "")
        gene_description = gene_info.get("Entrezgene_summary", "")
        gene_organism = gene_info.get("Entrezgene_source", {}).get("BioSource", {}).get("BioSource_org", {}).get("Org-ref", {}).get("Org-ref_taxname", "")
        
        return {
            "gene_name": gene_name,
            "gene_description": gene_description,
            "gene_organism": gene_organism
        }
    else:
        return None

