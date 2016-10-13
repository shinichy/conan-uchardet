from conans import ConanFile, CMake
import os

username = os.getenv( '"CONAN_USERNAME', 'shinichy' )
channel = os.getenv( 'CONAN_CHANNEL', 'testing' )

class UchardetTestConan( ConanFile ):
  settings = 'os', 'compiler', 'build_type', 'arch'
  requires = 'uchardet/0.0.6@%s/%s' %  (username, channel )
  generators = 'cmake'

  def build( self ):
    cmake = CMake( self.settings )
    self.run( 'cmake "%s" %s' % ( self.conanfile_directory, cmake.command_line ) )
    self.run( 'cmake --build . %s' % cmake.build_config )

  def imports( self ):
    self.copy( '*.dll', 'bin', 'bin' )
    self.copy( '*.dylib', 'bin', 'bin' )

  def test( self ):
    os.chdir( 'bin' )
    self.run( '.%sexample' % os.sep )
