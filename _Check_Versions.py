##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import qprompt
import verace

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

VERCHK = verace.VerChecker("Auxly", __file__)
VERCHK.include(r"lib\setup.py", match="version = ", delim='"')
VERCHK.include(r"lib\auxly\_modu.py", match="__version__ = ", delim='"')
VERCHK.include(r"CHANGELOG.adoc", match="auxly-", delim="-", delim2=" ", updatable=False)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    VERCHK.run()
    if qprompt.ask_yesno("Update version?", dft="n"):
        newver = qprompt.ask_str("New version string")
        if newver:
            VERCHK.update(newver)
            VERCHK.run()
            qprompt.pause()
