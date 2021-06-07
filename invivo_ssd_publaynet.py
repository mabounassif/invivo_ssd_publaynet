# The new confcig inherits a base config to highlight the necessary modification
_base_ = 'ssd/ssd512_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(
        num_classes=5
    ))

# Modify dataset related settings
dataset_type = 'CocoDataset'
classes = ('text', 'title', 'list', 'table', 'figure')
checkpoint_config = dict(  # Config to set the checkpoint hook, Refer to https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/hooks/checkpoint.py for implementation.
    interval=500,
    max_keep_ckpts=5,
    by_epoch=False)  # The save interval is 1
data = dict(
    # samples_per_gpu=24,
    # workers_per_gpu=12,
    train=dict(
        type=dataset_type,
        img_prefix='data/publaynet/train/',
        classes=classes,
        ann_file='data/publaynet/train.json'),
    val=dict(
        img_prefix='data/publaynet/val/',
        classes=classes,
        ann_file='data/publaynet/val.json'),
    test=dict(
        img_prefix='data/publaynet/val/',
        classes=classes,
        ann_file='data/publaynet/val.json'))
# total_epochs = 12
# lr_config = dict(
#     warmup_ratio=1.0 / 10,
# )
optimizer = dict(type='SGD', lr=2e-4, momentum=0.9, weight_decay=5e-5)
# load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
resume_from = './work_dirs/invivo_ssd_publaynet/latest.pth'
