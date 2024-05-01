from darvis_configs import *

import argparse
import os
def main():

    # # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Run the Darvis pipeline')
    parser.add_argument('pipeline', type=str,  help='Name of the pipeline')
    parser.add_argument('dataset', type=str,  help='Name of the dataset')
    parser.add_argument('sequence', type=int,  help='Sequence number')
    parser.add_argument('dataset_path', type=str,  help='Path to the dataset upto sequences folder if KITTI dataset is used')
    args = parser.parse_args()

    # Run the Darvis pipeline
    pipeline = args.pipeline # 'PIPELINE_ORBSLAM'
    dataset = args.dataset #'KITTI'
    sequence = args.sequence # 3
    dataset_path = args.dataset_path # '/Volumes/dl-primary-pool/lidar-research/Geometric_Seg_Pranay/datasets/data_odometry_labels/dataset/sequences'
    darvis_pipeline = DarvisPipeline(pipeline, dataset, sequence, dataset_path)
    # darvis_pipeline.print_configs()

    system_config_file = 'darvis_configs/system_config.yaml'
    dataset_config_file = f'darvis_configs/{dataset}_{sequence}.yaml'
    darvis_pipeline.run_pipeline(system_config_file, dataset_config_file)



if __name__ == '__main__':
    main()


