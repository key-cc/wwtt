from models import Encoder
import numpy as np
import glob as gb
import tqdm
import os
import cv2
import PIL
from PIL import Image
import torchvision.transforms as transforms
import custom_transform as tr
mean = np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
transform = transforms.Compose(
            [
                tr.FixScaleCrop(crop_size=224),
                # transforms.Resize(input_shape[-2:], Image.BICUBIC),
                transforms.ToTensor(),
                transforms.Normalize(mean, std),
            ]
)

feat_extractor = Encoder(latent_dim=512)
dataset_path = "G:\\gush_workspace\\OpenSourceDataset\\UCF-101"
video_paths = gb.glob(os.path.join(dataset_path, "*", "*.avi"))
tbar_video = tqdm.tqdm(video_paths)
threads=[]
sequence_length = 16
count= 0
for i, video_path in enumerate(tbar_video):
    sequence_type, sequence_name = video_path.split(".avi")[0].split(os.sep)[-2:]
    sequence_path = os.path.join(f"{dataset_path}-28frames", sequence_type, sequence_name)
    image_paths = sorted(gb.glob(sequence_path + os.sep + "*.jpg"))
    if len(image_paths) <28:
        print(sequence_path,len(image_paths))
        count+=1
print(f"total video num :{count}")
    # sample_interval = np.random.randint(1, len(image_paths) // sequence_length + 1)
    # start_i = np.random.randint(0, len(image_paths) - sample_interval * sequence_length + 1)
    #
    # # Extract frames as tensors
    # image_sequence = []
    # for i in range(start_i, len(image_paths), sample_interval):
    #     if sequence_length is None or len(image_sequence) < sequence_length:
    #
    #         image = Image.open(image_paths[i])
    #         image_tensor = transform(image)
