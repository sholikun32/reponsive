import streamlit as st
from streamlit import components

# Define HTML code for Tableau embed
tableau_html = """
<div class='tableauPlaceholder' id='viz1688602722091' style='position: relative'><noscript><a href='#'><img alt='Dashboard Home ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tb&#47;tb234&#47;DashboardHome&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='tb234&#47;DashboardHome' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;tb&#47;tb234&#47;DashboardHome&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1688602722091');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {{
        vizElement.style.width='1809px';
        vizElement.style.height='2757px';
    }} else if (divElement.offsetWidth > 500) {{
        vizElement.style.width='1809px';
        vizElement.style.height='2757px';
    }} else {{
        vizElement.style.width='100%';
        vizElement.style.height='2227px';
    }}
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Render the Tableau embed using components.html
st.write("Dashboard Home")
components.html(tableau_html, height=3000, scrolling=True)
