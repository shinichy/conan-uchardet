from conans import ConanFile, CMake
from conans.tools import download, unzip
import os

class UchardetConan( ConanFile ):
  name = 'uchardet'
  version = '0.0.6'
  license = 'MOZILLA PUBLIC LICENSE Version 1.1 https://cgit.freedesktop.org/uchardet/uchardet/plain/COPYING'
  url = 'https://github.com/silkedit/conan-uchardet'
  settings = 'os', 'compiler', 'build_type', 'arch'
  generators = 'cmake'
  folder = '%s-%s' % ( name, version )

  def source( self ):
    zip_name = 'uchardet-%s.zip' % ( self.version )
    download( 'https://cgit.freedesktop.org/uchardet/uchardet/snapshot/%s' % zip_name, zip_name )
    unzip( zip_name )
    os.unlink( zip_name )

  def build( self ):
    cmake = CMake( self.settings )
    flags = '-DCMAKE_OSX_DEPLOYMENT_TARGET=10.7 -DCMAKE_MACOSX_RPATH=ON -DBUILD_BINARY=OFF'
    self.run('cd %s && mkdir _build' % self.folder)
    configure_command = 'cd %s/_build && cmake .. %s' % ( self.folder, cmake.command_line )
    self.output.info( 'Configure with: %s' % configure_command )
    self.run( 'cd %s/_build && cmake .. %s %s' % ( self.folder, cmake.command_line, flags ) )
    self.run( "cd %s/_build && cmake --build . %s" % ( self.folder, cmake.build_config ) )

  def package( self ):
    self.copy( 'uchardet.h', dst='include/uchardet', src='%s/src' % self.folder )
    self.copy( '*uchardet*.lib', dst='lib', keep_path=False )
    self.copy( '*uchardet*.dll', dst='bin', keep_path=False )
    self.copy( '*uchardet*.so', dst='lib', keep_path=False )
    self.copy( '*uchardet*.a', dst='lib', keep_path=False )

  def package_info( self ):
    self.cpp_info.libs = ['uchardet']
