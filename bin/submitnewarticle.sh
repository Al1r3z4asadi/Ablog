#!/bin/bash
curl --location --request POST 'http://127.0.0.1:8000/api/v1/article/submit/' \
    --header 'Authorization: Token 767ea7c06c9f0cecd734decb9a6da26ca05c8ade' \
    --form 'title=shit' \
    --form 'content=i never shied at nights' \
    --form 'category_id=1' \
    --form 'author_id=9'
