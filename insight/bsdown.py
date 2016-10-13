#!/usr/bin/python
"""Use pandoc to convert markdown to html, and then embed in a bootstrap
  html template."""

import argparse
import subprocess
import tempfile
from bs4 import BeautifulSoup


BOOTSTRAP_HEADER = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head 
         content must come *after* these tags -->
    <title>Going the Distance</title>

    <!-- Bootstrap -->
    <!-- link href="css/bootstrap.min.css" rel="stylesheet" -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" 
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" 
      integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
      crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" 
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" 
      integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" 
      crossorigin="anonymous">


    <style type="text/css">
      div.content {
        float: none;
        max-width: 700px;
      }

      .center {
        margin: 0 auto;
      }

      .content img {
        max-width: 49%;
        margin: 0 auto;
      }

      body {
        font-size: 15px;
      }
    </style>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="jumbotron" style="background-color: #c9daf8; padding-bottom:0;">
      <img class="center" style="display: block; max-width: 1000px;" src="runner_trace4.png" width="70%"/>
    </div>
    <div class="content center">


"""

BOOTSTRAP_FOOTER = """

    </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <!-- script src="js/bootstrap.min.js"></script -->

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" 
    integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" 
    crossorigin="anonymous"></script>
  </body>
</html>
"""

def make_page(input_path, output_path):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    subprocess.check_call(['pandoc', '--from=markdown_github',
                           '--to=html5', input_path], stdout=tmp)
    tmp.close()

    with open(tmp.name, 'r') as infile:
      soup = BeautifulSoup(infile.read(), 'lxml')

    with open(output_path, 'w') as outfile:
      outfile.write(BOOTSTRAP_HEADER)
      for x in soup.body.contents:
        outfile.write(str(x))
      outfile.write(BOOTSTRAP_FOOTER)


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('input_path', help='Path to the markdown input file')
  parser.add_argument('output_path', help='Path to the output html file')
  args = parser.parse_args()
  make_page(args.input_path, args.output_path)

if __name__ == '__main__':
  main()
