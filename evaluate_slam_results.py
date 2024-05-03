

# evo_traj kitti /path/to/your_trajectory.txt --ref=/path/to/ground_truth.txt -p --plot_mode=xy


# evo_traj kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -p --plot_mode=xy


# evo_ape kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -va

# evo_rpe kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -va

# evo_traj kitti results/ORBSLAM/KITTI/00/orbslam3/ORBSLAM3.txt  --ref=results/ORBSLAM/KITTI/00/gt/GT.txt  -p  --align --correct_scale --plot_mode=xz

# evo_ape kitti results/ORBSLAM/KITTI/00/gt/GT.txt results/ORBSLAM/KITTI/00/orbslam3/ORBSLAM3.txt    -p  --correct_scale --plot_mode=xz

import os
import argparse

#NOTE : documentation at : https://github.com/MichaelGrupp/evo/wiki/Metrics


#Another might be useful evaluation tool: https://zdzhaoyong.github.io/GSLAM/evaluate.html

def get_ape_results(dataset, sequence, gt_file, slam_file, results_dir, plot =False):
    evo_app = "evo_ape"

    full_res_path = results_dir+"/"+dataset+"/"+ sequence

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)

    output_file = os.path.basename(slam_file)
    output_file = output_file.replace(".txt", "")

    output_file+= "_APE.zip"

    result_file = os.path.join(full_res_path ,output_file)

    cmd = evo_app+ " "+ dataset +" "+ gt_file +" "+ slam_file +"   --correct_scale --save_results "+ result_file +" --silent --no_warnings"

    if plot:
        cmd += " -p  --plot_mode=xz"

    print(cmd)
    os.system(cmd)

    return result_file

def get_rpe_results(dataset, sequence, gt_file, slam_file, results_dir, plot =False):
    evo_app = "evo_rpe"
    
    full_res_path = results_dir+"/"+dataset+"/"+ sequence

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)


    output_file = os.path.basename(slam_file)
    output_file = output_file.replace(".txt", "")

    output_file+= "_RPE.zip"

    result_file = os.path.join(full_res_path ,output_file)
    # result_file = full_res_path +"/RPE.zip"


    cmd = evo_app+ " "+ dataset +" "+ gt_file +" "+ slam_file +"   --correct_scale --save_results "+ result_file +" --silent --no_warnings"

    if plot:
        cmd += " -p  --plot_mode=xz"
    print(cmd)
    os.system(cmd)

    return result_file





def process_results_kitti(dataset, sequence, trajectory_file_dir, results_dir, plot = False):
    current_results_path = trajectory_file_dir # "results/kitti/00"
    gt_file = os.path.join(current_results_path, str(sequence)+".txt")

    traj_file_list = os.listdir(current_results_path)
    slam_files_list = []
    for traj_file in traj_file_list:
        if str(sequence)+".txt" not in traj_file and ".txt" in traj_file:
            slam_files_list.append(os.path.join(current_results_path, traj_file))
            slam_file = os.path.join(current_results_path, traj_file)
            ape_result_file = get_ape_results(dataset, sequence, gt_file, slam_file, results_dir)
            rpe_result_file = get_rpe_results(dataset, sequence, gt_file, slam_file, results_dir)


def process_results_tum(dataset, sequence, trajectory_file_dir, results_dir, plot = False):
    current_results_path = trajectory_file_dir # "results/tum/rgbd_dataset_freiburg1_desk"
    gt_file = os.path.join(current_results_path, "groundtruth.txt")

    traj_file_list = os.listdir(current_results_path)
    slam_files_list = []
    for traj_file in traj_file_list:
        if "groundtruth.txt" not in traj_file and ".txt" in traj_file:
            slam_files_list.append(os.path.join(current_results_path, traj_file))
            slam_file = os.path.join(current_results_path, traj_file)
            ape_result_file = get_ape_results(dataset, sequence, gt_file, slam_file, results_dir)
            rpe_result_file = get_rpe_results(dataset, sequence, gt_file, slam_file, results_dir)



def process_results_euroc(dataset, sequence, trajectory_file_dir, results_dir, plot = False):
    current_results_path = trajectory_file_dir # "results/euroc/mav0"
    gt_file = os.path.join(current_results_path, "data.csv")

    traj_file_list = os.listdir(current_results_path)
    slam_files_list = []
    for traj_file in traj_file_list:
        if "data.csv" not in traj_file and ".txt" in traj_file:
            slam_files_list.append(os.path.join(current_results_path, traj_file))
            slam_file = os.path.join(current_results_path, traj_file)
            ape_result_file = get_ape_results(dataset, sequence, gt_file, slam_file, results_dir)
            rpe_result_file = get_rpe_results(dataset, sequence, gt_file, slam_file, results_dir)


def main():

    parser = argparse.ArgumentParser(description='Run the SLAM Evaluation pipeline')
    # parser.add_argument('dataset', type=str,  help='Name of the dataset, [kitti, tum, euroc]')
    # parser.add_argument('sequence', type=str,  help='Sequence number')
    

    # parser.add_argument('--plot', action='store_true', help='Plot the results')


    parser.add_argument('--results_dir', type=str, default="results_evo",  help='Path to the directory to save the results')

    parser.add_argument('trajectory_file_dir', type=str,  help='Path to the directory containing the trajectory files')
    args = parser.parse_args()

    results_dir = args.results_dir #"results_evo"


    # kitti_sequeces_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
    # tum_sequences_list = ["rgbd_dataset_freiburg1_desk", "fr2", "fr3", "fr3_long", "fr3_no_loop", "fr3_sitting_static", "fr3_sitting_static", "fr3_walking_static", "fr3_walking_xyz", "fr3_walking_halfsphere"]
    # euroc_sequences_list = ["mav0", "mav1", "mav2", "mav3", "mav4", "mav5", "mav6", "mav7", "mav8", "mav9", "mav10"]


    input_dir = args.trajectory_file_dir

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

    # Process kitti
    print("Processing KITTI")
    print(kitti_sequeces_list)
    for sequence in kitti_sequeces_list:
        dataset = "kitti"
        trajectory_file_dir = os.path.join(args.trajectory_file_dir, dataset, sequence)
        if not os.path.exists(trajectory_file_dir):
            continue
        process_results_kitti(dataset, sequence, trajectory_file_dir, results_dir)


    # Process Euroc
    print("Processing Euroc")
    print(euroc_sequences_list)
    for sequence in euroc_sequences_list:
        dataset = "euroc"
        trajectory_file_dir = os.path.join(args.trajectory_file_dir, dataset, sequence)
        if not os.path.exists(trajectory_file_dir):
            continue
        process_results_euroc(dataset, sequence, trajectory_file_dir, results_dir)


    # Process TUM
    print("Processing TUM")
    print(tum_sequences_list)

    for sequence in tum_sequences_list:
        dataset = "tum"
        trajectory_file_dir = os.path.join(args.trajectory_file_dir, dataset, sequence)
        if not os.path.exists(trajectory_file_dir):
            continue
        process_results_tum(dataset, sequence, trajectory_file_dir, results_dir)

if __name__ == "__main__":
    main()