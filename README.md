# Python Import Traps

Sample codes to introduce the basic use of `import` in Python, and to demo some common errors

[Blog (Chinese)](https://pyliaorachel.github.io/blog/tech/python/2017/09/15/pythons-import-trap.html)

###### `module_package_basics`

Sample code to demo basic Python module and package relationships.

```bash
$ python3 -m module_package_basics.sample_package.sample_module_import

>>>
Hello!
```

###### `import_errors`

Sample code to demo common errors arrising from imcorrect import concepts, including __circular import__ and __relative import above top-level package__. Also prints out messages to trace when the module or function has done loading.

```bash
$ cd import_errors
$ python3 -m sample_package.B

>>>
B started importing
A started importing
B started importing
B finished importing
B finished defining B_say_hello
B finished defining B_greet_back
A finished importing
A finished defining A_say_hello
A finished defining A_greet_back
B finished importing
B finished defining B_say_hello
B finished defining B_greet_back
B says hello!
A says hello back!
```

###### `demo`

Sample code to simulate a real-world project and when relative/absolute imports need to be attended to.

```bash
$ python3 -m demo.src.app

>>>
Hello!😋
```
```bash
$ python3 -m demo.test.test_app

>>>
Test Passes
```
