# Project:      “AI Against Cancer Hackathon"
# Date created: Aug 10th, 2021

import pandas as pd


# Input: docment of the clinic of all patiences
# Output: the genes data of mutation and cell type
def read_clinic(doc):
    clinic = pd.read_excel(doc, index_col=None, usecols='F:H')  
    c_data = {
    "mutation": [],
    "cell_type": []
    }

    for i in range(len(clinic) - 3):
        c_data["mutation"].append(clinic["Mutation"][i])
        c_data["cell_type"].append(clinic["Single-cell type"][i])

    for i in range(len(c_data["mutation"])):
        print(f'{c_data["cell_type"][i]}: {c_data["mutation"][i]}')

    return c_data


# Input: docment of the genes of all patiences
# Output: the genes data of avg_logFC and cell type
def read_genes(doc):
    gene_xls = pd.ExcelFile(doc)
    genes = {}
    for i in range(40):    
        genes[i] = pd.read_excel(gene_xls, f'P{(i+1):02d}', index_col=None, usecols='C, J')

    print(genes)

    return genes

    
# main function for running the code
def main():
    doc_genes = "./datasets/All_patients_marker_genes.xlsx"
    doc_clinic = "./datasets/All_patients_clinical_data.xlsx"

    read_clinic(doc_clinic)
    read_genes(doc_genes)




if __name__ == "__main__":
    main()
