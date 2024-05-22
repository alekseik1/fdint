# FOR POETRY ONLY
# https://stackoverflow.com/a/63679316/5183539
try:
    from Cython.Build import cythonize
# Do nothing if Cython is not available
except ImportError:
    # Got to provide this function. Otherwise, poetry will fail
    def build(setup_kwargs):
        pass
# Cython is installed. Compile
else:
    from setuptools import Extension, setup
    import numpy

    ext = ".pyx"

    # This function will be executed in setup.py:
    def build(setup_kwargs):
        # The file you want to compile
        extensions = [
            Extension("fdint._fdint", ["fdint/_fdint" + ext]),
            Extension("fdint.fd", ["fdint/fd" + ext]),
            Extension("fdint.dfd", ["fdint/dfd" + ext]),
            Extension("fdint.ifd", ["fdint/ifd" + ext]),
            Extension("fdint.gfd", ["fdint/gfd" + ext]),
            Extension("fdint.dgfd", ["fdint/dgfd" + ext]),
            Extension("fdint.scfd", ["fdint/scfd" + ext]),
        ]

        # read in __version__
        exec(open("fdint/version.py").read())

        metadata = dict(
            name="fdint",
            version=__version__,  # read from version.py
            description="A free, open-source python package for quickly and "
            "precisely approximating Fermi-Dirac integrals.",
            long_description=open("README.rst").read(),
            url="http://scott-maddox.github.io/fdint",
            author="Scott J. Maddox",
            author_email="smaddox@utexas.edu",
            license="BSD",
            packages=["fdint", "fdint.tests", "fdint.examples"],
            package_dir={"fdint": "fdint"},
            data_files=[
                "fdint/__init__.pxd",
                "fdint/_fdint.pxd",
                "fdint/scfd.pxd",
            ],
            test_suite="fdint.tests",
            setup_requires=["numpy"],
            install_requires=["numpy"],
            #     zip_safe=True,
            #     use_2to3=True,
            include_dirs=[numpy.get_include()],
        )
        metadata["ext_modules"] = cythonize(extensions)
        setup(**metadata)
