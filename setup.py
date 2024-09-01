from setuptools import setup,  find_packages
setup(
    name='bakchodbot',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Only for bakchodi',
    install_requires=['chainlit','openai'],
    author='vishvesh',
    author_email='vishveshjain@outlook.com'
)

# 1. find_packages
# 2. setup()
# 3. readme.md
# 4. install_requires