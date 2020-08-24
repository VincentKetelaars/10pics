======
10pics
======
This project is based on a team introduction activity: Use 10 pictures to describe yourself!

With this project you will be able to choose 10 pictures from your Google Photos Library and display them in a Jupyter notebook.

Setup
========
Google Credentials
------------------
In order to be able to access your photos via Google's API you'll need to download a secrets file. The steps below outline how this is done.

- Create a client id using these borrowed instructions_. When it comes to choosing the application type, please choose Desktop.
- Once the client ID is created, download it as ``secrets_file.json``

.. _instructions: https://docs.google.com/document/d/1ck1679H8ifmZ_4eVbDeD_-jezIcZ-j6MlaNaeQiz7y0

Poetry
------
This project uses poetry. Install ``poetry`` by running the command ``python <(curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py)``.
Once installed, run ``poetry install``, which will create the virtual env with the required packages.

Run example
-----------
Run ``poetry run jupyter notebook`` to start a local Jupyter notebook, then provide the two path files as indicated.
- ``secrets_file.json`` as explained above
- ``credentials.pickle`` will store your session credentials for you, for easy reauthentication

When instantiating the client, you will be directed to your browser to authorize your application. Make sure to follow through, even where it says *This app isn't verified*.

Contribute
==========

Feel free to create a PR if you'd like to contribute.

Please make sure to run `make lint-check` before you do!


