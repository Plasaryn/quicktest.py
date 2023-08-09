# Write your code here!

# E.G.
def get_python_version():
    import sys
    print(f"Python Version: {sys.version}")

def run_test(function: 'function', run: 'bool', *args, **kwargs):
    if run:
        function(*args, **kwargs)

"""STYLE GUIDE
Name:             quicktest.py
Author:           github.com/Plasaryn
Style Guide Date: 8/9/23
Current Version:  <Current Python Version used for quicktest>

> PURPOSE
The purpose of this document is to provide a sandbox to come 
and test out python's features as one would desire! Forgot
what print() does? Then come in here and prove for yourself
what it does (By providing a string as an argument). 

It is not meant to host long term projects, or applications
that are meant to function in any serious capacity. Instead,
quicktest.py provides a place where foundational aspects of 
python can be evaluated, where newly learned features can be 
tested, and because it is the place where fringe ideas are
codified in the testers brain, it needs to retain the tests
that were performed with it in the past. As such, this 
style guide is meant to provide instructions for how a user
can perform these actions without cluttering up the workspace.

> GLOBAL DEFINITIONS
Inside this document, the only thing that should be defined
in the global scope are functions and classes. The purpose 
behind this is to;
    1: Keep the global namespace as clean as possible
    2: Allow for the easy copying or importing of 
       functions and modules to other projects.

As such, quicktest.py (and hopefully more scripts) follow
the boilerplate setup of 

def main():
    do_stuff()

if __name__ == "__main__": 
    main()

The  __name__ == "__main__" condition test will only execute
code if the script is run directly, which means that functions
WONT run if the script is imported. This helps ensure 
that no unwanted computations are executed if you were
to eventually decide to import this document into another
module.

Organizing the document this way also ensures that we can
control exactly what is being run by limiting what code
is being written in the main() function.

> The Purpose of main()
main() should only be used to call children functions.
That's it. No defining variables, no calculations,
nothing except being the conductor which tells which
function to execute, and in whichever order to do so. 
To keep things even more organized, I recommend calling
children functions through the run_test function.

> The Purpose of run_test(function, run, *args, **kwargs)
At 2 lines, it's easy to undersell the importance of run_test
as a function. However, it is an additional way by which 
main can control which functions get run. Some users may
prefer to comment out function calls from main in order
to keep main from calling functions, but having run_test
allows for a function to be passed without cluttering main
with comments. Further alternatives to run_test may also
include deleting lines, but that also history from quicktest.py
It is an option for you to use, but you can decide whether 
you want to use it. 

> Defining Functions
Functions are where the simple tests actually happen. 
Because this document is meant to be used with a majority
of it never being called, this style guide recommends 
importing dependent modules at the top of each test 
function rather than at the top of the document. This 
follows other python style guides in spirit by only
importing dependent packages when necessary, such as
other tactics like
from x import y,z

Inside of these callable functions, it is up to the 
discretion of the user to adhere to their own stylistic
preferences, and should design their logic in whatever
manner is cohesive with their other projects, or 
whatever is convenient in the course of time. (Although
if time is an issue to the point of neglecting style,
then the user is welcome to avoid this document in
the first place!)

> Defining Classes
Class definitions may happen in either global scope
or function scopes. I would recommend, however, if
you are defining a class that has dependencies on 
imported modules such that these modules will need
to be imported in the global scope, I will provide this
line of thinking. If you do wish to copy these class
definitions to other projects, then you may wish to 
write them inside their own file and promote your
efforts beyond quick testing. If you do not wish
to copy these class definitions to other projects, 
then what's the harm with nesting these classes 
within functions? By following those two lines
of thinking, we can save the unnecessary computation
of importing modules unnecessarily in future runs
of quicktest.py. 

> Additional recommendations
The goal of any style guide is to allow projects to
look pleasing to the eye. It's almost counter intuitive
to define a style guide for a script that is designed to
retain old code that isn't being used. Despite this, that
code may still be useful! Which is why this style guide
is meant to work with modern IDEs and text editors like
VSCode, Notepad++, Sublime, and I'm sure many others. 
Function and class definitions in these programs can
be cascaded. Even this style guide can be cascaded! 
Do that so you can easily scroll through the document to
find the code that is meaningful to you. 
"""

def main():
    run_test(get_python_version, True)

if __name__ == "__main__": 
    main()
