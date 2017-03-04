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