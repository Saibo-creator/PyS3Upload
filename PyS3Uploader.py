import os
from logging_setup import logger

class S3Uploader:

    def __init__(self, bucket: str = None, dir="margin_project/wiki_image_test", path_identifier: str = ""):
        if bucket:
            self.bucket = bucket
        else:
            self.bucket = "s3://eu.privately.datascience.datasets"
        self.output_dir = dir
        self.path_identifier = path_identifier
        self.METADATA = "metadata"

    def upload_file(self, input_filename: str, output_filename: str = None, input_dir: str = "", as_metadata=False,
                    remove=False):
        """
        :param remove:
        :param input_dir:
        :param input_filename:
        :param output_filename:
        :param as_metadata:
        :param bucket:
        :return: res=0 means success
        """

        logger.info("start to upload {} to server".format(input_filename))

        if output_filename is None:
            output_filename = os.path.basename(input_filename)
        input_filepath = os.path.join(input_dir, input_filename).replace(" ", "\ ")

        if as_metadata:
            output_filepath = os.path.join(self.bucket, self.output_dir, self.path_identifier, self.METADATA,
                                           output_filename)
        else:
            output_filepath = os.path.join(self.bucket, self.output_dir, self.path_identifier, output_filename)
        # res = os.system("s3cmd put {} {}".format(input_filepath, output_filepath))

        command = "s3cmd put {} {}".format(input_filepath, output_filepath)
        res = os.system(command)

        if res == 0:
            logger.info("S3upload {} successfully".format(input_filename))
            if remove:
                os.remove(os.path.join(input_dir, input_filename))
        else:
            logger.info("S3upload {} failed".format(input_filename))

        logger.info("finish to upload {}".format(input_filename))

        return res

