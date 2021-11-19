# Readme

A minimal reproduction example of a bad-free of a hello world c
extension compiled with clang with address sanitizer.
 
test.py works fine if you don't import pdb, but as soon as you add a
breakpoint crashes.

## How to reproduce
Define environment variable `CLANG_RT_ASAN_DYNAMIC_PATH` pointing to
`clang_rt.asan_dynamic-x86_64.dll`, e.g.
`c:/LLVM-13.0.0-win64/lib/clang/13.0.0/lib/windows/clang_rt.asan_dynamic-x86_64.dll`

Now you can call the test

    python test.py
