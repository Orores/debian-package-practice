from setuptools import setup

with open('README.md','r',encoding="utf-8") as file:
    long_description = file.read()


setup(
        name = 'machine_say',
        version = '1.0.5',
        description = 'small python package to make machine say something',
        long_description = long_description,
        long_description_content_type = "text/markdown",
        author = 'orores',
        author_email = 'orores@orores.com',
        url = 'orores.com',
        license = 'MIT',
        packages = ['machine_say'],
        package_dir = {'machine_say':'machine_say/'},
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            ],
        entry_points = {
            'console_scripts' : ['machine_say=machine_say.machine:main']
            },
        data_files = [
            ('share/applications/', ['machine_say.desktop'])
                ],
        keywords = 'machines says something',
        python_requires = ">=3.6",
        )





