from PIL import Image
import glob
import os
import cv2
from itertools import combinations as c
import os
import shutil
dir = "/home/oem/hang/Nail_fold/dataset_concat/original/diabetes/"
des = "/home/oem/hang/Nail_fold/dataset_concat/data_concat_9x1/diabetes"
# images = glob.glob(dir)
def concat_tile_size(list_2d, interpolation = cv2.INTER_CUBIC):
    img_list_v = [hconcat_resize(list_h, interpolation = cv2.INTER_CUBIC) for list_h in list_2d]
    return vconcat_resize(img_list_v, interpolation = cv2.INTER_CUBIC)
def vconcat_resize(img_list, interpolation  = cv2.INTER_CUBIC):
    w_min = min(img.shape[1] for img in img_list)
    im_list_resize =[cv2.resize(img, (w_min, int(img.shape[0] * w_min /img.shape[1])), interpolation = interpolation) for img in im_list]
    return cv2.vconcat(im_list_resize)
def hconcat_resize(img_list, interpolation  = cv2.INTER_CUBIC):
    h_min = min(img.shape[0] for img in img_list)
    im_list_resize =[cv2.resize(img, (int(img.shape[0] * h_min /img.shape[1]),h_min), interpolation = interpolation) for img in im_list]
    return cv2.hconcat(im_list_resize)
def concat_vh(list_2d):
    return cv2.vconcat([cv2.hconcat(list_h) for list_h in list_2d])

for dirname, subdir, files in os.walk(dir):
    # print("os",os.path.basename(dirname[2:]))
    dic = os.path.basename(dirname[2:])
    # print(dic)
    # print("sub",subdir)
    # print("files",files)
    path = os.path.join(dir, dirname)
    # print(path)
    images = []
    for file in files:
        image = os.path.join(path, file)
        images.append(image)
    im_list = []
    path_list = []
    for im_id, im_path in enumerate(images):
        im_list.append(im_id)
        path_list.append(im_path)
    already_seen = set()
    result = set()
    all_combos = c(im_list,16)
    print(all_combos)
    for combo in all_combos:
        pairs = set(c(combo, 3))
        print(pairs)
        if not pairs & already_seen:
            result.add(combo)
            already_seen.update(pairs)
    for i in list(result):
        com_list = list(i)
        img_list = []
        for j in list(com_list):
            img = cv2.imread(path_list[j])
            img_list.append(img)
        print(img_list)
        #3x3
        # im_concat = concat_vh([[img_list[0], img_list[1], img_list[2]],
        #                        [img_list[3], img_list[4], img_list[5]],
        #                        [img_list[6], img_list[7], img_list[8]]])
        #1x9
        #im_concat = cv2.hconcat([img_list[0], img_list[1], img_list[2], img_list[3], img_list[4], img_list[5], img_list[6], img_list[7], img_list[8]])
        #im_concat = cv2.hconcat([img_list[0], img_list[1], img_list[2], img_list[3]])
        #3x3
        #im_concat = concat_vh([[img_list[0], img_list[1], img_list[2]],
        #                        [img_list[3], img_list[4], img_list[5]],
        #                        [img_list[6], img_list[7], img_list[8]]])
        #4x4
        #im_concat = concat_vh([[img_list[0], img_list[1], img_list[2], img_list[3]],
        #                       [img_list[4], img_list[5], img_list[6], img_list[7]],
        #                       [img_list[8], img_list[9], img_list[10], img_list[11]],
        #                       [img_list[12], img_list[13], img_list[14], img_list[15]]])
             #9x1
        im_concat = cv2.vconcat([img_list[0], img_list[1], img_list[2], img_list[3], img_list[4], img_list[5], img_list[6], img_list[7], img_list[8]])

        print(im_concat)
        cv2.imwrite(f'{des}/concat_h_{dic}_{i}.jpg', im_concat)

