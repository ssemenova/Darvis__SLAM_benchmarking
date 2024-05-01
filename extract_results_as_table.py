

import os


def get_ape_results(results_zip, results_dir, dataset, sequence, plot =False):
    evo_app = "evo_res"

    full_res_path = results_dir

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)

    result_file = results_dir +"/APE_"+dataset+"_"+sequence+".csv"
    
    cmd = evo_app +" --save_table "+ result_file +" --silent --no_warnings "+ " "+ results_zip

    if plot:
        cmd += " -p"

    print(cmd)
    os.system(cmd)

    return result_file


def get_rpe_results(results_zip, results_dir, dataset, sequence, plot =False):
    evo_app = "evo_res"
    
    full_res_path = results_dir

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)
    result_file = results_dir +"/RPE_"+dataset+"_"+sequence+".csv"

    cmd = evo_app+" --save_table "+ result_file +" --silent --no_warnings  "+ " "+ results_zip 

    if plot:
        cmd += " -p"
    print(cmd)
    os.system(cmd)

    return result_file

def main():

    results_dir = "results_evo/all_results"

    results_zip_dir = "results_evo/kitti/00"

    list_of_files = os.listdir(results_zip_dir)
    results_zip_APE = ""
    for file in list_of_files:
        if file.endswith(".zip") and "APE" in file:
            results_zip_APE +=  " " + results_zip_dir +"/"+ file

    ape_result_file = get_ape_results(results_zip_APE, results_dir, "kitti", "00")

    results_zip_RPE = ""
    for file in list_of_files:
        if file.endswith(".zip") and "RPE" in file:
            results_zip_RPE +=  " " + results_zip_dir +"/"+ file
    
    ape_result_file = get_rpe_results(results_zip_RPE, results_dir, "kitti", "00")



if __name__ == "__main__":
    main()