from setuptools import find_packages, setup
setup(
    name='doceye',
    packages=find_packages(include=['doceye']),
    version='0.1.0',
    description='tesseract Py',
    author='Me',
    license='MIT',
    install_requires=['opencv-python==4.5.1.48','Pillow==8.2.0','pytesseract==0.3.7'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    )

