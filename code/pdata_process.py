

from numpy.lib.function_base import average
import data_set as ds
import numpy as np
import patients as pt


def compare_patients_tcell(patients):

    merged_relapse = {}
    merged_remission = {} 
    tcell = {}   
    
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

    diff_rem = {}
    print("\n\n -- The difference between Remission and Relapse - T Cell")
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = avg_remission[m] - avg_relapse[m]
            print(f'{m}: {diff_rem[m]}')
    
    tcell = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem
    }

    return tcell




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

    diff_rem = {}
    print("\n\n -- The difference between Remission and Relapse - B Cell ")
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = avg_remission[m] - avg_relapse[m]
            print(f'{m}: {diff_rem[m]}')
    
    bcell = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem
    }

    return bcell




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

    diff_rem = {}
    print("\n\n -- The difference between Remission and Relapse - Neutrophils ")
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = avg_remission[m] - avg_relapse[m]
            print(f'{m}: {diff_rem[m]}')
    
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem
    }

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

    diff_rem = {}
    print("\n\n -- The difference between Remission and Relapse - monotypes ")
    for m in avg_remission:
        if m in avg_relapse:
            diff_rem[m] = avg_remission[m] - avg_relapse[m]
            print(f'{m}: {diff_rem[m]}')
    
    cdata = {
        "avg_remission": avg_remission,
        "avg_relapse": avg_relapse,
        "diff": diff_rem
    }

    return cdata

