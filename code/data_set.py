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
        clinic = pd.read_excel(doc, index_col=None, usecols='F:H')  
        
        self.patients_num = len(clinic) - 3

        c_data = {
        "mutation": [],
        "outcome": []
        }
        
        for i in range(self.patients_num):
            c_data["mutation"].append(clinic["Mutation"][i])
            c_data["outcome"].append(OUTCOME[clinic["Single-cell type"][i]])

        print("Clinic data is done....")
        self.clinic_data = c_data
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
            if "extra" in gene_xls.sheet_names[i]:
                pid = gene_xls.sheet_names[i][2:]
                    
            else:
                pid = int(gene_xls.sheet_names[i][1:3])
                                       
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
