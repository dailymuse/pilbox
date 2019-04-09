import os.path

from setuptools import setup, Command


with open('README.rst') as f:
    readme = f.read()


class PilboxTest(Command):
    user_options=[]
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call(
            [sys.executable, os.path.join('pilbox', 'test', 'runtests.py')])
        raise SystemExit(errno)


setup(name='pilbox',
      version='2.1.3',
      description='Pilbox is an image processing application server built on the Tornado web framework using the Pillow Imaging Library',
      long_description=readme,
      classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        ],
      url='https://github.com/agschwender/pilbox',
      author='Adam Gschwender',
      author_email='adam.gschwender@gmail.com',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      include_package_data=True,
      packages=['pilbox'],
      package_data={
        'pilbox': ['frontalface.xml'],
        },
      install_requires=[
        'tornado==4.5.1',
        'Pillow==2.9.0',
        'muselog>=1.8.4'
        ],
      extras_require = {
          'Proxy': ['pycurl'],
          'Facial Recognition': ['cv']
      },
      zip_safe=True,
      cmdclass={'test': PilboxTest},
      entry_points = {'console_scripts': ['pilbox = pilbox.app:main']}
      )
