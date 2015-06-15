import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]
includefiles = ['images/', 'sounds/', 'fonts/']

cx_Freeze.setup(
    name="CrazyAnts",
    options={"build_exe": {"packages":["pygame", "os"],
                           "include_files":includefiles}},
    executables = executables

    )
