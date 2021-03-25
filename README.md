# PyS3Upload
need to add `logging_setup.py` at current directory


## Usage

```python
from PyS3Upload.PyS3Uploader import S3Uploader
from PyS3Upload.helper import get_time_identifier



REMOVE_LOCAL_AFTER_UPLOAD = True

time_identifier: str = get_time_identifier()
s3Uploader = S3Uploader(path_identifier=time_identifier, dir="margin_project/KidFace")

filepath = shutil.make_archive(base_name="images", format='tar', root_dir=img_root_dir)

upload_res = s3Uploader.upload_file(input_filename=filepath, remove=True)

if upload_res == 0:
    if REMOVE_LOCAL_AFTER_UPLOAD:
        "S3uploader only remove the .tar files, here we delete the individual images"
        shutil.rmtree(img_root_dir)


```

