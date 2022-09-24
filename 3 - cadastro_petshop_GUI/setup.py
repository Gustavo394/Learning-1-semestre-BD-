import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("cadastro_petshop.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)

setup(
    name = "cadastro_petshop",
    version = "1.0",
    description = "cadastro_petshop",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
