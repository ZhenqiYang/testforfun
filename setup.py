from setuptools import setup

setup(name="systeminfo",
    version="0.1",
    description="Bascic system information for Comp30670",
    url="",
    author="Archie Young",
    author_email="zhenqi.yang@ucdconnect.ie",
    licence="GPL3",
    packages=['systeminfo'],
    entry_points={
    'console_scripts':['comp30830_systeminfo=systeminfo.main:main']
    }
     ) 