# Sample point clouds from the ScanNet dataset.
import numpy as np
import pyviz3d.visualizer as viz

def main(): 
    # First, we set up a visualizer
    v = viz.Visualizer()

    # Load a point cloud
    for scene_name in ['scene0140_01']:
        scene = np.load('examples/data/' + scene_name + '.npy')
        point_positions = scene[:, 0:3]
        point_colors = scene[:, 3:6]
        point_size = 20.0

    # Sequence of the pcd moving in x-dimension
    for i in range (30):
        # Unit displacement vector
        d = np.array([0.02, 0, 0])
        # Add point to the sequence visualizer 
        # x_translation: group name
        # i: frame_id
        # pcd: object name inside the group
        v.add_points(f'x_translation;,{i + 1},pcd', point_positions + d * i, point_colors, point_size=point_size)

    
    # Sequence of the pcd scaling up
    scales = np.linspace(1.0, 2.0, num=10)
    for i, scale in enumerate(scales):
        # Unit displacement vector
        d = np.array([0.02, 0, 0])
        # Add point to the sequence visualizer 
        # scale_up: group name
        # i: frame_id
        # pcd: object name inside the group
        v.add_points(f'scale_up;,{i + 1},pcd', point_positions * scale, point_colors, point_size=point_size)

    # When we added everything we need to the visualizer, we save it.
    v.save('example_sequence')

if __name__ == '__main__':
    main()