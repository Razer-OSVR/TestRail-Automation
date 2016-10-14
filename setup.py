import sys
from cx_Freeze import setup, Executable

include_files = ['defaults.cfg']
build_deps = {"includes": ["argparse", "helpers", "TestRail", "os",
                           "dummy_threading", "urllib"],
              "include_files": include_files}

setup(
	name = "OSVR TestRail automation",
	version = "1.0",
	description = "CMD that can be used to update TestRail test cases.",
	options = {"build_exe": build_deps},
	executables = [Executable("main.py", base = None)])
