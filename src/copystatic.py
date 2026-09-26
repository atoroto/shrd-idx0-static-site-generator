import os
import shutil


def copy_static_to_public(src_path, dst_path):
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)

    def logged_copy(src_file, dst_file):
        print(f"Copying {src_file} -> {dst_file}")
        return shutil.copy(src_file, dst_file)

    shutil.copytree(src_path, dst_path, copy_function=logged_copy)
