

import os

import argparse

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


def process_results(results_zip_dir, results_dir, dataset, sequence):

    list_of_files = os.listdir(results_zip_dir)
    results_zip_APE = ""
    for file in list_of_files:
        if file.endswith(".zip") and "APE" in file:
            results_zip_APE +=  " " + results_zip_dir +"/"+ file

    ape_result_file = get_ape_results(results_zip_APE, results_dir, dataset, sequence)

    results_zip_RPE = ""
    for file in list_of_files:
        if file.endswith(".zip") and "RPE" in file:
            results_zip_RPE +=  " " + results_zip_dir +"/"+ file
    
    ape_result_file = get_rpe_results(results_zip_RPE, results_dir, dataset, sequence)



def main():



    parser = argparse.ArgumentParser(description='Run the SLAM Results to Table')
    parser.add_argument('results_dir', type=str,  help='Results Directory')
    parser.add_argument('input_zip_dir', type=str,  help='Results Zip Directory')
    args = parser.parse_args()

    results_dir = args.results_dir # "results_evo/all_results"



    # kitti_sequeces_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
    # tum_sequences_list = ["rgbd_dataset_freiburg1_desk", "fr2", "fr3", "fr3_long", "fr3_no_loop", "fr3_sitting_static", "fr3_sitting_static", "fr3_walking_static", "fr3_walking_xyz", "fr3_walking_halfsphere"]
    # euroc_sequences_list = ["mav0", "mav1", "mav2", "mav3", "mav4", "mav5", "mav6", "mav7", "mav8", "mav9", "mav10"]

    input_dir = args.input_zip_dir

    kitti_sequeces_list = []
    trajectory_file_dir_kitti = os.path.join(input_dir, 'kitti')
    if os.path.exists(trajectory_file_dir_kitti):
        kitti_sequeces_list = os.listdir(trajectory_file_dir_kitti)

    tum_sequences_list = []
    trajectory_file_dir_tum = os.path.join(input_dir, 'tum')
    if os.path.exists(trajectory_file_dir_tum):
        tum_sequences_list = os.listdir(trajectory_file_dir_tum)

    euroc_sequences_list = []
    trajectory_file_dir_euroc = os.path.join(input_dir, 'euroc')
    if os.path.exists(trajectory_file_dir_euroc):
        euroc_sequences_list = os.listdir(trajectory_file_dir_euroc)


    kitti_sequeces_list = [x for x in kitti_sequeces_list if x.startswith(".")==False]
    tum_sequences_list = [x for x in tum_sequences_list if x.startswith(".")==False]
    euroc_sequences_list = [x for x in euroc_sequences_list if x.startswith(".")==False]



    for sequence in kitti_sequeces_list:
        dataset = "kitti"
        results_zip_dir_root = args.input_zip_dir
        results_zip_dir = os.path.join(results_zip_dir_root, dataset, sequence)

        if os.path.exists(results_zip_dir):
            process_results(results_zip_dir, results_dir, dataset, sequence)
        


    for sequence in tum_sequences_list:
        dataset = "tum"
        results_zip_dir_root = args.input_zip_dir
        results_zip_dir = os.path.join(results_zip_dir_root, dataset, sequence)

        if os.path.exists(results_zip_dir):
            process_results(results_zip_dir, results_dir, dataset, sequence)

    for sequence in euroc_sequences_list:
        dataset = "euroc"
        results_zip_dir_root = args.input_zip_dir
        results_zip_dir = os.path.join(results_zip_dir_root, dataset, sequence)

        if os.path.exists(results_zip_dir):
            process_results(results_zip_dir, results_dir, dataset, sequence)


    # results_zip_dir = args.input_zip_dir # "results_evo/kitti/00"

    # list_of_files = os.listdir(results_zip_dir)
    # results_zip_APE = ""
    # for file in list_of_files:
    #     if file.endswith(".zip") and "APE" in file:
    #         results_zip_APE +=  " " + results_zip_dir +"/"+ file

    # ape_result_file = get_ape_results(results_zip_APE, results_dir, "kitti", "00")

    # results_zip_RPE = ""
    # for file in list_of_files:
    #     if file.endswith(".zip") and "RPE" in file:
    #         results_zip_RPE +=  " " + results_zip_dir +"/"+ file
    
    # ape_result_file = get_rpe_results(results_zip_RPE, results_dir, "kitti", "00")



if __name__ == "__main__":
    main()