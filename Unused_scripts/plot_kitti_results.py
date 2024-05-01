

# evo_traj kitti /path/to/your_trajectory.txt --ref=/path/to/ground_truth.txt -p --plot_mode=xy


# evo_traj kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -p --plot_mode=xy


# evo_ape kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -va

# evo_rpe kitti /Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences/01/poses.txt /Volumes/dl-primary-pool/pmeshram/SLAM_Run_Results/ORB_SLAM/KITTI/KeyFrameTrajectory_01.txt -va

# evo_traj kitti results/ORBSLAM/KITTI/00/orbslam3/ORBSLAM3.txt  --ref=results/ORBSLAM/KITTI/00/gt/GT.txt  -p  --align --correct_scale --plot_mode=xz

# evo_ape kitti results/ORBSLAM/KITTI/00/gt/GT.txt results/ORBSLAM/KITTI/00/orbslam3/ORBSLAM3.txt    -p  --correct_scale --plot_mode=xz

import os




def get_ape_results(dataset, sequence, gt_file, slam_files_list, results_dir, plot =False):
    evo_app = "evo_ape"

    full_res_path = results_dir+"/"+dataset+"/"+ sequence

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)
    result_file = full_res_path +"/APE.zip"



    cmd = evo_app+ " "+ dataset +" "+ gt_file +" "+ slam_files_list +"   --correct_scale --save_results "+ result_file +" --silent --no_warnings"

    if plot:
        cmd += " -p  --plot_mode=xz"

    print(cmd)
    os.system(cmd)

    return result_file

def get_rpe_results(dataset, sequence, gt_file, slam_files_list, results_dir, plot =False):
    evo_app = "evo_rpe"
    
    full_res_path = results_dir+"/"+dataset+"/"+ sequence

    if not os.path.exists(full_res_path):
        os.makedirs(full_res_path)
    result_file = full_res_path +"/RPE.zip"

    cmd = evo_app+ " "+ dataset +" "+ gt_file +" "+ slam_files_list +"   --correct_scale --save_results "+ result_file +" --silent --no_warnings"

    if plot:
        cmd += " -p  --plot_mode=xz"
    print(cmd)
    os.system(cmd)

    return result_file





def main():

    dataset = "kitti"
    sequence = "00"
    gt_file = "results/ORBSLAM/KITTI/00/GT.txt"
    slam_files_list = "results/ORBSLAM/KITTI/00/ORBSLAM3.txt"
    results_dir = "results_evo"

    ape_result_file = get_ape_results(dataset, sequence, gt_file, slam_files_list, results_dir)
    rpe_result_file = get_rpe_results(dataset, sequence, gt_file, slam_files_list, results_dir)


if __name__ == "__main__":
    main()