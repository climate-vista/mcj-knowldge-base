from setuptools import setup, find_packages

setup(
    name='my-python-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        # For example:
        # 'numpy==1.15.4',
        # 'pandas==0.23.4',
    ],
    entry_points={
        'console_scripts': [
            # Add any console scripts here
            # For example:
            # 'my-script = my_python_project.main:main',
        ],
    },
)