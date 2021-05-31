import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name='twarc-videos',
    version='0.0.6',
    url='https://github.com/docnow/twarc-videos',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    py_modules=['twarc_videos'],
    description='A twarc plugin to extract referenced video from tweet data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.3',
    install_requires=['twarc>=2.1.1', 'youtube_dl', 'click'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'python-dotenv'],
    entry_points='''
        [twarc.plugins]
        ids=twarc_videos:videos
    '''
)
