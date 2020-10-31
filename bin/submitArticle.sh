#!/bin/bash

echo enter titlel
read title
echo enter content
read content
echo enter category id
read category
echo enter author id
read author
echo enter your token please
read -S token



curl --location --request POST 'http://127.0.0.1:8000/api/v1/article/submit/' \
--header 'Authorization: Token '$token'' \
--form 'title='$title'' \
--form 'content='$content'' \
--form 'category_id='$category'' \
--form 'author_id='$author''
