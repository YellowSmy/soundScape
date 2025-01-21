import os, uuid
import hashlib

## Static folder create function seperated by User
def user_dir_path(instance, filename):
    """
    파일경로: media/<basename>/<user_email_hash>/<filename>
    """
    email_hash = hashlib.sha256(instance.user.email.encode()).hexdigest()

    ext = filename.split('.')[-1]
    unique_filename = f"profileImg.{ext}"
    Dir_path = os.path.join('profiles', 'images', email_hash, unique_filename)

    return Dir_path