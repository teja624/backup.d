""" backup.d/vars.py

This Python script defines variables for use by migrate.py.
Define some critical vars.  These need to be modified for each project!  Use 'drush status' to determine some values.

Customized 26-Apr-2017 to restore a backup from @rootstalk.prod to @rootstalk.dev.

"""

backup = "rootstalk.tar.gz"                                       # name the backup file
stick = "/Volumes/RS"                                             # name of a mounted drive to accept a copy of the backup
server = "rootstalk.grinnell.dev"                                 # the remote server name
backup_server = "rootstalk.grinnell.edu"                          # the remote server that the backup came from
user = "vagrant"                                                  # admin user on the remote server
drush_alias = "@rootstalk.dev"                                    # drush alias for the remote site
web_path = "/var/www/drupal/web/"                                 # path to the Drupal web root on the remote server
site_path = web_path + "sites/default"                            # path to the Drupal site on the remote server
drush = "/var/www/drupal/vendor/drush/drush/drush.php"            # remote server path to drush

