from setuptools import setup

setup(
    name='forecastio',
    version='0.0.1',
    description='Script to pull darksky API and report to InfluxDB',
    author='Dan Kolb',
    author_email='dan@dankolb.net',
    url='https://github.com/dankolbrs/forecastio.git',
    packages=['lib'],
    install_requires=open('requirements.txt').read(),
    tests_require=open('test_requirements.txt').read(),
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Programming Language :: Python'
        ],
    entry_points={
        'console_scripts': [
            'forecastio = forecast:main'
        ]
    }
)
