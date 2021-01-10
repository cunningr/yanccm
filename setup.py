from distutils.core import setup

setup(
    name='NetconfConfigurationManager',
    packages=[
        'controller',
        'sot',
        'ncservice',
        'ncservice.configDb',
        'ncservice.ncDeviceOps',
        'ncservice.ncDeviceOps.threaded',
        'view'],
    version='0.0.1',
    license='MIT',
    description='Netconf Configuration Manager is multithreaded configuration manger for network devices that '
                'leverages the Netconf protocol',
    author='Richard Cunningham',
    author_email='cunningr@gmail.com',
    url='https://github.com/cunningr/dna_workflows',
    download_url='https://github.com/cunningr/dna_workflows',
    keywords=['Netconf', 'Cisco', 'configuration management'],
    install_requires=[
        'ncclient',
        'lxml',
        'pyyaml',
        'pymongo'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points={
        'console_scripts': [
            'yanccm = controller.cli:main'
        ]
    }
)
