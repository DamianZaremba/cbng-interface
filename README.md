ClueBot NG Interface
====================

Development
-----------

```bash
virtualenv ve
. ve/bin/activate
pip install -r requirements.txt
```

Deployment
----------

All deployment is done from master via fabric.

To deploy, run `fab deploy` in the current directory with fabric installed locally.

To install fabric `pip install fabric`


Databases
---------

There are a number of databases used within the UI.
They are detailed below.

# Default
Used for any Django tables not in the review schema.

# Bot
Core schema, written to by ClueBot NG.
Not managed/migrated by Django.

# Review
Review schema, managed/migrated by Django.