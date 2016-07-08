from setuptools import setup, find_packages

setup(name='ninfo-plugin-flow_indexer',
    version='0.0.2',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
        "requests>=2.0",
    ],
    entry_points = {
        'ninfo.plugin': [
            'flow_indexer      = ninfo_plugin_flow_indexer',
        ]
    }
) 
