import setuptools

setuptools.setup(
    name='env2json',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
