import os
import os.path as osp
from time import strftime, localtime


def get_time_identifier():
    return strftime("%Y-%m-%d_%H:%M", localtime())


def make_uploading_record(identifier: str):
    template = "Upload_{}.txt"
    record_dir = osp.join(osp.dirname(osp.abspath(__file__)), "upload_history")
    record_path = os.path.join(record_dir, template.format(identifier))

    return record_path