''' edit the templates here '''

''' html is stored in strings '''

header = '''
<div style="padding-bottom:2em"><h1>My notes</h1>
<h5><a href="./search.html">search</a> | <a href="./sitemap.html">index</a> </h5></div>
'''

footer = '''

'''

''' 
META
'''
meta = '''
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="author" content=" YOUR NAME " />
    <meta
    name="description"
    content="A personal wiki (or digital garden) of something and something else notes." />
'''

style = '''
<style>


/* $color-text: #dedce5; */
/* Sakura.css v1.4.1
 * ================
 * Minimal css theme.
 * Project: https://github.com/oxalorg/sakura/
 */
/* Body */
html {
  font-size: 62.5%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
}

body {
  font-size: 1.8rem;
  line-height: 1.618;
  max-width: 38em;
  margin: auto;
  color: #c9c9c9;
  background-color: #222222;
  padding: 13px;
}

@media (max-width: 684px) {
  body {
    font-size: 1.53rem;
  }
}
@media (max-width: 382px) {
  body {
    font-size: 1.35rem;
  }
}
h1, h2, h3, h4, h5, h6 {
  line-height: 1.1;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  font-weight: 700;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
  overflow-wrap: break-word;
  word-wrap: break-word;
  -ms-word-break: break-all;
  word-break: break-word;
}

h1 {
  font-size: 2.20em;
}

h2 {
  font-size: 1.88em;
}

h3 {
  font-size: 1.75em;
}

h4 {
  font-size: 1.5em;
}

h5 {
  font-size: 1.25em;
}

h6 {
  font-size: 1em;
}

p {
  margin-top: 0px;
  margin-bottom: 2.5rem;
}

small, sub, sup {
  font-size: 75%;
}

hr {
  border-color: #ffffff;
}

a {
  text-decoration: none;
  color: #ffffff;
}
a:visited {
  color: #e6e6e6;
}
a:hover {
  color: #c9c9c9;
  border-bottom: 2px solid #c9c9c9;
}

ul {
  padding-left: 1.4em;
  margin-top: 0px;
  margin-bottom: 2.5rem;
}

li {
  margin-bottom: 0.4em;
}

blockquote {
  margin-left: 0px;
  margin-right: 0px;
  padding-left: 1em;
  padding-top: 0.8em;
  padding-bottom: 0.8em;
  padding-right: 0.8em;
  border-left: 5px solid #ffffff;
  margin-bottom: 2.5rem;
  background-color: #4a4a4a;
}

blockquote p {
  margin-bottom: 0;
}

img, video {
  height: auto;
  max-width: 100%;
  margin-top: 0px;
  margin-bottom: 2.5rem;
}

/* Pre and Code */
pre {
  background-color: #4a4a4a;
  display: block;
  padding: 1em;
  overflow-x: auto;
  margin-top: 0px;
  margin-bottom: 2.5rem;
  font-size: 0.9em;
}

code, kbd, samp {
  font-size: 0.9em;
  padding: 0 0.5em;
  background-color: #4a4a4a;
  white-space: pre-wrap;
}

pre > code {
  padding: 0;
  background-color: transparent;
  white-space: pre;
  font-size: 1em;
}

/* Tables */
table {
  text-align: justify;
  width: 100%;
  border-collapse: collapse;
}

td, th {
  padding: 0.5em;
  border-bottom: 1px solid #4a4a4a;
}

/* Buttons, forms and input */
input, textarea {
  border: 1px solid #c9c9c9;
}
input:focus, textarea:focus {
  border: 1px solid #ffffff;
}

textarea {
  width: 100%;
}

.button, button, input[type=submit], input[type=reset], input[type=button] {
  display: inline-block;
  padding: 5px 10px;
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  background-color: #ffffff;
  color: #222222;
  border-radius: 1px;
  border: 1px solid #ffffff;
  cursor: pointer;
  box-sizing: border-box;
}
.button[disabled], button[disabled], input[type=submit][disabled], input[type=reset][disabled], input[type=button][disabled] {
  cursor: default;
  opacity: 0.5;
}
.button:focus:enabled, .button:hover:enabled, button:focus:enabled, button:hover:enabled, input[type=submit]:focus:enabled, input[type=submit]:hover:enabled, input[type=reset]:focus:enabled, input[type=reset]:hover:enabled, input[type=button]:focus:enabled, input[type=button]:hover:enabled {
  background-color: #c9c9c9;
  border-color: #c9c9c9;
  color: #222222;
  outline: 0;
}

textarea, select, input {
  color: #c9c9c9;
  padding: 6px 10px; /* The 6px vertically centers text on FF, ignored by Webkit */
  margin-bottom: 10px;
  background-color: #4a4a4a;
  border: 1px solid #4a4a4a;
  border-radius: 4px;
  box-shadow: none;
  box-sizing: border-box;
}
textarea:focus, select:focus, input:focus {
  border: 1px solid #ffffff;
  outline: 0;
}

input[type=checkbox]:focus {
  outline: 1px dotted #ffffff;
}

label, legend, fieldset {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

</style>
'''


def default(page, html):
    return f'''

    <!DOCTYPE html>
    <html lang="en">
    <head>
    
    <title>{page['title']}</title>
    {style}
    {meta}


    </head>



    <body>
    {header}
    <h2>{page['title']}</h2>
    <h6>{page['date']}</h6>

    {html}

    {footer}
    </body>
    </html>


        '''


js = '''
console.clear();

        var trace = console.log.bind(console);
        var listSelector = "#question-list-container li";

        var idx = lunr(function () {
          // define searchable fields
          this.ref("id");
          this.field("title");
          this.field("body");

          this.k1(1.3);
          this.b(0);

          // create list of all searchable entries by reading out the
          // '#question-list-container' and saving it as a list of json objects
          // in this case: {id: , title: , ref: }
          var documents = htmlElementsToJSON(listSelector, function ($element) {
            var ref = $element.attr("data-question-id"),
              title = $element.find("p a").text(),
              body = $element.find("section").text();

            return { id: ref, title: title, body: body };
          });

          // adding all entires to lunr
          documents.forEach(function (doc) {
            this.add(doc);
          }, this);
        });

        //
        function htmlElementsToJSON(listSelector, unmarschallFunction) {
          // add the list elements to lunr
          var qs = $(listSelector);
          var entries = [];
          for (var i = 0; i < qs.length; i++) {
            var $q = $(qs[i]);
            entries.push(unmarschallFunction($q));
          }
          return entries;
        }

        function search(searchTerm) {
          var results = idx.search(searchTerm);

          // reset(hide) all entries
          $(listSelector).removeClass("show");

          for (var i = 0; i < results.length; i++) {
            var result = results[i];
            $(listSelector + "[data-question-id=" + result.ref + "]").addClass(
              "show"
            );
          }
        }

        function showAll(searchTerm) {
          $(listSelector).addClass("show");
        }

        $("#searchterm").on("search paste keyup", function (event) {
          var st = $(this).val();

          // make it async, otherwise the keyboard input is interrupted
          if (st != "") {
            setTimeout(function () {
              search(st);
            }, 100);
          }
        });

        // and show all results when clicking this button
        //$(".all").click(function () {
        //  showAll();
        //});

        var queryString = window.location.search;
        queryString = queryString
          .replaceAll("?=", "")
          .replaceAll("+", " ")
          .replaceAll("_", " ")
          .replaceAll("-", " ")
          .replaceAll("%20", " ");
        $("#searchterm").val(queryString);
        console.log(queryString);
        if (queryString != "") {
          search(queryString);
        }
'''

search_style = '''
<style>
body{transition:all 1s ease-in-out}.show{display:block !important}.snippet{display:none;margin:0}#question-list-container li{display:none;margin:1em;padding:5px;width:100%}#question-list-container ul{margin:0;padding:0}.searchbox{margin:0;border-bottom:1px dodgerblue dotted;background:transparent}.searchbox input{color:grey;padding:20px 12px;font-family:monospace;font-size:30px;border:0 solid lightgray;background:transparent}.searchbox input:focus{width:100%;outline:none}.questions p{display:inline}@media (prefers-color-scheme: dark){.searchbox input{color:white}}
</style>
'''


def searchTemplate(entries):
  return f'''
  <!DOCTYPE html>
  <html>
    {meta}
    <title>Search engine</title>

    {style}  
    {search_style}
    <script src="https://unpkg.com/lunr/lunr.js"></script>
    <script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>

    <body>
      
      {header}
      <main>
        
        <div class="searchbox">
          <input
            id="searchterm"
            class=""
            type="text"
            id="sample3"
            placeholder="🔍 Search"
          />
        </div>

        <div class="questions">
          <div id="question-list-container">
            <ul> 

            {entries}

            </ul>
          </div>
        </div>
      </main>
      <script>
        {js}
      </script>
      <p>For nostaglia purposes: search function requires javascript.</p>
    </body>
  </html>


  '''


def indexpage(html):
    return f'''

  <!DOCTYPE html>
  <html lang="en">
  <head>
  
  <title>wiki index</title>
  {style}
  {meta}
  </head>

  <body>
  {header}
  

  {html}

  {footer}
  </body>
  </html>


      '''
