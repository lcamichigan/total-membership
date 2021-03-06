# Total Membership

[![Build status](https://ci.appveyor.com/api/projects/status/odap1i2nrwrp4xxj?svg=true)](https://ci.appveyor.com/project/lcamichigan/total-membership)
[![Build Status](https://travis-ci.org/lcamichigan/total-membership.svg?branch=master)](https://travis-ci.org/lcamichigan/total-membership)

To run [make_total_membership_csv.py](make_total_membership_csv.py), enter in
PowerShell or Command Prompt on Windows:

```sh
python make_total_membership_csv.py
```

or in Terminal on macOS:

```sh
./make_total_membership_csv.py
```

Note that the script requires Python 3.

To install Python 3 on Windows, visit https://www.python.org/downloads/windows/,
and then download and run an installer for the latest release of Python 3. Make
sure you add python.exe to your Windows PATH when you install Python 3.

The easiest way to install Python 3 on macOS is probably through
[Homebrew](https://brew.sh). To install Homebrew, follow the instructions at
https://brew.sh. After you install Homebrew, enter `brew install python` in
Terminal.

The script creates a CSV file named total-membership.csv containing total
membership by date. You can analyze the CSV file using a variety of tools. For
example, you can visualize it as a
[chart](https://support.google.com/docs/answer/63728) in a Google spreadsheet:

<img width="587" alt="total-membership" src="https://user-images.githubusercontent.com/14102861/51693937-d55e6200-1fcd-11e9-91c9-721b07834a0b.png">
