from setuptools import setup, find_packages

setup(
    name='operator-csv-libs',
    version='0.0.0',
    description='Code to manage OLM related CSVs and channels',
    author='bennett-white',
    url='https://github.com/multicloud-ops/operator-csv-libs',
    packages=['operator_csv_libs'],
    install_requires=[
        'pyyaml==6.0',
        'pygithub==1.58.0',
        'dohq-artifactory==0.8.4',
        'requests==2.27.1'
    ]
)
