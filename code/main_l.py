

from numpy.lib.function_base import average
import data_set as ds
import numpy as np
import patients as pt

    

# initlize the dataset with the file names
def init_dataset() -> ds.DataSet:

    doc_genes = "./datasets/All_patients_marker_genes.xlsx"
    doc_clinic = "./datasets/All_patients_clinical_data.xlsx"
    doc_bcell = "./datasets/All_patients_marker_genes_Bcells.xlsx"
    doc_tcell = "./datasets/All_patients_marker_genes_Tcell.xlsx"
    doc_monocytes = "./datasets/All_patients_marker_genes_monocytes.xlsx"
    doc_neu = "./datasets/All_patients_marker_genes_neutrophils.xlsx"

    
    data_set = ds.DataSet()
    data_set.read_clinic(doc_clinic)
    data_set.read_genes(doc_genes)
    data_set.read_cells(doc_tcell)
    data_set.read_cells(doc_monocytes)
    data_set.read_cells(doc_bcell) 
    data_set.read_cells(doc_neu)   

    return data_set


def print_datasets(datasets: ds.DataSet) -> None:

    print(f'\n--Patient B cells: {len(datasets.bcell_data["patient_id"])}')
    print(datasets.bcell_data["patient_id"])
    for x in datasets.bcell_data["genes"]:        
        print(f'Patient: {x} - {datasets.bcell_data["genes"][x]}')
    
    print(f'\n--Patient T cells: {len(datasets.tcell_data["patient_id"])}')
    print(datasets.tcell_data["patient_id"])
    for x in datasets.tcell_data["genes"]:
        print(f'Patient: {x} - {datasets.tcell_data["genes"][x]}')
    
    print(f'\n--Patient Monocytes: {len(datasets.monocytes_data["patient_id"])}')
    print(datasets.monocytes_data["patient_id"])
    for x in datasets.monocytes_data["genes"]:
        print(f'Patient: {x} - {datasets.monocytes_data["genes"][x]}')
    
    print(f'\n--Patient Neutrophils data: {len(datasets.neu_data["patient_id"])}')
    print(datasets.neu_data["patient_id"])
    for x in datasets.neu_data["genes"]:
        print(f'Patient: {x} - {datasets.neu_data["genes"][x]}')



def init_patients(datasets: ds.DataSet):

    patients = {}
    c = datasets.clinic_data

    for i in range(len(c["patient_id"])):
        p = pt.Patient()
        p.set_id(c["patient_id"][i])
        p.set_outcome(c["outcome"][i])
        p.set_mutation(c["mutation"][i])
        p.set_treatment(c["treatment"][i])

        # set tcell
        if p.id in datasets.tcell_data["patient_id"]:
            p.set_tcell(datasets.tcell_data["genes"][p.id])
        
        # set bcell
        if p.id in datasets.bcell_data["patient_id"]:
            p.set_bcell(datasets.bcell_data["genes"][p.id])
        
        # set monocytes
        if p.id in datasets.monocytes_data["patient_id"]:
            p.set_monotypes(datasets.monocytes_data["genes"][p.id])
        

        # set Neutrophils
        if p.id in datasets.neu_data["patient_id"]:
            p.set_neu(datasets.neu_data["genes"][p.id])
        
        patients[i] = p
        
    
    return patients


def print_patients(patients):
    for p in patients:
        x = patients[p]
        print(f'\n- Patient id: {x.id} \
                \n -- Outcome: {x.outcome}  - Mutation: {x.mutation} - treatment: {x.treatment}')
        print(f' * T cell: {x.tcell}')
        print(f' * B cell: {x.bcell}')
        print(f' * Monocytes: {x.monotypes}')
        print(f' * Neu: {x.neu}')


CATE = {
    "tcell": "tcell",
    "bcell": "bcell",
    "monotypes": "monotypes",
    "neu": "neu"
}

def compare_patients(patients):

    merged_relapse = {}
    merged_remission = {}
    
    for x in patients:
        p = patients[x]

        if p.outcome == "relapse":
            merged = merged_relapse
        elif p.outcome == "remission":
            merged = merged_remission

        for cell in p.tcell:
            if cell in merged:
                merged[cell].append(p.tcell[cell])
                
            else:
                merged[cell] = [p.tcell[cell]]

    avg_relapse = {}
    avg_remission = {}
    print("\n--Remission patients at Average:")
    for m in merged_remission:
        print(f'{m} - {merged_remission[m]}')
        avg_remission[m] = average(merged_remission[m])
        print(f'{m} - {avg_remission[m]}')

    print("\n--Relapse patients at Average:")
    for m in merged_relapse:
        print(f'{m} - {merged_relapse[m]}')
        avg_relapse[m] = average(merged_relapse[m])
        print(f'{m} - {avg_relapse[m]}')

    diff_rem = {}
    print("\n\n -- The difference between Remission and Relapse")
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = avg_remission[m] - avg_relapse[m]
            print(f'{m}: {diff_rem[m]}')
    



# main function for running the code
def main():
    datasets = init_dataset()

    patients = init_patients(datasets)
    
    # print_patients(patients)
    compare_patients(patients)

        

if __name__ == "__main__":
    main()
