#!/usr/bin/env python3

import sys
import os
from dropbox import Dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


def upload(path, token):
    dbx = Dropbox(token)
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            'ERROR: Invalid Dropbox access token; try re-generating it at https://www.dropbox.com/developers/apps'
        )
    with open(path, 'rb') as f:
        try:
            dbx.files_upload(
                f.read(),
                '/' + os.path.basename(path),
                mode=WriteMode('overwrite'))
        except ApiError as err:
            if (err.error.is_path()
                    and err.error.get_path().error.is_insufficient_space()):
                sys.exit('ERROR: Cannot upload file - insufficient space.')
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('USAGE: %s <file to upload>' % sys.argv[0])

    upload(sys.argv[1], os.environ['DROPBOX_TOKEN'])
