

from numpy.lib.function_base import average
import pandas as pd
import data_set as ds
import numpy as np
import patients as pt

DATA_FILTER = 0.2


def compare_patients_tcell(patients):

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

    print("\n\n--T Cell Data ----")

    print("\n--Remission patients at Average - T Cell:")
    for m in merged_remission:
        # print(f'{m} - {merged_remission[m]}')
        avg_remission[m] = average(merged_remission[m])
        print(f'{m} - {avg_remission[m]}')

    print("\n--Relapse patients at Average - T Cell:")
    for m in merged_relapse:
        # print(f'{m} - {merged_relapse[m]}')
        avg_relapse[m] = average(merged_relapse[m])
        print(f'{m} - {avg_relapse[m]}')

   
    print("\n\n -- The difference between Remission and Relapse - T Cell")
    diff_rem = computer_diff(avg_remission, avg_relapse)
    
    print("\n\n -- The filtered difference - T Cell ")
    filtered, non_filter = filter_diff(diff_rem)
    
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem,
        "filtered": filtered,
        "non_filter": non_filter
    }
    csv_file = open("tcell_filtered.csv", "w")
    csv_file.write(f"\nGenes,filtered difference")
    for x in filtered:
        csv_file.write(f"\n{x},{filtered[x]}")
    csv_file.close()

    return cdata




def compare_patients_bcell(patients):

    merged_relapse = {}
    merged_remission = {} 
    
    for x in patients:
        p = patients[x]

        if p.outcome == "relapse":
            merged = merged_relapse
        elif p.outcome == "remission":
            merged = merged_remission

        for cell in p.bcell:
            if cell in merged:
                merged[cell].append(p.bcell[cell])
                
            else:
                merged[cell] = [p.bcell[cell]]

    avg_relapse = {}
    avg_remission = {}

    print("\n\n--B Cell Data ----")

    print("\n--Remission patients at Average - B Cell :")
    for m in merged_remission:
        # print(f'{m} - {merged_remission[m]}')
        avg_remission[m] = average(merged_remission[m])
        print(f'{m} - {avg_remission[m]}')

    print("\n--Relapse patients at Average - B Cell :")
    for m in merged_relapse:
        # print(f'{m} - {merged_relapse[m]}')
        avg_relapse[m] = average(merged_relapse[m])
        print(f'{m} - {avg_relapse[m]}')

    print("\n\n -- The difference between Remission and Relapse - B Cell ")
    diff_rem = computer_diff(avg_remission, avg_relapse)
    
    print("\n\n -- The filtered difference - B Cell ")
    filtered, non_filter = filter_diff(diff_rem)
    
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem,
        "filtered": filtered,
        "non_filter": non_filter
    }

    csv_file = open("bcell_filtered.csv", "w")
    csv_file.write(f"\nGenes,Filtered Difference")
    for x in filtered:
        csv_file.write(f"\n{x},{filtered[x]}")
    csv_file.close()

    return cdata




def compare_patients_neu(patients):

    merged_relapse = {}
    merged_remission = {} 
    
    for x in patients:
        p = patients[x]

        if p.outcome == "relapse":
            merged = merged_relapse
        elif p.outcome == "remission":
            merged = merged_remission

        for cell in p.neu:
            if cell in merged:
                merged[cell].append(p.neu[cell])
                
            else:
                merged[cell] = [p.neu[cell]]

    avg_relapse = {}
    avg_remission = {}

    print("\n\n--Neutrophils Data ----")

    print("\n--Remission patients at Average - Neutrophils :")
    for m in merged_remission:
        # print(f'{m} - {merged_remission[m]}')
        avg_remission[m] = average(merged_remission[m])
        print(f'{m} - {avg_remission[m]}')

    print("\n--Relapse patients at Average - Neutrophils :")
    for m in merged_relapse:
        # print(f'{m} - {merged_relapse[m]}')
        avg_relapse[m] = average(merged_relapse[m])
        print(f'{m} - {avg_relapse[m]}')
    
    print("\n\n -- The difference between Remission and Relapse - Neutrophils ")
    diff_rem = computer_diff(avg_remission, avg_relapse)
        
    print("\n\n -- The filtered difference - Neutrophils ")

    filtered, non_filter = filter_diff(diff_rem)
    
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem,
        "filtered": filtered,
        "non_filter": non_filter
    }

    csv_file = open("Neu_filtered.csv", "w")
    csv_file.write(f"\nGenes,Filtered Difference")
    for x in filtered:
        csv_file.write(f"\n{x},{filtered[x]}")
    csv_file.close()


    return cdata


def compare_patients_mono(patients):

    merged_relapse = {}
    merged_remission = {} 
    
    for x in patients:
        p = patients[x]

        if p.outcome == "relapse":
            merged = merged_relapse
        elif p.outcome == "remission":
            merged = merged_remission

        for cell in p.monotypes:
            if cell in merged:
                merged[cell].append(p.monotypes[cell])
                
            else:
                merged[cell] = [p.monotypes[cell]]

    avg_relapse = {}
    avg_remission = {}

    print("\n\n--monotypes Data ----")

    print("\n--Remission patients at Average - monotypes :")
    for m in merged_remission:
        # print(f'{m} - {merged_remission[m]}')
        avg_remission[m] = average(merged_remission[m])
        print(f'{m} - {avg_remission[m]}')

    print("\n--Relapse patients at Average - monotypes :")
    for m in merged_relapse:
        # print(f'{m} - {merged_relapse[m]}')
        avg_relapse[m] = average(merged_relapse[m])
        print(f'{m} - {avg_relapse[m]}')

    
    print("\n\n -- The difference between Remission and Relapse - monotypes ")
    diff_rem = computer_diff(avg_remission, avg_relapse)
    
    print("\n\n -- The filtered difference - Monotypes ")
    
    filtered, non_filter = filter_diff(diff_rem)
        
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem,
        "filtered": filtered,
        "non_filter": non_filter
    }

    csv_file = open("mono_filtered.csv", "w")
    csv_file.write(f"\nGenes,Filtered Difference")
    for x in filtered:
        csv_file.write(f"\n{x},{filtered[x]}")
    csv_file.close()

    return cdata


def filter_diff(diff_rem):
    filtered = {}
    non_filter = {}
    for d in diff_rem:
        non_filter[d] = diff_rem[d][2]
        if  abs(diff_rem[d][2]) > DATA_FILTER:
            filtered[d] = diff_rem[d][2]
            print(f'{d}: {filtered[d]}')
    
    print("\nSorted.............")
    # filt = {k: v for k, v in sorted(filtered.items(), key=lambda item: item[1])}
    
    filt = sorted(filtered.items(), key=lambda x:x[1])
    nf = sorted(non_filter.items(), key=lambda x:x[1])

    r_data = {}
    for d in filt:
        print(f'{d[0]}: {d[1]}')
        r_data[d[0]] = d[1]

    print(r_data)

    n_data = {}
    for d in nf:
        n_data[d[0]] = d[1]
    
    return r_data, n_data

    

def computer_diff(avg_remission, avg_relapse):
    diff_rem = {}
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = [avg_remission[m], 
                            avg_relapse[m],
                            avg_remission[m] - avg_relapse[m]]
            print(f'{m}: {diff_rem[m]}')
    return diff_rem


