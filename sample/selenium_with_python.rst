====================
Selenium with Python
====================

:Author: `Baiju Muthukadan <http://baijum81.livejournal.com/>`_
:Email: baiju.m.mail AT gmail.com
:Version: 0.3.2

.. note::

  `This document has been submitted to Selenium
  <http://code.google.com/p/selenium/issues/detail?id=1930>`_ project
  to be included in the official documentation.  The `format of this
  text is reStucturedText
  <https://raw.github.com/gist/1047207/selenium_with_python.rst>`_.  I
  am looking forward to your feedback.  Please send your feedback to:
  `baiju.m.mail AT gmail.com` or you can `comment at the bottom of
  this gist <https://gist.github.com/1047207#comments>`_.


Introduction
------------

Selenium Python bindings provide a convenient API to access Selenium
WebDrivers like Firefox, Ie and Chrome.  The current supported Python
versions are Python 2.6 and Python 2.7.  Python 3 is not yet
supported.  Selenium server is a Java program.  Java Runtime
Environment (JRE) 1.6 is recommended to run Selenium server.  This
article explain using Selenium 2 with WebDriver API.  Selenium 1 API
is not covered here.

Installation
------------


Downloading Selenium server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download Selenium server 2.x from the `download page of
selenium website <http://seleniumhq.org/download/>`_.  The file name
should be something like this:
``selenium-server-standalone-2.x.x.jar``.  You can always download the
latest 2.x version of Selenium server.

If Java Runtime Environment (JRE) is not installed in your system, you
can download the `JRE from the Oracle website
<http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_.
If you have root access in your system, you can also use your
operating system instructions to install JRE.


Downloading Python bindings for Selenium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download Python bindings for Selenium from the `PyPI page for
selenium package <http://pypi.python.org/pypi/selenium>`_.  It has a
dependency on `rdflib <http://pypi.python.org/pypi/rdflib>`_ , version
3.1.x.

You can also use `easy_install
<http://python-distribute.org/distribute_setup.py>`_ or `pip
<http://pypi.python.org/pypi/pip>`_ to install the bindings::

  easy_install selenium

or::

  pip install selenium

You may consider using `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_ to create isolated Python
environments.


Using Buildout for installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to use `Buildout <http://wwww.buildout.org>`_ to install
all the dependencies from a GNU/Linux machine, you can use this
configuration::

  [buildout]
  file-server = http://fileserver.example.org
  parts =
      jre_download
      jre_install
      selenium_server_download
      selenium_py

  [jre_download]
  recipe = hexagonit.recipe.download
  url = ${buildout:file-server}/jre-6u26-linux-i586.bin
  download-only = true
  ignore-existing = true

  [jre_install]
  recipe = iw.recipe.cmd
  on_install = true
  on_update = true
  shell = bash
  cmds =
      chmod +x ${jre_download:location}/jre-6u26-linux-i586.bin
      cd ${buildout:directory};if [[ -e "jre1.6.0_26" ]]; then echo -n; else ${jre_download:location}/jre-6u26-linux-i586.bin; fi

  [selenium_server_download]
  recipe = hexagonit.recipe.download
  url = ${buildout:file-server}/selenium-server-standalone-2.1.0.jar
  download-only = true
  ignore-existing = true

  [selenium_py]
  recipe = z3c.recipe.scripts
  interpreter = python
  eggs = selenium

Windows Buildout users can use these parts for automating installation
of Selenium server and creating a script to run it::

  [buildout]
  file-server = http://fileserver.example.org
  parts =
      jre_download
      jre_install
      selenium_server_download
      selenium_py

   [jre_download]
   recipe = hexagonit.recipe.download
   url = ${pkgserver:fullurl}/zepackages/jre-6u26-windows-i586.zip
   destination = ${buildout:directory}
   ignore-existing = true

  [selenium_server_download]
  recipe = hexagonit.recipe.download
  url = ${pkgserver:fullurl}/zepackages/selenium-server-standalone-2.1.0.jar
  download-only = true
  ignore-existing = true

  [selenium_server_script]
  recipe = collective.recipe.template
  input = inline:
      set PATH=%PATH%;${firefox_download:destination}\firefox36
      ${jre_download:destination}\jre6\bin\java.exe -jar ${selenium_server_download:location}\selenium-server-standalone-2.1.0.jar -timeout 180 -port 4444 -forcedBrowserModeRestOfLine firefoxchrome
  output = ${buildout:bin-directory}/selenium-server.bat

  [selenium_py]
  recipe = z3c.recipe.scripts
  interpreter = python
  eggs = selenium

The `jre-6u26-windows-i586.zip` is not available from Oracle site.
So, you can install JRE once and zip it and then upload to your
file server.


Running Selenium server
-----------------------

You should have Java Runtime Environment (JRE) in the system.  If
`java` command is available in the PATH (environment variable), you
can start the Selenium server using the command command given below.
Replace `2.x.x` with actual version of Selenium server you downloaded
from the site.  If JRE is installed as a non-root user and/or if it is
not available in the PATH (environment variable), you can type the
relative/absolute path to the `java` command, for eg:-
``./jre1.6.0_26/bin/java``::

  java -jar selenium-server-standalone-2.x.x.jar

In GNU/Linux, you can use the script given below to run it as a
daemon.  You will be required to change the location of `java` command
(``JAVA`` variable) and Selenium server jar file (``SELENIUM``
variable).

::

  #! /bin/bash

  ### BEGIN INIT INFO
  # Provides:          selenium-server
  # Required-Start:    $local_fs $remote_fs $network $named $time
  # Required-Stop:     $local_fs $remote_fs $network $named $time
  # Should-Start:      $syslog
  # Should-Stop:       $syslog
  # Default-Start:     2 3 4 5
  # Default-Stop:      0 1 6
  # Short-Description: Starts selenium server for testing
  # Description:       Selenium server for functional testing
  ### END INIT INFO

  . /lib/lsb/init-functions

  JAVA=java
  SELENIUM=/path/to/selenium-server-standalone-2.x.xjar
  BMODE=firefoxchrome
  PORT=4444
  LOG=selenium.log
  PIDFILE=selenium.pid
  DISPLAY=:0.0

  pidof_server() {
      if [ -e "$PIDFILE" ]; then
          if pidofproc java | tr ' ' '\n' | grep -w $(cat $PIDFILE); then
              return 0
          fi
      fi
      return 1
  }


  case $1 in
      start)
          DISPLAY=$DISPLAY $JAVA -jar $SELENIUM \
              -timeout 180 -port $PORT -forcedBrowserModeRestOfLine $BMODE > $LOG &
          log_success_msg "Starting Selenium server!" "selenium-server"
          echo $! > $PIDFILE
      ;;
      stop)
          SELPID=`cat $PIDFILE` && kill $SELPID
          log_success_msg "Stopping Selenium server!" "selenium-server"
      ;;
      status)
          PID=$(pidof_server) || true
          if [ -n "$PID" ]; then
              echo "Selenium Server is running (pid $PID)."
              exit 0
          else
              echo "Selenium Server is NOT running."
              exit 1
          fi
      ;;
      *)
          echo "Usage: selenium-server.sh {start|stop|status}"
          exit 1
      ;;
  esac

Buildout users can use `collective.recipe.template` recipe with above
text as the template.  You will be required to change the location of
`java` command (``JAVA`` variable) and Selenium server jar file
(``SELENIUM`` variable).  If you are using Buildout configuration
given in the previous section, you can change the variables like
this::

  JAVA=${buildout:directory}/jre1.6.0_26/bin/java
  SELENIUM=${selenium_server_download:location}/selenium-server-standalone-2.1.0.jar


Using Selenium
--------------

If you have installed Selenium server and Python bindings and able to
run the server, you can start using it from Python like this.

::

  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys

  driver = webdriver.Firefox()
  driver.get("http://www.python.org")
  assert "Python" in driver.title
  elem = driver.find_element_by_name("q")
  elem.send_keys("selenium")
  elem.send_keys(Keys.RETURN)
  assert "Google" in driver.title
  driver.close()

The above script can be saved into a file (eg:-
`python_org_search.py`), then it can be run like this::

  python python_org_search.py

The `python` which you are running should have the `selenium` module
installed.

Walk through of the example
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `selenium.webdriver` module provides all the WebDriver
implementations.  Currently supported WebDriver implementations are
Firefox, Chrome, Ie and Remote.  The `Keys` class provide keys in the
keyboard like RETURN, F1, ALT etc.

::

  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys

Next, the instance of Firefox WebDriver is created.

::

  driver = webdriver.Firefox()

The `driver.get` method will navigate to a page given by the URL.
WebDriver will wait until the page has fully loaded (that is, the
"onload" event has fired) before returning control to your test or
script.  It's worth noting that if your page uses a lot of AJAX on
load then WebDriver may not know when it has completely loaded.::

  driver.get("http://www.python.org")

The next line is an assertion to confirm that title has "Python" word
in it::

  assert "Python" in driver.title

WebDriver offers a number of ways to find elements.  One of the
approach is to use the `find_element_by_*` methods.  Commonly used
methods are `find_element_by_id`, `find_element_by_name`,
`find_element_by_xpath`, `find_element_by_link_text`,
`find_element_by_partial_link_text`, `find_element_by_tag_name`,
`find_element_by_class_name`, `find_element_by_css_selector`::

  elem = driver.find_element_by_name("q")

Next we are sending keys, this is similar to entering keys using your
keyboard.  Special keys can be send using `Keys` class imported from
`selenium.webdriver.common.keys`::

  elem.send_keys("selenium")
  elem.send_keys(Keys.RETURN)

After submission of the page, you should be reached in the Google
site::

  assert "Google" in driver.title

Finally, the browser window is closed.  You can also call `quit`
method instead of `close`.  The `quit` will exit entire browser where
as `close` will close one tab, but if it just one tab, by default most
browser will exit entirely.::

  driver.close()


Using Selenium to write tests
-----------------------------

Selenium will be used mostly for writing test cases.  You can write
test cases using Python’s unittest module.  Here is the modified
example which uses unittest module.  This is a test for python.org
search functionality::

  import unittest
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys

  class PythonOrgSearch(unittest.TestCase):

      def setUp(self):
          self.driver = webdriver.Firefox()

      def test_search_in_python_org(self):
          driver = self.driver
          driver.get("http://www.python.org")
          self.assertIn("Python", driver.title)
          elem = driver.find_element_by_name("q")
          elem.send_keys("selenium")
          elem.send_keys(Keys.RETURN)
          self.assertIn("Google", driver.title)

      def tearDown(self):
          self.driver.close()

  if __name__ == "__main__":
      unittest.main()


You can run the above test case from a shell like this::

  python test_python_org_search.py
  .
  ----------------------------------------------------------------------
  Ran 1 test in 15.566s

  OK


Walk through of the example
---------------------------

Initially, all the basic modules required are imported.  The `unittest
<http://docs.python.org/library/unittest.html>`_ module is a built-in
Python based on Java's JUnit.  This module provides the framework for
organizing the test cases.  The `selenium.webdriver` module provides
all the WebDriver implementations.  Currently supported WebDriver
implementations are Firefox, Chrome, Ie and Remote.  The `Keys` class
provide keys in the keyboard like RETURN, F1, ALT etc.

::

  import unittest
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys

The test case class is inherited from `unittest.TestCase`.
Inheriting from `TestCase` class is the way to tell `unittest` module
that, this is a test case::

  class PythonOrgSearch(unittest.TestCase):


The `setUp` is part of initialization, this method will get called
before every test function which you are going to write in this test
case class.  Here you are creating the instance of Firefox WebDriver.

::

      def setUp(self):
          self.driver = webdriver.Firefox()

This is the test case method.  The first line inside this method
create a local reference to the driver object created in `setUp`
method.

::

      def test_search_in_python_org(self):
          driver = self.driver

The `driver.get` method will navigate to a page given by the URL.
WebDriver will wait until the page has fully loaded (that is, the
"onload" event has fired) before returning control to your test or
script.  It's worth noting that if your page uses a lot of AJAX on
load then WebDriver may not know when it has completely loaded.::

          driver.get("http://www.python.org")

The next line is an assertion to confirm that title has "Python" word
in it::

          self.assertIn("Python", driver.title)

WebDriver offers a number of ways to find elements.  One of the
approach is to use the `find_element_by_*` methods. Commonly used
methods are `find_element_by_id`, `find_element_by_name`,
`find_element_by_xpath`, `find_element_by_link_text`,
`find_element_by_partial_link_text`, `find_element_by_tag_name`,
`find_element_by_class_name`, `find_element_by_css_selector`::

          elem = driver.find_element_by_name("q")

Next we are sending keys, this is similar to entering keys using your
keyboard.  Special keys can be send using `Keys` class imported from
`selenium.webdriver.common.keys`::

          elem.send_keys("selenium")
          elem.send_keys(Keys.RETURN)

After submission of the page, you should be reached in the Google
site.  You can confirm it by asserting "Google" in the title::

          self.assertIn("Google", driver.title)

The `tearDown` method will get called after every test method.  This
is a place to do all cleanup actions.  In the current method, the
browser window is closed.  You can also call `quit` method instead of
`close`.  The `quit` will exit all entire browser where as `close`
will close one tab, but if it just one tab, by default most browser
will exit entirely.::

      def tearDown(self):
          self.driver.close()

Final lines are some boiler plate code to run the test suite::

  if __name__ == "__main__":
      unittest.main()


Navigating
----------

.. warning::

    This section is a copy-paste from Java docs, so it requires some
    modification.

The first thing you'll want to do with WebDriver is navigate to a
page.  The normal way to do this is by calling "get":

::

  driver.get("http://www.google.com");

WebDriver will wait until the page has fully loaded (that is, the
"onload" event has fired) before returning control to your test or
script.  It's worth noting that if your page uses a lot of AJAX on
load then WebDriver may not know when it has completely loaded.  If
you need to ensure such pages are fully loaded then you can use
"waits".

.. TODO: link to a section on explicit waits in WebDriver


Interacting with the page
~~~~~~~~~~~~~~~~~~~~~~~~~

Just being able to go to places isn't terribly useful.  What we'd
really like to do is to interact with the pages, or, more
specifically, the HTML elements within a page.  First of all, we need
to find one.  WebDriver offers a number of ways to find elements.  For
example, given an element defined as::

  <input type="text" name="passwd" id="passwd-id" />

you could find it using any of::

  element = driver.find_element_by_id("passwd-id")
  element = driver.find_element_by_name("passwd")
  element = driver.find_element_by_xpath("//input[@id='passwd-id']")

You can also look for a link by its text, but be careful! The text
must be an exact match! You should also be careful when using `XPATH
in WebDriver`.  If there's more than one element that matches the
query, then only the first will be returned.  If nothing can be found,
a ``NoSuchElementException`` will be raised.

.. TODO: Is this following paragraph correct ?

WebDriver has an "Object-based" API; we represent all types of
elements using the same interface.  This means that although you may
see a lot of possible methods you could invoke when you hit your IDE's
auto-complete key combination, not all of them will make sense or be
valid.  Don't worry! WebDriver will attempt to do the Right Thing, and
if you call a method that makes no sense ("setSelected()" on a "meta"
tag, for example) an exception will be raised.

So, you've got an element.  What can you do with it? First of all, you
may want to enter some text into a text field::

  element.send_keys("some text");

You can simulate pressing the arrow keys by using the "Keys" class::

  element.send_keys(" and some", Keys.ARROW_DOWN);

It is possible to call `send_keys` on any element, which makes it
possible to test keyboard shortcuts such as those used on GMail.  A
side-effect of this is that typing something into a text field won't
automatically clear it.  Instead, what you type will be appended to
what's already there.  You can easily clear the contents of a text
field or textarea with `clear` method::

  element.clear();


Filling in forms
~~~~~~~~~~~~~~~~

We've already seen how to enter text into a textarea or text field,
but what about the other elements? You can "toggle" the state of
checkboxes, and you can use "setSelected" to set something like an
`OPTION` tag selected.  Dealing with `SELECT` tags isn't too bad::

    select = driver.find_element_by_xpath("//select"))
    all_options = select.find_elements_by_tag_name("option"))
    for option in all_options:
        print "Value is: %s" % option.getValue() #<- FIXME: API
        option.setSelected() #<- FIXME: API

This will find the first "SELECT" element on the page, and cycle
through each of it's OPTIONs in turn, printing out their values, and
selecting each in turn.  As you can see, this isn't the most efficient
way of dealing with SELECT elements . WebDriver's support classes
include one called "Select", which provides useful methods for
interacting with these.

::

    select = driver.find_element_by_xpath("//select").select()  #<- FIXME: API
    select.deselectAll() #<- FIXME: API
    select.selectByVisibleText("Edam") #<- FIXME: API

This will deselect all OPTIONs from the first SELECT on the page, and
then select the OPTION with the displayed text of "Edam".

Once you've finished filling out the form, you probably want to submit
it. One way to do this would be to find the "submit" button and click
it::

  # Assume the button has the ID "submit" :)
  driver.find_element_by_id("submit").click()

Alternatively, WebDriver has the convenience method "submit" on every
element.  If you call this on an element within a form, WebDriver will
walk up the DOM until it finds the enclosing form and then calls
submit on that.  If the element isn't in a form, then the
``NoSuchElementException`` will be raised::

  element.submit();


Drag and drop
~~~~~~~~~~~~~

You can use drag and drop, either moving an element by a certain
amount, or on to another element::

  element = driver.find_element_by_name("source")
  target = driver.find_element_by_name("target")

  from selenium.webdriver import ActionChains
  action_chains = ActionChains(driver)
  action_chains.drag_and_drop(element, target);


Moving between windows and frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's rare for a modern web application not to have any frames or to be
constrained to a single window.  WebDriver supports moving between
named windows using the "switch_to_window" method::

  driver.switch_to_window("windowName")

All calls to ``driver`` will now be interpreted as being directed to
the particular window.  But how do you know the window's name? Take a
look at the javascript or link that opened it::

  <a href="somewhere.html" target="windowName">Click here to open a new window</a>

Alternatively, you can pass a "window handle" to the
"switch_to_window()" method.  Knowing this, it's possible to iterate
over every open window like so::

  for handle in driver.window_handles:
      driver.switch_to_window(handle);

You can also swing from frame to frame (or into iframes)::

  driver.switch_to_frame("frameName")

It's possible to access subframes by separating the path with a dot,
and you can specify the frame by its index too.  That is::

  driver.switch_to_frame("frameName.0.child")

would go to the frame named "child" of the first subframe of the frame
called "frameName".  **All frames are evaluated as if from *top*.**


Popup dialogs
~~~~~~~~~~~~~

Selenium WebDriver has built-in support for handling popup dialog
boxes.  After you've triggerd and action that would open a popup, you
can access the alert with the following::

  alert = driver.switch_to_alert()

This will return the currently open alert object.  With this object
you can now accept, dismiss, read its contents or even type into a
prompt.  This interface works equally well on alerts, confirms,
prompts.  Refer to the API documentation for more information.


Navigation: history and location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Earlier, we covered navigating to a page using the "get" command (
``driver.get("http://www.example.com")``) As you've seen, WebDriver
has a number of smaller, task-focused interfaces, and navigation is a
useful task.  To navigate to a page, you can use `get` method::

  driver.get("http://www.example.com");

To move backwards and forwards in your browser's history::

  driver.forward()
  driver.back()

Please be aware that this functionality depends entirely on the
underlying driver.  It's just possible that something unexpected may
happen when you call these methods if you're used to the behaviour of
one browser over another.


Cookies
~~~~~~~

Before we leave these next steps, you may be interested in
understanding how to use cookies.  First of all, you need to be on the
domain that the cookie will be valid for:

::

  # Go to the correct domain
  driver.get("http://www.example.com")

  # Now set the cookie. This one's valid for the entire domain
  cookie = {"key": "value"})
  driver.add_cookie(cookie)

  # And now output all the available cookies for the current URL
  all_cookies = driver.get_cookies()
  for cookie_name, cookie_value in all_cookies.items():
      print "%s -> %s", cookie_name, cookie_value


Next, next steps!
~~~~~~~~~~~~~~~~~

This has been a high level walkthrough of WebDriver and some of its
key capabilities.  You may want to look at the `Test Design
Considerations` chapter to get some ideas about how you can reduce the
pain of maintaining your tests and how to make your code more modular.


Test Design Considerations
--------------------------


API
---

This chapter cover all the interfaces of Selenium WebDriver.

Exceptions
~~~~~~~~~~

**module:** selenium.common.exceptions


- class WebDriverException(msg=None, screen=None, stacktrace=None)

  base: Exception


- class ErrorInResponseException(response, msg)

  base: WebDriverException

  An error has occurred on the server side.

  This may happen when communicating with the firefox extension or the
  remote driver server.


- class InvalidSwitchToTargetException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  The frame or window target to be switched doesn't exist.


- class NoSuchFrameException(msg=None, screen=None, stacktrace=None)

  base: InvalidSwitchToTargetException

  The frame target to be switched doesn't exist.

- class NoSuchWindowException(msg=None, screen=None, stacktrace=None)

  base: InvalidSwitchToTargetException

  The window target to be switched doesn't exist.

- class NoSuchElementException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  The find_element_by_* methods can't find the element.


- class NoSuchAttributeException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class StaleElementReferenceException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Indicates that a reference to an element is now "stale" --- the
  element no longer appears on the DOM of the page.

- class InvalidElementStateException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class ElementNotVisibleException(msg=None, screen=None, stacktrace=None)

  base: InvalidElementStateException

  Thrown to indicate that although an element is present on the DOM,
  it is not visible, and so is not able to be interacted with.

- class ElementNotSelectableException(msg=None, screen=None, stacktrace=None)

  base: InvalidElementStateException

- class InvalidCookieDomainException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Thrown when attempting to add a cookie under a different domain
  than the current URL.

- class UnableToSetCookieException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

  Thrown when a driver fails to set a cookie.

- class RemoteDriverServerException(msg=None, screen=None, stacktrace=None)

  base: WebDriverException

- class TimeoutException(msg=None, screen=None, stacktrace=None)

  Thrown when a command does not complete in enough time.

Action Chains
~~~~~~~~~~~~~

**module:** selenium.webdriver.common.action_chains

- class ActionChains(driver)

  *driver:* The WebDriver instance which performs user actions.

  Generate user actions.  All actions are stored in the ActionChains
  object.  Call perform() to fire stored actions.

  - perform()

    Performs all stored actions.

  - click(on_element=None)

    Clicks an element.

    *on_element:* The element to click.  If None, clicks on current
    mouse position.

  - click_and_hold(on_element)

    Holds down the left mouse button on an element.

    *on_element:* The element to mouse down.  If None, clicks on
    current mouse position.

  - context_click(on_element)

    Performs a context-click (right click) on an element.

    *on_element:* The element to context-click.  If None, clicks on
    current mouse position.

  - double_click(on_element)

    Double-clicks an element.

    *on_element:* The element to double-click.  If None, clicks on
    current mouse position.

  - drag_and_drop(source, target)

    Holds down the left mouse button on the source element, then moves
    to the target element and releases the mouse button.

    *source:* The element to mouse down.

    *target:* The element to mouse up.

  - key_down(key, element=None)

    Sends a key press only, without releasing it.  Should only be used
    with modifier keys (Control, Alt and Shift).

    *key:* The modifier key to send. Values are defined in Keys class.

    *element:* The element to send keys.  If None, sends a key to
    current focused element.


  - key_up(key, element=None)

    Releases a modifier key.

    *key:* The modifier key to send. Values are defined in Keys class.

    *element:* The element to send keys.  If None, sends a key to
    current focused element.

  - move_by_offset(xoffset, yoffset)

    Moving the mouse to an offset from current mouse position.

    *xoffset:* X offset to move to.
    *yoffset:* Y offset to move to.

  - move_to_element(to_element)

    Moving the mouse to the middle of an element.

    *to_element:* The element to move to.

  - move_to_element_with_offset(to_element, xoffset, yoffset)

    Move the mouse by an offset of the specificed element.
    Offsets are relative to the top-left corner of the element.

    *to_element:* The element to move to.
    *xoffset:* X offset to move to.
    *yoffset:* Y offset to move to.

  - release(on_element)

    Releasing a held mouse button.

    *on_element:* The element to mouse up.

  - end_keys(`*keys_to_send`)

    Sends keys to current focused element.

    *keys_to_send:* The keys to send.

  - end_keys_to_element(self, element, `*keys_to_send`):

    Sends keys to an element.

    *element:* The element to send keys.
    *keys_to_send:* The keys to send.


Resources
---------

- Blog post explaining how to use headless X for running Selenium
  tests:
  http://coreygoldberg.blogspot.com/2011/06/python-headless-selenium-webdriver.html

- Jenkins plugin for headless Selenium tests:
  https://wiki.jenkins-ci.org/display/JENKINS/Xvnc+Plugin


Frequently asked questions
--------------------------


How to use ChromeDriver ?
~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest `chromdriver from download page
<http://code.google.com/p/chromium/downloads/list>`_.  Unzip the
file::

  unzip chromedriver_linux32_x.x.x.x.zip

You should see a ``chromedriver`` executable.  Now you can instance of
Chrome WebDriver like this::

  driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

The rest of the example should work as given in other other
documentation.


Conclusion
----------

Selenium Python bindings provides a simple API to automate all kinds
of functional/acceptance tests using Selenium WebDriver.  Though Python
API you can access all functionalities in an intuitive way.

