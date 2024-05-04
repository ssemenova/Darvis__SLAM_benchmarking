
import os 


import argparse


def get_config_file(seq_num):
        

    seq_int = int(seq_num)

    configs_list = ["KITTI00-02.yaml", "KITTI03.yaml", "KITTI04-12.yaml"]
    if seq_int <=2:
        curr_config = configs_list[0]
    elif seq_int ==3:
        curr_config = configs_list[1]
    else:
        curr_config = configs_list[2]
    print(f"{seq_int:02}", curr_config)    
    return curr_config

def main():


    
    #./mono_kitti ../../Vocabulary/ORBvoc.txt KITTI00-02.yaml  'dataset/sequences/01'

    parser = argparse.ArgumentParser(description='Run the ORBSLAM pipeline')

    parser.add_argument('vocab_file', type=str,  help='Path to the vocabulary file')
    parser.add_argument('seq_path', type=str,  help='Path to the sequences folder containing all the seuqences. Eg. dataset/sequences/')
    parser.add_argument('executable_dir', type=str,  help='Path to the executable directory')
    
    parser.add_argument('--out_dir', type=str, default="results",  help='Path to the output directory')
    parser.add_argument('--dataset', type=str, default="kitti",  help='Name of the dataset')

    args = parser.parse_args()


    dataset = args.dataset # "kitti"

    exec_dir = args.executable_dir 

    exec_dir = os.path.abspath(exec_dir)

    exec_app =  os.path.join(args.executable_dir ,"/mono_"+dataset) # "./mono_kitti"

    vocab_file = args.vocab_file # "../../Vocabulary/ORBvoc.txt"

    seqs_path = args.seq_path # "datasets/data_odometry_color/dataset/sequences/"

    out_dir = args.out_dir # "results/"

    out_dir = os.path.abspath(out_dir)

    out_dir = os.path.join(out_dir , dataset)

    sequence_list = os.listdir(seqs_path)

    for curr_seq in sequence_list:
        
        # curr_seq = i #f"{i:02}"
        out_dir_seq = os.path.join(out_dir, curr_seq)

        if not os.path.exists(out_dir_seq):
            os.makedirs(out_dir_seq)

        out_dir_file = os.path.join(out_dir_seq, "KeyFrameTrajectory_"+curr_seq+".txt")
        print(out_dir_file)
        if os.path.exists(out_dir_file):
            print(curr_seq, "results already exists, skipping!!")
            continue

        curr_config = get_config_file(curr_seq)

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