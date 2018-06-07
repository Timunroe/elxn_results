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
<section style="border-top-style: solid; border-top-width: 1px; border-bottom-style: solid; border-bottom-width: 1px; border-color: lightgrey; padding-top: 8px; padding-bottom: 12px; margin-bottom: 8px; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif;" class="" id="party-seats">
        <div style="margin-bottom: 4px; text-transform: uppercase; font-size: 12px;" class="">Ontario Election Results</div>
        <div style="display: flex; flex-wrap: wrap; padding-top: 4px; padding-bottom: 4px; margin-bottom: 4px;" class="">
            {% for item in data['parties']|sort(attribute='seats', reverse=True) %}
            <div style="width: 25%; border-left-style: solid; border-left-width: 12px; border-color: {{ item['clr'] }}; margin-bottom: 4px; padding-left: 6px; font-size: 26px;" class=""><span style="font-weight: 200;">{{item['name']}}</span> <span style="font-weight: 800;" class="">{{ item['seats'] }}</span></div>
            {% endfor %}
        </div>
        <div style="font-size: 10px;" class="">
            Note: Ridings won or leading. Total of 124 ridings: 63 needed for a majority.<br>
            All results are unofficial until final ballot counts are verified by <a href="https://www.elections.on.ca/en.html">Elections Ontario</a>.
        </div>
    </section>

    <section style="border-bottom-style: solid; border-bottom-width: 1px; border-color: lightgrey; padding-top: 8px; padding-bottom: 8px; margin-bottom: 8px; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif;" class="" id="party-leaders">
        <div style="text-transform: uppercase; font-size: 12px; margin-bottom: 4px;" class="">Party Leaders</div>
        <div style="display: flex; flex-wrap: wrap;" class="pv1">
            <div style="display: flex; flex-basis: 400px; margin-bottom: 8px;" class="">
                <div style="flex-basis: 50%;" class="">
                    <div style="font-weight: 500; font-size: 16px;" class="">Doug Ford</div>
                    <div style="padding-top: 4px; padding-bottom: 4px; font-size: 10px;" class="">PC - Etobicoke North</div>
                    <div style="" class="f5">{{ data['leaders']['ford']|title }}</div>
                </div>
                <div style="flex-basis: 50%;" class="">
                    <div style="font-weight: 500; font-size: 16px;" class="">Andrea Horwath</div>
                    <div style="padding-top: 4px; padding-bottom: 4px; font-size: 10px;" class="">NDP - Hamilton Centre</div>
                    <div class="f5">{{ data['leaders']['horwath']|title }}</div>
                </div>
            </div>
            <div style="display: flex; flex-basis: 400px;" class="w-100 w-50-ns">
                <div style="flex-basis: 50%;" class="">
                    <div style="font-weight: 500; font-size: 16px;" class="">Mike Schreiner</div>
                    <div style="padding-top: 4px; padding-bottom: 4px; font-size: 10px;" class="">GRN - Guelph</div>
                    <div class="f5">{{ data['leaders']['schreiner']|title }}</div>
                </div>
                <div style="flex-basis: 50%;" class="">
                    <div style="font-weight: 500; font-size: 16px;" class="">Kathleen Wynne</div>
                    <div style="padding-top: 4px; padding-bottom: 4px; font-size: 10px;" class="">LIB - Don Valley West</div>
                    <div class="f5">{{ data['leaders']['wynne']|title }}</div>
                </div>
            </div>
        </div>
    </section>

    <section style="border-bottom-style: solid; border-bottom-width: 1px; border-color: lightgrey; padding-top: 8px; padding-bottom: 8px; font-family: -apple-system, BlinkMacSystemFont, avenir, helvetica, ubuntu, roboto, noto, arial, sans-serif;" class="" id="local-ridings">
        <div style="padding-bottom: 8px; text-transform: uppercase; font-size: 12px;" class="">Local ridings</div>
        {% for riding in data['ridings'] %}
        <button style="font-weight: 600; font-size: 16px;" class="pica-accordion">{{ riding['name']|safe }}</button>
        <div class="pica-panel">
            <table style="font-size: 12px; width: 100%; padding-top: 8px; padding-bottom: 8px; border-style: solid; border-width: 1px; border-collapse: collapse; border-spacing: 0; border-radius: .25rem; border-color: gainsboro;" class="">
                <tbody>
                    <tr class="striped--light-gray">
                        <th style="text-align: left; font-weight: 600; text-transform: uppercase; padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="f6">Party</th>
                        <th style="text-align: left; font-weight: 600; text-transform: uppercase; padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="f6">Candidate</th>
                        <th style="text-align: left; font-weight: 600; text-transform: uppercase; padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="f6">Votes</th>
                        <th style="text-align: left; font-weight: 600; text-transform: uppercase; padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="f6">Pct</th>
                    </tr>
                    {% set total = riding['candidates']|sum(attribute='votes') %}

                    {% for candidate in riding['candidates']|sort(attribute='votes', reverse=True) %}
                    <tr class="striped--light-gray">
                        <td style="padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="">{{ candidate['party'] }}</td>
                        <td style="padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="">{{ candidate['name'] }}</td>
                        <td style="padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="">{{ candidate['votes'] }}</td>
                        {% if candidate['votes'] != 0 %}
                        {% set pct = (candidate['votes'] / total) * 100 %}
                        <td style="padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="">{{ pct|round(1, 'common') }}</td>
                        {% else %}
                        <td style="padding-top: 8px; padding-bottom: 8px; padding-left: 12px; padding-right: 12px;" class="">0</td>
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
