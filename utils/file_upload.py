import os, uuid

## Static folder create function seperated by User
def user_dir_path(instance, filename):
    """
    파일경로: media/<basename>/<user_email>/<filename>
    """
    ext = filename.split('.')[-1]
    unique_filename = f"profileImg.{ext}"
    Dir_path = os.path.join('profiles', 'images', instance.user.email, unique_filename)

    return Dir_path