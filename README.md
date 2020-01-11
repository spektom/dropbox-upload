dropbox-upload
==============

Script for uploading files to Dropbox.


### Prerequisites ###

 * Python3
 * For Python dependencies, see `requirements.txt`
 * Create a [Dropbox app](https://www.dropbox.com/developers/apps), and acquire its access token.
 

### Running ###

    DROPBOX_TOKEN=<Your App's Token> ./dropbox-upload.py /path/to/<File to upload>

Please note that:

 * Existing files are overwritten.
 * Uploaded files are placed under `/Apps/<Dropbox App Name>/`

