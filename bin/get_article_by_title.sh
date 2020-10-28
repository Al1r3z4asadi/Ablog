#!/bin/bash

read title

curl -X GET -H 'Content-Type: application/json' -i 'http://127.0.0.1:8000/api/v1/article/?article_title='$title''
