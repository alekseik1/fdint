# FOR POETRY ONLY
import os
import shutil
from distutils.command.build_ext import build_ext
from pathlib import Path

import numpy
from Cython.Build import cythonize
from setuptools import Distribution, Extension

ext = ".pyx"
basedir = Path(__file__).absolute().parent


# This function will be executed in setup.py:
def build():
    # The file you want to compile
    extensions = [
        Extension(
            "fdint._fdint",
            [str(basedir / "fdint/_fdint.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.fd",
            [str(basedir / "fdint/fd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.dfd",
            [str(basedir / "fdint/dfd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.ifd",
            [str(basedir / "fdint/ifd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.gfd",
            [str(basedir / "fdint/gfd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.dgfd",
            [str(basedir / "fdint/dgfd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
        Extension(
            "fdint.scfd",
            [str(basedir / "fdint/scfd.pyx")],
            include_dirs=[numpy.get_include()],
        ),
    ]

    distribution = Distribution(
        {"name": "extended", "ext_modules": cythonize(extensions)}
    )
    distribution.package_dir = "extended"

    cmd = build_ext(distribution)
    cmd.ensure_finalized()
    cmd.run()

    # Copy built extensions back to the project
    for output in cmd.get_outputs():
        relative_extension = os.path.relpath(output, cmd.build_lib)
        shutil.copyfile(output, relative_extension)
        mode = os.stat(relative_extension).st_mode
        mode |= (mode & 0o444) >> 2
        os.chmod(relative_extension, mode)


if __name__ == "__main__":
    build()
