from subprocess import run
import sys
from pathlib import Path
import os

r"""
When building a c extension the follwoing commands are called on windows.
This script tries to do the same but with clang.

C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\cl.exe
    /c
    /nologo
    /Ox
    /W3
    /GL
    /DNDEBUG
    /MD
    -IC:\s\eklang\venv\py39\include
    -IC:\Python39\include
    -IC:\Python39\include
    -IC:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\ATLMFC\include
    -IC:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\include
    -IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um
    -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\ucrt
    -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\shared
    -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\um
    -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\winrt
    -IC:\Program Files (x86)\Windows Kits\10\include\10.0.19041.0\cppwinrt
    /Tchello.c
    /Fobuild\temp.win-amd64-3.9\Release\hello.obj
C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\bin\HostX86\x64\link.exe
    /nologo
    /INCREMENTAL:NO
    /LTCG
    /DLL
    /MANIFEST:EMBED,ID=2
    /MANIFESTUAC:NO
    /LIBPATH:C:\s\eklang\venv\py39\libs
    /LIBPATH:C:\Python39\libs
    /LIBPATH:C:\Python39
    /LIBPATH:C:\s\eklang\venv\py39\PCbuild\amd64
    /LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\ATLMFC\lib\x64
    /LIBPATH:C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.29.30133\lib\x64
    /LIBPATH:C:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\lib\um\x64
    /LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.19041.0\ucrt\x64
    /LIBPATH:C:\Program Files (x86)\Windows Kits\10\lib\10.0.19041.0\um\x64
    /EXPORT:PyInit_hello build\temp.win-amd64-3.9\Release\hello.obj
    /OUT:build\lib.win-amd64-3.9\hello.cp39-win_amd64.pyd
    /IMPLIB:build\temp.win-amd64-3.9\Release\hello.cp39-win_amd64.lib

"""
def main():
    in_github = os.environ.get("GITHUB_PATH")
    py_prefix = Path(sys.exec_prefix) if in_github else Path("c:/Python39")
    py_include = py_prefix / "include"
    py_libs = py_prefix / "libs"

    assert (py_include / "Python.h").exists()
    cmd = (f"clang -I{py_include} "
           " -Wno-everything "
           " -c hello.c -o hello.o ")
    print(cmd)
    run(cmd, check=True, shell=True)

    cmd = (" clang --shared "
           f" -L{py_libs} "
           " -Wno-everything "
           " -shared-libsan -fsanitize=address "
           " hello.o -shared -o hello.pyd ")
    print(cmd)
    run(cmd, check=True, shell=True)


if __name__ == '__main__':
    main()
