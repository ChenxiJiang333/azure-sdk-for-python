# tsp-client update failed when generating Python SDK
## question
I've updated my TypeSpec PR (link: ([Conv Authoring] modify Python clientname 20250515preview)[https://github.com/Azure/azure-rest-api-specs/pull/36074]) and am using the latest commit ID to generate the Python SDK via tsp-client update. However, the command consistently fails with the following error:

npm warn cleanup Failed to remove some directories [
npm warn cleanup   [
npm warn cleanup     '\\\\?\\C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec\\compiler',
npm warn cleanup     [Error: EPERM: operation not permitted, rmdir 'C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@typespec\compiler\dist\src\core'] {
npm warn cleanup       errno: -4048,
npm warn cleanup       code: 'EPERM',
npm warn cleanup       syscall: 'rmdir',
npm warn cleanup       path: 'C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec\\compiler\\dist\\src\\core'      
npm warn cleanup     }
npm warn cleanup   ],
npm warn cleanup   [
npm warn cleanup     '\\\\?\\C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec',
npm warn cleanup     [Error: EPERM: operation not permitted, rmdir 'C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@typespec\http-client-python\generator\build\lib\pygen\codegen'] {
npm warn cleanup       errno: -4048,
npm warn cleanup       code: 'EPERM',
npm warn cleanup       syscall: 'rmdir',
npm warn cleanup       path: 'C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec\\http-client-python\\generator\\build\\lib\\pygen\\codegen'
npm warn cleanup     }
npm warn cleanup   ],
npm warn cleanup   [
npm warn cleanup     '\\\\?\\C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec\\http-client-python',
npm warn cleanup     [Error: EPERM: operation not permitted, rmdir 'C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@typespec\http-client-python\venv\Lib\site-packages\pip\_vendor'] {
npm warn cleanup       errno: -4048,
npm warn cleanup       code: 'EPERM',
npm warn cleanup       syscall: 'rmdir',
npm warn cleanup       path: 'C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@typespec\\http-client-python\\venv\\Lib\\site-packages\\pip\\_vendor'
npm warn cleanup     }
npm warn cleanup   ],
npm warn cleanup   [
npm warn cleanup     '\\\\?\\C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@azure-tools',
npm warn cleanup     [Error: EPERM: operation not permitted, rmdir 'C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@azure-tools\typespec-python\venv'] {
npm warn cleanup       errno: -4048,
npm warn cleanup       code: 'EPERM',
npm warn cleanup       syscall: 'rmdir',
npm warn cleanup       path: 'C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@azure-tools\\typespec-python\\venv'       
npm warn cleanup     }
npm warn cleanup   ]
npm warn cleanup ]
npm error code 1
npm error path C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@azure-tools\typespec-python
npm error command failed
npm error command C:\WINDOWS\system32\cmd.exe /d /s /c tsx ./scripts/run-python3.ts ./scripts/install.py
npm error Traceback (most recent call last):
npm error   File "C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@azure-tools\typespec-python\scripts\install.py", line 46, in <module>
npm error     main()
npm error     ~~~~^^
npm error   File "C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@azure-tools\typespec-python\scripts\install.py", line 39, in main
npm error     venv_context = create_venv_with_package_manager(venv_path)
npm error   File "C:\Users\v-amberchen\source\repos\azure-sdk-for-python\sdk\cognitivelanguage\azure-ai-language-conversations-authoring\TempTypeSpecFiles\node_modules\@azure-tools\typespec-python\scripts\package_manager.py", line 140, in create_venv_with_package_manager
npm error     env_builder.create(venv_path)
npm error     ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
npm error   File "C:\Users\v-amberchen\AppData\Local\Programs\Python\Python313\Lib\venv\__init__.py", line 82, in create
npm error     self._setup_pip(context)
npm error     ~~~~~~~~~~~~~~~^^^^^^^^^
npm error   File "C:\Users\v-amberchen\AppData\Local\Programs\Python\Python313\Lib\venv\__init__.py", line 446, in _setup_pip
npm error     self._call_new_python(context, '-m', 'ensurepip', '--upgrade',
npm error     ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
npm error                           '--default-pip', stderr=subprocess.STDOUT)
npm error                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
npm error   File "C:\Users\v-amberchen\AppData\Local\Programs\Python\Python313\Lib\venv\__init__.py", line 442, in _call_new_python
npm error     subprocess.check_output(args, **kwargs)
npm error     ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
npm error   File "C:\Users\v-amberchen\AppData\Local\Programs\Python\Python313\Lib\subprocess.py", line 472, in check_output
npm error     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
npm error            ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
npm error                **kwargs).stdout
npm error                ^^^^^^^^^
npm error   File "C:\Users\v-amberchen\AppData\Local\Programs\Python\Python313\Lib\subprocess.py", line 577, in run  
npm error     raise CalledProcessError(retcode, process.args,
npm error                              output=stdout, stderr=stderr)
npm error subprocess.CalledProcessError: Command '['C:\\Users\\v-amberchen\\source\\repos\\azure-sdk-for-python\\sdk\\cognitivelanguage\\azure-ai-language-conversations-authoring\\TempTypeSpecFiles\\node_modules\\@azure-tools\\typespec-python\\venv\\Scripts\\python.exe', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
npm error Error: Command failed: py -3 ./scripts/install.py
npm error A complete log of this run can be found in: C:\Users\v-amberchen\AppData\Local\npm-cache\_logs\2025-07-21T22_34_40_381Z-debug-0.log
update
I've checked my Python installation ensurepip is satisfied, tried manually deleting the TempTypeSpecFiles folder or running the command in an Administrator terminal.... But the issue still persists. Has anyone encountered this before or could share some insights? Any help would be much appreciated. Thank you!

## answer
Maybe you could try install "uv" (here is guidance (Installation | uv)[https://docs.astral.sh/uv/getting-started/installation/]) and sync with latest main branch of python sdk repo then try again.