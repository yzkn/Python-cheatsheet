import subfile
subfile.hello()

import subdir.main
subdir.main.hello()

from subdir import main
main.hello()

import subdir.subfile
subdir.subfile.hello()
