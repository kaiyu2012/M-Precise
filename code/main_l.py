

import data_set as ds
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


def init_patients(datasets: ds.DataSet):

    patients = {}

    for i in range(datasets.patients_num):
        p = pt.Patient()
        p.set_mutation(datasets.clinic_data["mutation"][i])
        p.set_outcome(datasets.clinic_data["outcome"][i])

        patients[i] = p
    
    return patients


# main function for running the code
def main():
    datasets = init_dataset()
    
    print(f'\n--Patient B cells: {len(datasets.bcell_data["patient_id"])}')
    print(datasets.bcell_data["patient_id"])
    for x in datasets.bcell_data["genes"]:        
        print(f'Patient Bcell: {x} - {datasets.bcell_data["genes"][x]}')
    
    print(f'\n--Patient T cells: {len(datasets.tcell_data["patient_id"])}')
    print(datasets.tcell_data["patient_id"])
    for x in datasets.tcell_data["genes"]:
        print(f'Patient Tcell: {x} - {datasets.tcell_data["genes"][x]}')
    
    print(f'\n--Patient Monocytes: {len(datasets.monocytes_data["patient_id"])}')
    print(datasets.monocytes_data["patient_id"])
    for x in datasets.monocytes_data["genes"]:
        print(f'Patient Monocytes_data: {x} - {datasets.monocytes_data["genes"][x]}')
    
    print(f'\n--Patient Neutrophils data: {len(datasets.neu_data["patient_id"])}')
    print(datasets.neu_data["patient_id"])
    for x in datasets.neu_data["genes"]:
        print(f'Patient Neutrophils data: {x} - {datasets.neu_data["genes"][x]}')

if __name__ == "__main__":
    main()
