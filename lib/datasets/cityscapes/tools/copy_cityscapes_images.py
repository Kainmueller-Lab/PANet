import os
import glob

target = '/home/maisl/workspace/panet/PANet/data/cityscapes/images'
#source = '/home/maisl/data/cityscapes/leftImg8bit_trainvaltest/leftImg8bit'
source = '/home/maisl/data/cityscapes/gtFine_trainvaltest/gtFine'
sets = ['train', 'val', 'test']

for set in sets:
    images = glob.glob(os.path.join(source, set) + '/*/*instanceIds.png')
    for image in images:
        cmd = 'cp ' + image + ' ' + os.path.join(target, set)
        os.system(cmd)

