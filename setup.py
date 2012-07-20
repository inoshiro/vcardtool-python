from setuptools import setup

entry_points = {
    'console_scripts':[
        'vcardtool = vcardtool:main'
    ]
}

setup(name='vcardtool',
      version='0.0.1',
      author='Kenjiro Kosaka',
      author_email='inoshirou@gmail.com',
      url='https://github.com/inoshiro/vcardtool-python',
      py_modules=['vcardtool'],
      install_requires=['vobject'],
      entry_points=entry_points)
