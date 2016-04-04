from setuptools import setup

setup(
    name='glot',
    version='0.1',
    packages=['glot'],
    package_dir={'glot': 'src/glot'},

    description='CLI manager for Glossia',
    author='NUMA Engineering Services Ltd.',
    author_email='phil.weir@numa.ie',
    url='http://gosmart-project.eu/',

    scripts=[
        'scripts/glot',
    ],

    install_requires=[
        'aiohttp',
        'Click',
        'gitpython',
        'tabulate',
        'colorama',
        'glossia.comparator'
    ]
)
