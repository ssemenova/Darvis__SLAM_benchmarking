import os 


import argparse


def get_config_file(seq_num):

    if "freiburg1" in seq_num:
        return "TUM1.yaml"
    elif "freiburg2" in seq_num:
        return "TUM2.yaml"
    elif "freiburg3" in seq_num:
        return "TUM3.yaml"
    else:
        raise ValueError("Invalid sequence name")


def main():
    
    #./mono_tum ../../Vocabulary/ORBvoc.txt TUM1.yaml  'dataset/rgbd_dataset_freiburg1_desk'


    parser = argparse.ArgumentParser(description='Run the ORBSLAM pipeline')

    parser.add_argument('vocab_file', type=str,  help='Path to the vocabulary file')
    parser.add_argument('seq_path', type=str,  help='Path to the sequences folder containing all the seuqences. i.e. the root dataset directory')
    
    parser.add_argument('executable_dir', type=str,  help='Path to the executable directory')
    
    parser.add_argument('--out_dir', type=str, default="results",  help='Path to the output directory')
    parser.add_argument('--dataset', type=str, default="tum",  help='Name of the dataset')

    args = parser.parse_args()


    dataset = args.dataset # "tum"

    exec_dir = args.executable_dir 

    exec_dir = os.path.abspath(exec_dir)

    exec_app =  os.path.join(args.executable_dir ,"/mono_"+dataset) # "./mono_tum"

    vocab_file = args.vocab_file # "../../Vocabulary/ORBvoc.txt"

    seqs_path = args.seq_path # "datasets/data_odometry_color/dataset/sequences/"

    out_dir = args.out_dir # "results/"

    out_dir = os.path.abspath(out_dir)

    out_dir = os.path.join(out_dir , dataset)

    for i in range(13):
        
        curr_seq = f"{i:02}"
        out_dir_seq = os.path.join(out_dir, curr_seq)

        if not os.path.exists(out_dir_seq):
            os.makedirs(out_dir_seq)

        out_dir_file = os.path.join(out_dir_seq, "KeyFrameTrajectory_"+curr_seq+".txt")
        print(out_dir_file)
        if os.path.exists(out_dir_file):
            print(curr_seq, "results already exists, skipping!!")
            continue

        curr_config = get_config_file(i)

        curr_config = os.path.join(exec_dir, curr_config)


        seq_path_curr = "".join([seqs_path, curr_seq])
        print(seq_path_curr)
        command = " ".join([exec_app, vocab_file, curr_config, seq_path_curr])
        print(command)
        os.system(command)

        out_dir_file_cam = os.path.join(out_dir_seq, "CameraTrajectory_"+curr_seq+".txt")
        
        os.system("cd "+exec_dir+" mv KeyFrameTrajectory.txt KeyFrameTrajectory_"+curr_seq+".txt" )
    
        os.system("cd "+exec_dir+"; mv CameraTrajectory.txt CameraTrajectory_"+curr_seq+".txt" )

        os.system("cd "+exec_dir+"; cp KeyFrameTrajectory_"+curr_seq+".txt "+out_dir_file)
        os.system("cd "+exec_dir+"; cp CameraTrajectory_"+curr_seq+".txt "+out_dir_file_cam)


if __name__ =="__main__":
    main()