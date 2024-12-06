import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hmvpack-NG",
    version="0.0.3",
    author="Nikhil Gupta",
    author_email="ngupta_be17@thapar.edu",
    description="Handling missing values in python",
	url='https://github.com/CachingNik/HMV-Pack',
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['HMVcli=hmvlib.hmvcli:main'],
    },
	keywords = ['CLI', 'missing', 'Data', 'HMV'], 
	python_requires='>=2.7', 
)
