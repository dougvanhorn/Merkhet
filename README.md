Merkhet
=======

Time Management Application



## DVH Notes

Keeping my notes here so that you know what I did before you pull these changes
back into your project.  These can be cleaned up over time.


### Virtual Environment

The current best-practice for working with Django projects is to create
something called a Virtual Environment.  The idea is that you create a little
walled garden for your code.  This will allow you to install exactly the right
versions of software you need.

For example, I have an older application I support called TeacherLine.  It runs
on Django 1.1.  I also maintain LearningMedia, which runs on Django 1.5.
Instead of installing multiple Django's at the global/operating system level, I
install Django into virtual environments for each of those projects.

So for this project, we would do the following:

```bash
$ sudo apt-get install virtualenv
$ cd <project-dir>
$ virtualenv --python=python3 ve
```

This will create a virtual environment in <project-dir>/ve.  Once that's done,
you activate the virtual environment.

Before you activate it, do this:

```bash
$ which python3
```

`which` should find `python3` somwhere in the /usr/bin/ directory.  Now activate
the environment and run the same command.

```bash
$ . ve/bin/activate  # or you can do...
$ source ve/bin/activate

$ which python3
```

`which` should now find `python3` in your Virtual Environment.

What this all means is that, with your activated Virtual Environment, you now
have a separate, clean development environment for this project.  Once that's
done, let's install Django and other tools.

```bash
$ pip install git+ssh://git@github.com/django/django.git@1.7c2#egg=django-1.7c2
```

This will install Django version 1.7c2 (Release Candidate 2).  1.7 will release
in the next few weeks, so let's go ahead and use the latest so we don't have to
upgrade.

First, install some system libraries so everything will build correctly.  This
stuff isn't related to Django or your specific project.  They are libraries
that you need to build the libraries going into your Virtual Environment.

```bash
$ sudo apt-get install python3-dev python3-setuptools \
libjpeg-dev \
libopenjpeg-dev \
libfreetype6-dev \
libwebp-dev \
liblcms2-dev \
libtiff4-dev \
libtiff5-dev \
zlib1g-dev \
python3-tk tcl8.6-dev tk8.6-dev
```

Now you can install some additional applications.

```bash
$ pip install django-localflavor
$ pip install django-bootstrap3
$ pip install pytz
$ pip install Pillow
```

* `django-localflavor` used to be a part of the Django project, but it was
  separated so that it could be kept up to date outside of Django releases.

* `django-bootstrap3` will give us easier access to Twitter Bootstrap
  functionality.  See http://getbootstrap.com/ for more information about what
  it is.

* `pytz` is a set of tools to use when working with Timezones.  Which are a
  huge pain in the ass.  Probably won't need it here, but it's kind of a
  standard install.

* `Pillow` is an Image Processing library.  We probably won't use it in this
  project, but if you do anything with `ImageField` fields, you need it
  install.  A bit of history, Pillow is a fork of PIL (Python Imaging Library),
  which is no longer supported.  This is the library that needs all of the
  development libraries above.


Now that you've installed everything, do this:

```bash
$ pip freeze
```

That will output the apps currently installed in your environment.  Normally
you would put this text into a `requirements.txt` file.  I've already done
that, and added some comments for good measure.  To me, it's important to keep
the requirements file organized and well documented.  Future you will thank you
for it.


### Project (re)Organization

Now, let's dig into the project sturcture itself.  There are lots of different
ways to do it, and there is no "right" way.  I'm going to set this one up how I
like it.  You can read up on all the other ways and decide for yourself how you
like it.

#### Project Directory


#### Applications

