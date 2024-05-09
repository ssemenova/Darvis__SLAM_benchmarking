# ORBSLAM3 execution scripts
Three different exeuction scripts based on the dataset

execution/run_<dataset>.py


    parser.add_argument('vocab_file', type=str,  help='Path to the vocabulary file')
    parser.add_argument('seq_path', type=str,  help='Path to the sequences folder containing all the seuqences. Eg. dataset/sequences/')
    parser.add_argument('executable_dir', type=str,  help='Path to the executable directory')
    
    parser.add_argument('--out_dir', type=str, default="results",  help='Path to the output directory')
    parser.add_argument('--dataset', type=str, default="kitti",  help='Name of the dataset')

example use
```
    python execution/run_kitti.py <OS3_root>//Vocabulary/ORBvoc.txt  <kitti_dataset_root>/dataset/sequences/ <OS3_root>/Examples/Monocular/ --out_dir ./results  

```



# Evaluation steps

1. Move all the GT and generated trajectories as per following hierarchy:
```
<root_dir>/<dataset>/<sequence>/<gtfile> 
                                <pipeline1 trajectory file>
                                ... 
                                ...

```

Example 
```
results/kitti/00/00.txt
                /ORBSLAM3.txt
                /DARVIS_ORBSLAM3.txt
                ...
results/euroc/mav0/data.csv
                /ORBSLAM3.txt
                /DARVIS_ORBSLAM3.txt
                ...
```

2. Run evaluation script on the root dir:
    ```
        python evaluate_slam_results.py <root_dir> --results_dir=<target_results_dir>
    ```

    Example:
    ```
        python evaluate_slam_results.py results --results_dir=results_evo
    ```


3. Run summary table extraction script:
    ```
        python extract_results_as_table.py <output_dir> <input_root_dir>
    ```
Example:
    ```
        python extract_results_as_table.py results_evo/all_results results_evo
    ```


#Note:
For Euroc dataset, trajectory format is only supported as TUM format. When generating trajectories output format for euroc dataset must be TUM format trajectory and need to modify example code to generate this format specifically.
