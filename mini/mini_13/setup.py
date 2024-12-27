from setuptools import Extension, setup

setup(
    name="foreign",
    version="1.0.0",
    description="Python interface for product of matrices in C",
    author="kbn",
    author_email="pig.anishenko@gmail.com",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["foreign.c"],
        ),
    ]
)