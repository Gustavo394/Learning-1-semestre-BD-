import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("cor_roupa.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)

setup(
    name = "cor_roupa",
    version = "1.0",
    description = "verificador",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
