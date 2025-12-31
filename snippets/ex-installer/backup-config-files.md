After loading your software, you can use the `Backup config files` button to save a copy of your configuration files.

![Load software](/_static/images/ex-installer/loaded.png){ width=50% }

Either manually type the location you wish to save the configuration files to, or click the `Browse` button to select it:

![Backup config files](/_static/images/ex-installer/backup.png){ width=50% }

Once selected, click the `Backup files` button to save them to the selected location.

If you are selecting the same location as you have previously used, you will receive a warning that you are about to overwrite existing configuration files. You can either continue and overwrite them, or select a different location to retain the existing files.

![Overwrite backup config files](/_static/images/ex-installer/backup-overwrite.png){ width=50% }

!!! warning

    It is important that you do not attempt to store these files in any directory managed by EX-Installer. If you attempt to store the files there, you will receive an error that the files could not be copied.

    EX-Installer manages all files in your user home directory, typically "C:\Users\\<username\>\ex-installer" on Windows, and "/home/<username\>/ex-installer" on Linux and macOS.
