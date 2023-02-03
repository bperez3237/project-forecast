from setuptools import setup

setup(
    name='project_name',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author='Brian Perez',
    author_email='b.perez3237@gmail.com',
    url='https://github.com/bperez3237/project-forecast',
    # packages=find_packages(where='src'),
    package_dir={'': 'src'},
    # install_requires=[
    #     'dependency1',
    #     'dependency2',
    #     ...
    # ],
)