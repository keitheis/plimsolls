plimsolls
=========

Presentation helpers based on Plim


Usage
-----

Used in Plim::

    -namespace module="plimsolls.formatters.code2html" name="code2html"

    h2 Pygments Example: Result
    pre
      -py
        code = """
        #Python 2.x:
        python -m SimpleHTTPServer

        #Python 3.x:
        python -m http.server 8000
        """

      == code2html.reformat('bash', code)
