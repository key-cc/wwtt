"""
Helper script for extracting frames from the UCF-101 dataset
"""

import cv2
import glob
import os
import time
import tqdm
import datetime
import argparse
import numpy as np
import multiprocessing
# def extract_frames(video_path):
#     frames = []
#     video = av.open(video_path)
#     for frame in video.decode(0):
#         yield frame.to_image()
label_dir={'CleanAndJerk': 0, 'Diving': 1, 'PlayingFlute': 2, 'HammerThrow': 3, 'BabyCrawling': 4, 'SalsaSpin': 5, 'Drumming': 6,
           'TennisSwing': 7, 'CricketBowling': 8, 'BenchPress': 9, 'CuttingInKitchen': 10, 'PlayingCello': 11, 'PlayingPiano': 12,
           'FrontCrawl': 13, 'JumpingJack': 14, 'PlayingDhol': 15, 'Fencing': 16, 'FrisbeeCatch': 17, 'VolleyballSpiking': 18, 'Archery': 19,
           'BrushingTeeth': 20, 'TrampolineJumping': 21, 'PizzaTossing': 22, 'CliffDiving': 23, 'LongJump': 24, 'Rafting': 25,
           'BaseballPitch': 26, 'Hammering': 27, 'ParallelBars': 28, 'Lunges': 29, 'FloorGymnastics': 30, 'WritingOnBoard': 31,
           'PlayingViolin': 32, 'Bowling': 33, 'TaiChi': 34, 'HandstandWalking': 35, 'PushUps': 36, 'Nunchucks': 37,
           'SumoWrestling': 38, 'RockClimbingIndoor': 39, 'JumpRope': 40, 'Biking': 41, 'WalkingWithDog': 42, 'BlowingCandles': 43,
           'Typing': 44, 'BodyWeightSquats': 45, 'HeadMassage': 46, 'BoxingSpeedBag': 47, 'SoccerJuggling': 48, 'StillRings': 49,
           'JugglingBalls': 50, 'PullUps': 51, 'PlayingSitar': 52, 'ApplyLipstick': 53, 'Shotput': 54, 'ThrowDiscus': 55,
           'Punch': 56, 'BasketballDunk': 57, 'HandstandPushups': 58, 'UnevenBars': 59, 'Swing': 60,
           'MoppingFloor': 61, 'Rowing': 62, 'IceDancing': 63, 'Kayaking': 64, 'ShavingBeard': 65, 'BreastStroke': 66,
           'Billiards': 67, 'PlayingTabla': 68, 'HighJump': 69, 'Haircut': 70, 'CricketShot': 71, 'HulaHoop': 72,
           'BandMarching': 73, 'SkateBoarding': 74, 'BlowDryHair': 75, 'RopeClimbing': 76, 'TableTennisShot': 77,
           'Basketball': 78, 'PlayingDaf': 79, 'Surfing': 80, 'Skiing': 81, 'YoYo': 82, 'Skijet': 83, 'Mixing': 84,
           'MilitaryParade': 85, 'ApplyEyeMakeup': 86, 'SkyDiving': 87, 'PoleVault': 88, 'PlayingGuitar': 89,
           'WallPushups': 90, 'Knitting': 91, 'PommelHorse': 92, 'BoxingPunchingBag': 93, 'JavelinThrow': 94,
           'FieldHockeyPenalty': 95, 'SoccerPenalty': 96, 'GolfSwing': 97, 'HorseRace': 98, 'HorseRiding': 99, 'BalanceBeam': 100}


def get_frames(filename, n_frames=1):
    frames = []
    v_cap = cv2.VideoCapture(filename)
    v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_list = np.linspace(0, v_len - 1, n_frames + 1, dtype=np.int16)
    for fn in range(v_len):
        success, frame = v_cap.read()
        if success is False:
            continue
        if (fn in frame_list):
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame)
    v_cap.release()
    return frames, v_len

def thread_get_frames(filename, save_dir,n_frames=28):# The minimum frames = 28
    frames = []
    v_cap = cv2.VideoCapture(filename)
    v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_list = np.linspace(0, v_len - 1, n_frames + 1, dtype=np.int16)
    count=0
    for fn in range(v_len):
        success, frame = v_cap.read()
        if success is False:
            continue
        if (fn in frame_list):
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite(save_dir+os.sep+str(count)+".jpg",frame)
            count+=1
    v_cap.release()
    # return frames, v_len



prev_time = time.time()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type=str, default="G:\\gush_workspace\\OpenSourceDataset\\UCF-101", help="Path to UCF-101 dataset")
    opt = parser.parse_args()
    print(opt)
    n_frames = 28
    time_left = 0
    video_paths = glob.glob(os.path.join(opt.dataset_path, "*", "*.avi"))
    tbar_video = tqdm.tqdm(video_paths)
    threads=[]
    for i, video_path in enumerate(tbar_video):
        sequence_type, sequence_name = video_path.split(".avi")[0].split(os.sep)[-2:]
        sequence_path = os.path.join(f"{opt.dataset_path}-28frames", sequence_type, sequence_name)

        # if os.path.exists(sequence_path):
        #     continue

        os.makedirs(sequence_path, exist_ok=True)
        thread_get_frames(video_path, sequence_path,n_frames=n_frames)
    #
    #
    #     thread = multiprocessing.Process(target=thread_get_frames, args=(video_path, sequence_path))
    #     threads.append(thread)
    #     thread.start()
    # for thread in threads:
    #     thread.join()

        # frames,_ = get_frames(video_path,n_frames=n_frames)
        # for j, frame in enumerate(frames):
        # # Extract frames
        # # for j, frame in enumerate(
        # #         tqdm.tqdm(
        # #             extract_frames(video_path),
        # #             desc=f"[{i}/{len(video_paths)}] {sequence_name} : ETA {time_left}",
        # #         )
        # # ):
        # #     frame.save(os.path.join(sequence_path, f"{j}.jpg"))
        #     cv2.imwrite(os.path.join(sequence_path, f"{j}.jpg"),frame)
        # # Determine approximate time left
        # videos_left = len(video_paths) - (i + 1)
        # time_left = datetime.timedelta(seconds=videos_left * (time.time() - prev_time))
        # prev_time = time.time()
