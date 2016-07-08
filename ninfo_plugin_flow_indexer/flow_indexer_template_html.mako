<%
    base_url = plugin_config['base_url']
    index = plugin_config['index']
%>
%if not hits:
Never seen.
%else:
<h3>Seen in ${hits}. First seen on ${first_time}. Last seen on ${last_time}.</h3>

<ul>
%for b in buckets:
    <li>
    ${b["bucket"]}: ${b["hits"]} hits.
    </li>
%endfor
</ul>

<a href="${base_url}v1/dump?i=${index}&q=${arg}">Dump all records</a>

%endfor
%endif
