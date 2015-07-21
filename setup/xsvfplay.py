from distutils.core import setup
import py2exe

setup(windows=[{"script":"xsvfplay.py"}], 
      name='XSVFPlay FPGA Programming Tool',
      description='XSVFPlay Programming Tool',
      author='Superna (c) 2015',
      author_email='superna9999@gmail.com',
      options = {'py2exe': {'includes': ["sip", 'msvcrt'],
                            'excludes': ['FCNTL', 'TERMIOS', 'javax.comm'],
							'dll_excludes': ["MSVCP90.dll"]	
                           } 
                },
	  packages=['ui']
      )

