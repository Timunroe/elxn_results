page_template = '''\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <title>Ontario Election 2018</title>
    <link rel="stylesheet" href="https://unpkg.com/tachyons@4.8.0/css/tachyons.min.css"/>
    <style type="text/css">
        $css
    </style>
</head>
    <body style="max-width: 800px;margin: auto;">
        $core
    </body>
</html
'''

core_template = '''\
<section class="bt bb b--gray pt2 pb3 mb2" id="party-seats">
        <div class="ttu mb1">Ontario Election Results</div>
        <div class="flex flex-wrap pv1 mb1">
            {% for item in data['parties']|sort(attribute='seats', reverse=True) %}
            <div class="f2 w-25 bl bw4 b--{{item['clr']}} mb1 pl2">{{item['name']}} <span class="fw8">{{ item['seats'] }}</span></div>
            {% endfor %}
        </div>
        <div class="f6">
            Note: Ridings won or leading. Total of 124 ridings: 63 needed for a majority.<br>
            All results are unofficial until final ballot counts are verified by <a href="https://www.elections.on.ca/en.html">Elections Ontario</a>.
        </div>
    </section>

    <section class="bb b--gray pt2 pb2 mb2" id="party-leaders">
        <div class="ttu">Party Leaders</div>
        <div class="flex flex-wrap pv1">
            <div class="flex w-100 w-50-ns mb2">
                <div class="w-50">
                    <div class="f4 fw5">Doug Ford</div>
                    <div class="f6 pv1">PC - Etobicoke North</div>
                    <div class="f5">{{ data['leaders']['ford']|title }}</div>
                </div>
                <div class="w-50">
                    <div class="f4 fw5">Andrea Horwath</div>
                    <div class="f6 pv1">NDP - Hamilton Centre</div>
                    <div class="f5">{{ data['leaders']['horwath']|title }}</div>
                </div>
            </div>
            <div class="flex w-100 w-50-ns">
                <div class="w-50">
                    <div class="f4 fw5">Mike Schreiner</div>
                    <div class="f6 pv1">GRN - Guelph</div>
                    <div class="f5">{{ data['leaders']['schreiner']|title }}</div>
                </div>
                <div class="w-50">
                    <div class="f4 fw5">Kathleen Wynne</div>
                    <div class="f6 pv1">LIB - Don Valley West</div>
                    <div class="f5">{{ data['leaders']['wynne']|title }}</div>
                </div>
            </div>
        </div>
    </section>

    <section class=" bb b--gray pt2 pb2" id="local-ridings">
        <div class="pb2 ttu">Local ridings</div>
        {% for riding in data['ridings'] %}
        <button class="pica-accordion fw6">{{ riding['name']|safe }}</button>
        <div class="pica-panel">
            <table class="collapse ba br2 b--black-10 pv2 w-100">
                <tbody>
                    <tr class="striped--light-gray">
                        <th class="tl f6 fw6 ttu pv2 ph3">Party</th>
                        <th class="tl f6 fw6 ttu pv2 ph3">Candidate</th>
                        <th class="tl f6 fw6 ttu pv2 ph3">Votes</th>
                        <th class="tl f6 fw6 ttu pv2 ph3">Pct</th>
                    </tr>
                    {% set total = riding['candidates']|sum(attribute='votes') %}

                    {% for candidate in riding['candidates']|sort(attribute='votes', reverse=True) %}
                    <tr class="striped--light-gray">
                        <td class="pv2 ph3">{{ candidate['party'] }}</td>
                        <td class="pv2 ph3">{{ candidate['name'] }}</td>
                        <td class="pv2 ph3">{{ candidate['votes'] }}</td>
                        {% if candidate['votes'] != 0 %}
                        {% set pct = (candidate['votes'] / total) * 100 %}
                        <td class="pv2 ph3">{{ pct|round(1, 'common') }}</td>
                        {% else %}
                        <td class="pv2 ph3">0</td>
                        {% endif %}
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endfor %}
    </section>
'''

script_template = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;

var acc = document.getElementsByClassName("pica-accordion");
var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("pica-active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    });
}
'''
