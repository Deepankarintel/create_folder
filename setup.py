from setuptools import setup

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='FTP',
      version='1.0.3',
      description='A small code to create folders and subfolders',
      long_description=long_description,
      url='https://github.com/Deepankarintel/create_folder',
      author='Deepankar',
      author_email='deepankar.borgohainx@gmail.com',
      license='MIT',
      packages=['FTP'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='Create Folders'
      )
