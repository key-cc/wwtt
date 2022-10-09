# import os
# import shutil
# import glob as gb
#
# import cv2
#
# # pred_image_files = gb.glob("H:\\FishPointerData\\img0923_check_result\\defect_image_check\\9"+os.sep+"*.png")
# dst_dir ="H:\\FishPointerData\\22-09-filter9"
# # if os.path.exists(dst_dir):
# #     shutil.rmtree(dst_dir)
# # os.makedirs(dst_dir)
# # for pred_image_file in pred_image_files:
# #     pred_image = cv2.imread(pred_image_file,0)
# #     image_height,image_width = pred_image.shape
# #     contours, hierarchy = cv2.findContours(pred_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #     for c in contours:
# #         x, y, w, h = cv2.boundingRect(c)
# #         # if 0.33*image_width < x < 0.66*image_width and y > 0.5 * image_height:
# #         if y > 0.5 * image_height:
# #             shutil.copyfile(pred_image_file, dst_dir+os.sep+os.path.basename(pred_image_file))
# #             shutil.copyfile(pred_image_file.replace("png","jpg"),
# #                             dst_dir+os.sep+os.path.basename(pred_image_file).replace("png","jpg"))
#
# pred_image_files = gb.glob(dst_dir+os.sep+"*.png")
# for pred_image_file in pred_image_files:
#     try:
#         pred_image = cv2.imread(pred_image_file,0)
#         image_height,image_width = pred_image.shape
#         contours, hierarchy = cv2.findContours(pred_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         for c in contours:
#             x, y, w, h = cv2.boundingRect(c)
#             if 0.2 *image_width < x < 0.8*image_width:
#                 os.remove(pred_image_file)
#                 os.remove(pred_image_file.replace("png","jpg"))
#                 print(f"delete error file {pred_image_file}")
#     except Exception as e:
#         print(pred_image_file,e)
# org_image_files = gb.glob(dst_dir+os.sep+"*.jpg")
# for org_image_file in org_image_files:
#     if not os.path.exists(org_image_file.replace(".jpg",".png")):
#         os.remove(org_image_file)
#
#
