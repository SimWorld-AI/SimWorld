"""Utilities for recording simulation videos and logging metadata for multiple humanoids."""

import csv
import os
import random

import cv2


class VideoRecorder:
    """Record frames from multiple humanoid-mounted cameras and export video/CSV logs."""

    def __init__(
        self,
        communicator,
        humanoids,
        output_dir='.',
        resolution=(1440, 720),
        fps=25.0,
        frame_num=500,
        move_pattern=None,
        camera_mode='lit'
    ):
        """Initialize the recorder with target communicator and humanoids.

        Parameters
        ----------
        communicator: object
            Game communicator providing camera and control APIs.
        humanoids: list
            List of humanoid agents that own the cameras to record from.
        output_dir: str
            Directory to write the output files.
        resolution: tuple[int, int]
            Target camera resolution (width, height).
        fps: float
            Frames per second for the output video.
        frame_num: int
            Total number of frames to record.
        camera_mode: str
            Unreal render mode, e.g., 'lit', 'depth'.
        move_pattern: callable
            Function move_pattern(timestamp) -> list of (action_name, value)
        """
        self.communicator = communicator
        self.humanoids = humanoids if isinstance(humanoids, list) else [humanoids]
        self.output_dir = output_dir
        self.resolution = resolution
        self.fps = fps
        self.frame_num = frame_num
        self.camera_mode = camera_mode

        # If user provides a move_pattern, use it; otherwise, use default
        self.move_pattern = move_pattern if move_pattern else self._default_move_pattern

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Set camera resolution and fps
        for humanoid in self.humanoids:
            self.communicator.unrealcv.set_camera_resolution(humanoid.camera_id, resolution)
        self.communicator.unrealcv.set_fps(fps)

    def record(self):
        """Record frames from all humanoids synchronously.

        Each humanoid gets its own folder for video + CSV logs.

        Returns
        -------
        dict
            Dictionary mapping humanoid ID to their video folder path.
        """
        timestamp = 0
        stop = False

        # Prepare per-humanoid storage
        storage = {}
        for h in self.humanoids:
            folder = os.path.join(self.output_dir, f'humanoid_{h.id}')
            os.makedirs(folder, exist_ok=True)
            storage[h.id] = {
                'folder': folder,
                'images': [],
                'camera': [],
                'actions': []
            }

        while not stop:
            for humanoid in self.humanoids:
                # Capture image
                # Get actions from move_pattern (independent of humanoid)
                action_list = self.move_pattern(timestamp)
                try:
                    img = self.communicator.get_camera_observation(
                        humanoid.camera_id, self.camera_mode, mode='direct'
                    )
                    storage[humanoid.id]['images'].append(img)
                except Exception as e:
                    print(f'❌ Error getting image for humanoid {humanoid.id}:', e)
                    storage[humanoid.id]['images'].append(None)

                # Get camera location & rotation
                cam_loc = self.communicator.unrealcv.get_camera_location(humanoid.camera_id)
                cam_rot = self.communicator.unrealcv.get_camera_rotation(humanoid.camera_id)
                storage[humanoid.id]['camera'].append([timestamp, cam_loc, cam_rot])

                # Apply all actions to this humanoid
                for action_name, value in action_list:
                    self._apply_action(humanoid, action_name, value, timestamp, storage[humanoid.id]['actions'])

            # Progress bar
            timestamp += 1
            if self.frame_num > 0:
                progress = timestamp / self.frame_num
                bar_length = 30
                filled = int(bar_length * progress)
                bar = '#' * filled + '-' * (bar_length - filled)
                print(f'\rProgress: |{bar}| {timestamp}/{self.frame_num} ({progress:.1%})', end='')

            if timestamp >= self.frame_num:
                stop = True

            # Tick once for all humanoids
            self.communicator.unrealcv.tick()

        print('\n✅ Recording finished.')

        # Save video and CSVs for each humanoid
        video_paths = {}
        for humanoid in self.humanoids:
            folder = storage[humanoid.id]['folder']
            vid_path = os.path.join(folder, 'video.mp4')
            cam_csv = os.path.join(folder, 'camera.csv')
            act_csv = os.path.join(folder, 'actions.csv')

            self.save_video(storage[humanoid.id]['images'], vid_path)
            self.save_csv(storage[humanoid.id]['camera'], storage[humanoid.id]['actions'], cam_csv, act_csv)

            video_paths[humanoid.id] = folder

        return video_paths

    def _default_move_pattern(self, timestamp):
        """Default move pattern: independent random movement per humanoid.

        Returns a list of (action_name, value) tuples. No humanoid reference here.
        """
        actions = []
        # Always move forward
        actions.append(('move_forward', None))

        # Large random turn occasionally
        if timestamp % random.randint(30, 50) == 0:
            turn_dir = random.choice(['left', 'right'])
            turn_angle = random.randint(60, 160)
            actions.append((f'rotate_{turn_dir}', turn_angle))
        # Small jitter occasionally
        elif timestamp % random.randint(20, 40) == 0:
            jitter = random.randint(-10, 10)
            if jitter > 0:
                actions.append(('rotate_right', jitter))
            elif jitter < 0:
                actions.append(('rotate_left', abs(jitter)))
        return actions

    def _apply_action(self, humanoid, action, value, timestamp, actions_log):
        """Apply an action to a specific humanoid and log it.

        Parameters
        ----------
        humanoid: object
            Target humanoid agent.
        action: str
            Action name.
        value: int or None
            Parameter for rotation actions.
        timestamp: int
            Current frame timestamp.
        actions_log: list
            List to append action records: [timestamp, action_name]
        """
        if action == 'move_forward':
            self.communicator.humanoid_move_forward(humanoid.id)
            actions_log.append([timestamp, 'move_forward'])
        elif action == 'rotate_right':
            self.communicator.humanoid_rotate(humanoid.id, value, 'right')
            actions_log.append([timestamp, 'rotate_right'])
        elif action == 'rotate_left':
            self.communicator.humanoid_rotate(humanoid.id, value, 'left')
            actions_log.append([timestamp, 'rotate_left'])

    def save_video(self, images, video_path):
        """Save frames to an MP4 file using OpenCV."""
        if not images:
            print(f'⚠️ No frames to save for {video_path}.')
            return
        h, w, _ = images[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_path, fourcc, self.fps, (w, h))
        for img in images:
            if img is not None:
                out.write(img)
        out.release()
        print(f'💾 Video saved to {video_path}')

    def save_csv(self, camera_positions, humanoid_actions, cam_csv, act_csv):
        """Save camera positions and humanoid actions to CSV files."""
        with open(cam_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'camera_loc', 'camera_rot'])
            for row in camera_positions:
                writer.writerow(row)
        print(f'💾 Camera positions saved to {cam_csv}')

        with open(act_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'action'])
            for row in humanoid_actions:
                writer.writerow(row)
        print(f'💾 Actions saved to {act_csv}')
