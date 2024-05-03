# Evaluation steps

1. Move all the GT and generated trajectories as per following hierarchy:

<root_dir>/<dataset>/<sequence>/<gtfile> 
                                <pipeline1 trajectory file>
                                ... 
                                ...
Example 
results/kitti/00/GT.txt
                /ORBSLAM3.txt
                /DARVIS_ORBSLAM3.txt
                ...
results/euroc/mav0/data.csv
                /ORBSLAM3.txt
                /DARVIS_ORBSLAM3.txt
                ...
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
