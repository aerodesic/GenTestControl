from DistUtilsExtra.auto import setup
from distutils.command.install import install
import os

PACKAGE="gentestcontrol"
VERSION="1.0"

# In case we need hooks
class post_install(install):
    def run(self):
        install.run(self)

setup(
    name              = PACKAGE,
    author            = "Gary Oliver",
    author_email      = "go@robosity.com",
    url               = "https://www.robosity.com",
    version           = VERSION,
    packages          = [ "gentestcontrol" ],
    scripts           = [ "scripts/GenTestControl" ],
    license           = "Copyright 2021, Gary Oliver",
    description       = "Generator Test main control",
    long_description  = open("README.md").read(),
    data_files        = [
        ("share/GenTestDisplay",             [ "extra/license", ] ),
    ],
    cmdclass = { 'install': post_install },
)
