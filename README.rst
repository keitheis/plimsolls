plimsolls
=========

Presentation helpers based on Plim


Usage
-----

File: example.plim::

    -namespace module="plimsolls.formatters.code2html" name="code2html"

    h2 Pygments Example:
    pre
      -py
        code = """
        #Python 2.x:
        python -m SimpleHTTPServer

        #Python 3.x:
        python -m http.server 8000
        """

      == code2html.reformat('bash', code)
