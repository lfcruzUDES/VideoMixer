from setuptools import setup, find_packages

setup(
    name="VideoMixer",
    version="0.1",
    description="Join videos",
    author="Luis Fernando Cruz Carrillo",
    author_email='lfcruz@udes.edu.mx',
    license="GPL",
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    entry_points=""" 
        [console_scripts]
        mixer_conf=mixer.scripts.general_conf:cli
    """,
)
