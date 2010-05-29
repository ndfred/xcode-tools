xcode-tools
===========

Various xcode build, localization and iPhone-related scripts.
All of these scripts can easily be imported to fit in a bigger project.
Please take a look at the source code for further information.
These scripts are compatible with python 2.5 and 2.6, but mainly tested with
python 2.6.
Mac OS X is obviously the platform of choice for these tools, although the
code should be portable.


xcode_project.py
----------------
This script parses an [XCode][] project and gives access to all of its targets
and build settings.
If you run it, it will display the contents of the project file:

    $ python xcode_project.py App.xcodeproj

[XCode]: http://developer.apple.com/technologies/tools/xcode.html

The `xcode_project.py` script needs the [`plutil`][plutil] command-line tool to run.

[plutil]: http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/plutil.1.html


mobile_provision.py
-------------------
This script parses a [mobile provision][] and gives access to its name,
devices UDIDs, application identifier and so forth.
If you run it, it will display the contents of the mobile provision file:

    $ python mobile_provision.py app.mobileprovision

[mobile provision]: http://developer.apple.com/iphone/library/documentation/Xcode/Conceptual/iphone_development/128-Managing_Devices/devices.html

update_strings.py
-----------------
This script updates a given [strings file][] with the new strings found in
your project's source code.
You can also import an already-translated strings file that will update your
current strings file.
To run it:

    $ python update_strings.py Localizable.strings

The `update_strings.py` script needs the [`genstrings`][genstrings]
command-line tool to run.

[genstrings]: http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/genstrings.1.html
[strings file]: http://developer.apple.com/iphone/library/documentation/MacOSX/Conceptual/BPInternational/Articles/StringsFiles.html
