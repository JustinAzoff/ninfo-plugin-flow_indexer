%if not hits:
Never seen.
%else:
Seen in ${hits}. First seen on ${first_time}. Last seen on ${last_time}.

%for b in buckets:
 * ${b["bucket"]}: ${b["hits"]} hits.
%endfor
%endif
