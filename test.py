import win32api
import build

build.main()  # builds hello.pyd with clang


import os
# Here you need your llvm installation path
try:
  clang_rt_asan_dyn = os.environ['CLANG_RT_ASAN_DYNAMIC_PATH']
except KeyError as e:
    example = "c:/LLVM-13.0.0-win64/lib/clang/13.0.0/lib/windows/clang_rt.asan_dynamic-x86_64.dll"
    raise RuntimeError(("Missing environment variable CLANG_RT_ASAN_DYNAMIC_PATH "
                        f"e.g. set CLANG_RT_ASAN_DYNAMIC_PATH={example}")) from e

succeded = win32api.LoadLibrary(clang_rt_asan_dyn)
if not succeded:
    raise RuntimeError("failed to load clang_rt.asan_dynamic-x86_64.dll")

import hello
print(hello.system())

# Comment the following line and asan will not complain
import pdb; pdb.set_trace()

# if you comment the previous line, install numpy
# the same happens when you import it:
# Address 0x0242209973b0 is a wild pointer inside of access range of size 0x000000000001.
# SUMMARY: AddressSanitizer: bad-free (clang\bin\LLVM-13.0.0-win64\lib\clang\13.0.0\lib\windows\clang_rt.asan_dynamic-x86_64.dll+0x180037f31)
# ==21264==ABORTING
# import numpy
