```commandline
 
    template tags
    {% open template tag
    %} close template tag
    {{ variable open tag
    }} variable close tag
    
    - Extending template using this
        {% extends 'html file'%}
        
        {% block content%}
        {% end block%}
    - load static
        {% load static %}
    - url configration
        {% url 'url_name' %}  (<a href="{% url 'url_name' %} ">name</a>
    - Looping query set
        {% for data in queryset %}
            {{object.field_name}}
        {% endfor %}
    - Direct object of variable
        {{object.field_name}}
    - conditions
        {% if condtion %}
            
        {% endif %}
    - filters
        {{object.field_name |upper | lower | length | add "value" | date }} check documanetation
    
```