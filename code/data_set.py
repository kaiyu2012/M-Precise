# Project:      “AI Against Cancer Hackathon"
# Date created: Aug 10th, 2021

import pandas as pd
import numpy as np

OUTCOME = {
"I":     "relapse",
"II":    "remission",
np.nan:  "unknown"
}


class DataSet:

    def __inti__(self):
        self.patients_num = 0

    # Input: docment of the clinic of all patiences
    # Output: the genes data of mutation and cell type
    def read_clinic(self, doc) -> dict:
        clinic = pd.read_excel(doc, index_col=None, usecols='A, F, H, I')  
        
        # only use 40 patients data, drop others
        self.patients_num = len(clinic) - 6      

        c_data = {
        "patient_id":[],
        "mutation": [],
        "treatment":[],
        "outcome": []
        }
        
        print(clinic.columns)
        for i in range(self.patients_num):
            c_data["patient_id"].append(clinic[clinic.columns[0]][i])
            c_data["mutation"].append(clinic[clinic.columns[1]][i])
            c_data["treatment"].append(clinic[clinic.columns[2]][i])
            c_data["outcome"].append(OUTCOME[clinic[clinic.columns[3]][i]])

        print("Clinic data is done....")
        self.clinic_data = c_data
        print(c_data)
        return c_data


    # Input: docment of the genes of all patiences
    # Output: the genes data of avg_logFC and cell type
    def read_genes(self, doc) -> dict:
        gene_xls = pd.ExcelFile(doc)
        genes = {}
        for i in range(len(gene_xls.sheet_names)):    
            genes[i] = pd.read_excel(gene_xls, gene_xls.sheet_names[i], index_col=None, usecols='C, J')

        print("All genes data are fetched...")

        self.genes_data = genes

        return genes



    # Input: docment of the genes of Bcell or Tcell
    # Output: the genes data of avg_logFC and cell type
    def read_cells(self, doc) -> None:
        gene_xls = pd.ExcelFile(doc)
        genes = {}
        for i in range(len(gene_xls.sheet_names)):    
            genes[i] = pd.read_excel(gene_xls, gene_xls.sheet_names[i], index_col=None, usecols='A, C')

        cell = {
            "patient_id":[],
            "genes": {},
            }               

        for i in range(len(genes)):

            # get the column index name for every sheet
            columns = []
            for col in genes[i]:
                columns.append(col)

            # get the patient id
            # # drop the extra patient data
            if "extra" in gene_xls.sheet_names[i]:            
                continue                    
            else:
                pid = gene_xls.sheet_names[i][0:3]
                                       
            cell["patient_id"].append(pid)
            # parser the data
            g = {}
            for j in range(len(genes[i][columns[0]])):
                g[genes[i][columns[0]][j]] = genes[i][columns[1]][j] 

            cell["genes"][pid] = g
        
        if "Bcell" in doc:
            print("B cell data are fetched...")                         
            self.bcell_data = cell

        elif "Tcell" in doc:
            print("T cell data are fetched...")
            self.tcell_data = cell

        elif "monocytes" in doc:
            print("Monocytes data are fetched...")
            self.monocytes_data = cell
        elif "neutro" in doc:
            print("Neutrophils data are fetched...")
            self.neu_data = cell
